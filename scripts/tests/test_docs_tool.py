"""scripts/docs_tool.py 시험. 임시 저장소를 만들어 sync와 check, 위반 검출을 확인한다.

실행: python3 -I -m unittest discover -s scripts/tests -v
"""
import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "docs_tool.py"


def load():
    spec = importlib.util.spec_from_file_location("docs_tool_under_test", TOOL)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def write(p, text):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def make_repo(tool, root):
    """검사를 통과하는 최소 저장소: 계열 01-gpt 아래 모델 m1 하나."""
    u = root / "universal"
    write(u / "ko-core.md", "# 범용 · 한국어 공통\n> 기준일\n\n### 1.1 목표\n" + " ".join(tool.KO_CORE_KEYWORDS) + "\n")
    for d in tool.ALL_DOMAINS:
        ko = d in tool.KO_DOMAINS
        write(u / f"{d}.md",
              f"# 범용 · {d}\n\n## 1. 분야 규칙 — {d}\n본문 {d}\n"
              + ("\n<!-- BEGIN:ko-core -->\n<!-- END:ko-core -->\n" if ko else
                 f"\n<!-- BEGIN:generic -->\n## 2. 어떤 모델이든 지킬 점 — {d}\n- 범용 {d}\n<!-- END:generic -->\n"))
    m1 = root / "md" / "01-gpt" / "m1"
    write(m1 / "AGENTS.md", "# AGENTS.md\n- 전역 지침\n")
    for d in tool.ALL_DOMAINS:
        if d in tool.KO_DOMAINS:
            block = "## 2. 이 모델에서 지킬 점 (한국어 윤문)\n- 지시를 지킨다.\n" if d == "ko-academic" else ""
            tail = f"\n<!-- BEGIN:model -->\n{block}<!-- END:model -->\n"
        elif d == "web":
            tail = "\n<!-- BEGIN:generic -->\n<!-- END:generic -->\n"
        else:
            tail = "\n## 2. 이 모델에서 지킬 점 — 분야\n- 지시를 지킨다.\n"
        write(m1 / f"{d}.md",
              f"# M1 · {d}\n\n<!-- BEGIN:domain -->\n<!-- END:domain -->\n{tail}")
    write(root / "docs" / "README.md", "# docs\n")
    m = root / "docs" / "01-gpt" / "m1"
    write(m / "README.md", "# M1 색인\n")
    write(m / "sources.md", "# 출처\nhttps://example.com\n")
    write(m / "korean-writing.md", "# 한국어\nhttps://example.com\n")
    for d in tool.DOMAINS:
        write(m / "domains" / f"{d}.md", "# 분야\nhttps://example.com\n")


class Base(unittest.TestCase):
    def setUp(self):
        self.tool = load()
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.root = root
        make_repo(self.tool, root)
        self.tool.ROOT, self.tool.UNIV = root, root / "universal"
        self.tool.MD, self.tool.DOCS = root / "md", root / "docs"

    def run_tool(self, fn, *args):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = fn(*args)
        return code, buf.getvalue()

    def synced(self):
        code, out = self.run_tool(self.tool.sync)
        self.assertEqual(code, 0, out)


class ResearchMarkerTest(unittest.TestCase):
    def setUp(self):
        self.tool = load()

    def labels(self, text, skip_tags=False):
        return " ".join(self.tool.research_hits(text, skip_tags))

    def test_url(self):
        self.assertIn("출처 URL", self.labels("참고 https://a.b"))

    def test_tag(self):
        self.assertIn("근거 수준 태그", self.labels("사실이다 [부분]"))
        self.assertNotIn("근거 수준 태그", self.labels("사실이다 [부분]", skip_tags=True))

    def test_price(self):
        self.assertIn("가격", self.labels("입력 $4"))

    def test_clean_text(self):
        self.assertEqual(self.tool.research_hits("그냥 지침 문장이다."), [])


class InjectTest(unittest.TestCase):
    def test_inject_replaces_block(self):
        tool = load()
        text = "a\n<!-- BEGIN:x -->\nold\n<!-- END:x -->\nb\n"
        self.assertEqual(tool.inject(text, "x", "new"), "a\n<!-- BEGIN:x -->\nnew\n<!-- END:x -->\nb\n")

    def test_inject_missing_marker(self):
        self.assertIsNone(load().inject("no markers", "x", "new"))

    def test_fact_rows(self):
        tool = load()
        text = "### 1.2 시점에 민감한 사실\n문장\n\n| 항목 | 내용 |\n|---|---|\n| A | 내용A |\n| B | 내용B |\n\n### 1.3 다음\n| C | 무시 |\n"
        rows = tool.fact_rows(text)
        self.assertEqual(sorted(rows), ["A", "B"])
        self.assertEqual(rows["A"][1], "내용A")


class SyncCheckTest(Base):
    def test_sync_then_check_passes(self):
        self.synced()
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 0, out)

    def test_sync_injects_domain_block(self):
        self.synced()
        app = (self.root / "md/01-gpt/m1/app.md").read_text(encoding="utf-8")
        self.assertIn("## 1. 분야 규칙 — app", app)
        self.assertIn("## 2. 이 모델에서 지킬 점", app)
        self.assertNotIn("어떤 모델이든", app)

    def test_sync_injects_generic_block_when_no_model_section(self):
        self.synced()
        web = (self.root / "md/01-gpt/m1/web.md").read_text(encoding="utf-8")
        self.assertIn("## 2. 어떤 모델이든 지킬 점 — web", web)
        self.assertNotIn("본문 web\n\n<!-- BEGIN:generic", web.split("<!-- END:domain -->")[0])

    def test_generic_and_model_section_together_is_rejected(self):
        self.synced()
        p = self.root / "md/01-gpt/m1/web.md"
        p.write_text(p.read_text(encoding="utf-8") + "\n## 2. 이 모델에서 지킬 점 — web\n- 중복\n", encoding="utf-8")
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("하나만 둔다", out)

    def test_out_of_sync_generic_is_rejected(self):
        self.synced()
        p = self.root / "md/01-gpt/m1/web.md"
        p.write_text(p.read_text(encoding="utf-8").replace("- 범용 web", "- 다른 내용"), encoding="utf-8")
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("generic 블록이 원본과 다름", out)

    def test_sync_propagates_ko_model_block_to_siblings(self):
        self.synced()
        ko = (self.root / "md/01-gpt/m1/ko-literary.md").read_text(encoding="utf-8")
        self.assertIn("지시를 지킨다.", ko)

    def test_domain_part_expands_ko_core_without_markers(self):
        self.synced()
        text = (self.root / "md/01-gpt/m1/ko-everyday.md").read_text(encoding="utf-8")
        self.assertIn("### 1.1 목표", text)
        self.assertNotIn("BEGIN:ko-core", text)

    def test_url_in_md_is_rejected(self):
        self.synced()
        p = self.root / "md/01-gpt/m1/web.md"
        p.write_text(p.read_text(encoding="utf-8") + "\n참고 https://example.com\n", encoding="utf-8")
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("출처 URL", out)

    def test_price_and_tag_in_md_are_rejected(self):
        self.synced()
        p = self.root / "md/01-gpt/m1/app.md"
        p.write_text(p.read_text(encoding="utf-8") + "\n가격 $4 [부분]\n", encoding="utf-8")
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("가격", out)
        self.assertIn("근거 수준 태그", out)

    def test_phrase_duplicated_from_global_is_rejected(self):
        self.synced()
        p = self.root / "md/01-gpt/m1/web.md"
        p.write_text(p.read_text(encoding="utf-8") + "- 첫머리에서 복명복창한다.\n", encoding="utf-8")
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("전역 지침과 겹치는 표현", out)

    def test_extra_section_in_md_is_rejected(self):
        self.synced()
        p = self.root / "md/01-gpt/m1/web.md"
        p.write_text(p.read_text(encoding="utf-8") + "\n## 3. 덧붙임\n", encoding="utf-8")
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("'## 2.' 절만", out)

    def test_general_doc_is_rejected(self):
        self.synced()
        write(self.root / "md/01-gpt/m1/general.md", "# M1 · general\n")
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("general.md는 없앴다", out)

    def test_out_of_sync_block_is_rejected(self):
        self.synced()
        p = self.root / "md/01-gpt/m1/app.md"
        p.write_text(p.read_text(encoding="utf-8").replace("본문 app", "다른 본문"), encoding="utf-8")
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("domain 블록이 원본과 다름", out)

    def test_missing_domain_doc_is_error_when_complete(self):
        self.synced()
        (self.root / "md/01-gpt/m1/ko-everyday.md").unlink()
        self.assertEqual(self.run_tool(self.tool.check, True, False)[0], 1)
        self.assertEqual(self.run_tool(self.tool.check, False, False)[0], 0)

    def test_missing_global_file_is_error_when_complete(self):
        self.synced()
        (self.root / "md/01-gpt/m1/AGENTS.md").unlink()
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("전역 지침", out)

    def test_missing_docs_pair_is_error_when_complete(self):
        self.synced()
        (self.root / "docs/01-gpt/m1/sources.md").unlink()
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("sources.md", out)

    def test_korean_domain_only_for_ko_families(self):
        self.synced()
        extra = self.root / "md" / "02-claude" / "x"
        body = ("# X\n\n<!-- BEGIN:domain -->\n<!-- END:domain -->\n\n"
                "<!-- BEGIN:model -->\n<!-- END:model -->\n")
        write(extra / "ko-academic.md", body)
        # claude는 KO_FAMILIES에 있으므로 허용, deepseek 같은 계열은 거부
        write(self.root / "md" / "05-deepseek" / "x" / "ko-academic.md", body)
        code, out = self.run_tool(self.tool.check, False, True)
        self.assertEqual(code, 1)
        self.assertIn("한국어 윤문 분야는", out)

    def test_shared_dir_is_rejected(self):
        self.synced()
        (self.root / "_shared").mkdir()
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("_shared", out)

    def test_old_family_root_is_rejected(self):
        self.synced()
        (self.root / "gpt").mkdir()
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("옛 위치", out)

    def test_effort_level_is_rejected_in_domain_doc(self):
        self.synced()
        p = self.root / "md/01-gpt/m1/app.md"
        p.write_text(p.read_text(encoding="utf-8") + "- `xhigh`에서 시작한다.\n", encoding="utf-8")
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("추론 강도 단계", out)

    def test_effort_level_is_rejected_in_global_file(self):
        self.synced()
        g = self.root / "md/01-gpt/m1/AGENTS.md"
        g.write_text("# AGENTS.md\n- effort를 올려서 쓴다\n", encoding="utf-8")
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("추론 강도 단계", out)

    def test_global_file_too_long_is_rejected(self):
        self.synced()
        g = self.root / "md/01-gpt/m1/AGENTS.md"
        g.write_text("# AGENTS.md\n" + "- 규칙 번호 %d\n" * 0 + "".join(f"- 규칙 {i} 항목\n" for i in range(210)), encoding="utf-8")
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("AGENTS.md", out)

    def test_global_file_duplicate_line_is_rejected(self):
        self.synced()
        g = self.root / "md/01-gpt/m1/AGENTS.md"
        g.write_text("# AGENTS.md\n- 같은 항목을 두 번 쓴다\n- 같은 항목을 두 번 쓴다\n", encoding="utf-8")
        code, out = self.run_tool(self.tool.check, True, False)
        self.assertEqual(code, 1)
        self.assertIn("반복됨", out)


class FactTableTest(Base):
    def add_table(self, level="부분", docs_content="내용A"):
        u = self.root / "universal" / "web.md"
        text = u.read_text(encoding="utf-8")
        text += ("\n### 1.2 시점에 민감한 사실\n아래 표는 확정된 사실이 아니라 확인의 출발점이다.\n\n"
                 "| 항목 | 내용 |\n|---|---|\n| A | 내용A |\n")
        u.write_text(text, encoding="utf-8")
        write(self.root / "docs/_common/domain-rules/web.md",
              f"# x\n\n| 항목 | 근거 수준 | 내용 |\n|---|---|---|\n| A | {level} | {docs_content} |\n")

    def errors(self):
        errs = []
        self.tool.check_fact_tables(errs)
        return errs

    def test_matching_tables_pass(self):
        self.add_table()
        self.assertEqual(self.errors(), [])

    def test_content_mismatch(self):
        self.add_table(docs_content="다른 내용")
        self.assertTrue(any("내용이" in e for e in self.errors()))

    def test_invalid_level(self):
        self.add_table(level="아마도")
        self.assertTrue(any("허용값" in e for e in self.errors()))

    def test_missing_hedge_sentence(self):
        self.add_table()
        u = self.root / "universal" / "web.md"
        u.write_text(u.read_text(encoding="utf-8").replace("확정된 사실이 아니라", "사실이다"), encoding="utf-8")
        self.assertTrue(any("명령문이 없음" in e for e in self.errors()))

    def test_row_missing_in_docs(self):
        self.add_table()
        write(self.root / "docs/_common/domain-rules/web.md", "# x\n\n| 항목 | 근거 수준 | 내용 |\n|---|---|---|\n")
        self.assertTrue(any("근거 수준 행 없음" in e for e in self.errors()))


if __name__ == "__main__":
    unittest.main()
