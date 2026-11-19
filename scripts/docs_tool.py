#!/usr/bin/env python3
"""LLM 컨텍스트용 지침(universal/, md/)과 사람이 읽는 조사 기록(docs/)을 관리한다.

사용법:
  python3 -I scripts/docs_tool.py sync              # 분야 규칙 블록을 md/ 문서에 주입
  python3 -I scripts/docs_tool.py check             # 구조·분리 검사 (누락은 경고)
  python3 -I scripts/docs_tool.py check --complete  # 모델 폴더마다 분야 문서와 docs 대응을 필수로 검사
  python3 -I scripts/docs_tool.py check --skip-blocks  # 주입 전 초안: 블록 일치 비교 생략

루트 폴더:
  universal/                      모델에 상관없이 쓰는 범용 지침. 분야 문서 8개 + 한국어 윤문 3개 + ko-core.md
  md/<계열>/<모델>/               전역 지침(AGENTS·CLAUDE·GEMINI.md 중 하나) + 분야 문서
      <분야>.md                  분야 규칙(범용 지침과 같음) + 이 모델에서 지킬 점
  docs/<계열>/<모델>/             조사·검증·근거 기록. 컨텍스트에 넣지 않는다.
      README · overview · performance · operations · critique · sources · xcheck .md
      domains/<분야>.md           md의 분야 문서 8개의 대응 문서(모델×분야 운용 조사와 출처)
      korean-writing.md          한국어 윤문 3분야(ko-*)의 모델별 조사 기록
  universal/·md/ 문서에는 근거·출처·가격·벤치마크·비판을 두지 않는다. docs/에 둔다.

분야 문서에는 전역 지침과 겹치는 규칙(복명복창, 5항목 보고, 작업 원칙, 모델 공통 수칙)을 두지 않는다.
전역 지침이 이미 읽히기 때문이다. 겹치면 두 문서가 어긋날 때 모델이 임의로 하나를 고른다.

원본(정본)의 위치:
  한국어 공통 원리 universal/ko-core.md          → universal/ko-*.md 의 <!-- BEGIN:ko-core --> 블록
  분야 규칙       universal/<분야>.md            → md/<계열>/<모델>/<분야>.md 의 <!-- BEGIN:domain --> 블록
  한국어 모델 지침 md/<계열>/<모델>/ko-academic.md 의 <!-- BEGIN:model --> 블록 → 같은 모델의 ko-everyday, ko-literary
  모델×분야 지침  md/<계열>/<모델>/<분야>.md 의 '## 2.' 절 (손으로 쓴다. 근거는 docs/<계열>/<모델>/domains/<분야>.md)
  범용 2절        universal/<분야>.md 의 <!-- BEGIN:generic --> 블록 → 모델 전용 2절이 없는 md 문서에 주입. 모델 전용 2절을 쓰면 generic 블록을 지운다.
                 근거는 docs/_common/generic-notes.md
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UNIV = ROOT / "universal"
MD = ROOT / "md"
DOCS = ROOT / "docs"
# 계열 폴더는 번호를 앞에 붙인다(인지도 순). 번호 규칙은 README.md의 "디렉터리 구조"에 있다.
FAMILIES = ["01-gpt", "02-claude", "03-gemini", "04-grok", "05-deepseek", "06-qwen",
            "07-kimi", "08-glm", "09-gemma", "10-muse", "11-minimax",
            "12-mistral", "13-microsoft", "14-nvidia", "15-tencent", "16-baidu", "17-thinking-machines",
            "18-lg", "19-sk-telecom", "20-upstage", "21-motif", "22-naver", "23-kakao", "24-kt",
            "25-krafton", "26-xiaomi"]
DOMAINS = ["web", "app", "native", "hardware", "firmware",
           "web-research", "research", "tech-research"]
GLOBAL_FILES = ["AGENTS.md", "CLAUDE.md", "GEMINI.md"]
KO_DOMAINS = ["ko-academic", "ko-everyday", "ko-literary"]
KO_FAMILIES = ["gpt", "claude", "gemini", "gemma"]  # 번호를 뗀 계열 이름
ALL_DOMAINS = DOMAINS + KO_DOMAINS
KO_DOC = "korean-writing"
MODEL_DOC_NAMES = {"README", "overview", "performance", "operations", "critique", "sources", "xcheck", KO_DOC}
KO_MODEL_SOURCE = "ko-academic"
# 추론 강도(effort·thinking 단계) 설정은 지침 문서에 쓰지 않는다. 도구와 사용자 설정이 정한다.
EFFORT_PATTERN = re.compile(
    r"`(?:max|xhigh|high|medium|low|minimal|none|MINIMAL|LOW|MEDIUM|HIGH)`|(?<![A-Za-z])(?:effort|xhigh)(?![A-Za-z])|thinking_level|추론 단계|추론 강도|생각 수준|생각 단계|최고 단계|효과 설정|추론 모드|(?<![A-Za-z_])max(?![A-Za-z_]) 단계|노력 단계")

# 전역 지침이 맡는 규칙이다. 분야 문서(한국어 윤문 제외)에 다시 쓰면 중복이므로 검사가 막는다.
GLOBAL_DUP_PHRASES = ["복명복창", "5항목", "God-object", "500줄", "Co-Authored-By"]
# 사용자가 요구한 항목이 한국어 공통 원리에서 빠지면 검사가 실패한다.
KO_CORE_KEYWORDS = ["흐름", "호흡", "과서술", "대구", "도치", "감정", "번역투",
                    "윤문 순환", "측정", "라이선스"]
# 컨텍스트로 들어가는 글에 있으면 안 되는 리서치 표지.
RESEARCH_MARKERS = [
    (re.compile(r"https?://"), "출처 URL"),
    (re.compile(r"\[(?:확인|부분|미확인|추정|권고)[^\]]*\]"), "근거 수준 태그"),
    (re.compile(r"근거와 한계|근거 표기"), "근거 절"),
    (re.compile(r"\$\s?\d"), "가격"),
    (re.compile(r"Artificial Analysis|SWE-bench|Terminal-Bench|LMArena|EQ-Bench|KatFishNet"), "벤치마크·연구 출처"),
]
HARD_LIMIT = 200  # Claude Code 공식 안내: 파일당 200줄 아래
SOFT_LIMIT = 120


def block_re(name):
    return re.compile(rf"(<!-- BEGIN:{name} -->\n)(.*?)(<!-- END:{name} -->)", re.S)


def read(p):
    return p.read_text(encoding="utf-8")


def block_of(text, name):
    m = block_re(name).search(text)
    return m.group(2).strip("\n") if m else None


def strip_blocks(text, names):
    for n in names:
        text = block_re(n).sub("", text)
    return text


def from_marker(text, marker):
    i = text.find(marker)
    return text[i:].strip("\n") if i >= 0 else ""


def ko_core_text():
    t = read(UNIV / "ko-core.md")
    m = re.search(r"^### ", t, re.M)
    return t[m.start():].strip("\n") if m else ""


def domain_part(d):
    """범용 문서에서 분야 규칙 본문. ko-core 표식은 걷어 낸다."""
    part = from_marker(read(UNIV / f"{d}.md"), "## 1. 분야 규칙")
    part = part.split("<!-- BEGIN:generic -->")[0]
    return re.sub(r"<!-- (?:BEGIN|END):ko-core -->\n?", "", part).strip("\n")


def generic_part(d):
    """범용 문서의 '어떤 모델이든 지킬 점' 본문. 모델 전용 2절이 없는 md 문서에 들어간다."""
    return block_of(read(UNIV / f"{d}.md"), "generic")


def fam_key(fam):
    """'01-gpt' -> 'gpt'. 계열 폴더의 번호 접두를 뗀 이름."""
    return re.sub(r"^\d+-", "", fam)


def md_files():
    for fam in FAMILIES:
        for p in sorted((MD / fam).glob("*/*.md")):
            if p.name in GLOBAL_FILES:
                continue
            yield p


def parts(p):
    return p.parent.parent.name, p.parent.name, p.stem


def ko_model_text(fam, model):
    """한국어 윤문 3문서가 공유하는 모델 지침 블록의 원본."""
    p = MD / fam / model / f"{KO_MODEL_SOURCE}.md"
    return block_of(read(p), "model") if p.exists() else None


def research_hits(text, skip_tags=False):
    hits = []
    for rx, label in RESEARCH_MARKERS:
        if skip_tags and label == "근거 수준 태그":
            continue
        m = rx.search(text)
        if m:
            hits.append(f"{label} '{m.group(0)[:30]}'")
    return hits


def inject(text, name, body):
    rx = block_re(name)
    if not rx.search(text):
        return None
    return rx.sub(lambda m: m.group(1) + body + "\n" + m.group(3), text, count=1)


def sync():
    ko_core = ko_core_text() if (UNIV / "ko-core.md").exists() else ""
    changed = 0
    for d in KO_DOMAINS:
        p = UNIV / f"{d}.md"
        if not p.exists():
            continue
        text = read(p)
        new = inject(text, "ko-core", ko_core)
        if new is None:
            print(f"ERROR {p.relative_to(ROOT)}: BEGIN/END:ko-core 마커 없음")
            return 1
        if new != text:
            p.write_text(new, encoding="utf-8")
            changed += 1
    for p in md_files():
        fam, model, dom = parts(p)
        if dom not in ALL_DOMAINS or not (UNIV / f"{dom}.md").exists():
            print(f"SKIP  {p.relative_to(ROOT)} (범용 지침 없음: {dom})")
            continue
        text = read(p)
        new = inject(text, "domain", domain_part(dom))
        if new is None:
            print(f"ERROR {p.relative_to(ROOT)}: BEGIN/END:domain 마커 없음")
            return 1
        if dom in DOMAINS and block_re("generic").search(new):
            gtext = generic_part(dom)
            if not gtext:
                print(f"ERROR universal/{dom}.md: generic 블록이 비어 있음")
                return 1
            new = inject(new, "generic", gtext)
        if dom in KO_DOMAINS:
            mtext = ko_model_text(fam, model)
            if not mtext:
                print(f"ERROR {p.relative_to(ROOT)}: 한국어 모델 지침 원본 블록이 비어 있음 ({KO_MODEL_SOURCE}.md)")
                return 1
            new = inject(new, "model", mtext)
            if new is None:
                print(f"ERROR {p.relative_to(ROOT)}: BEGIN/END:model 마커 없음")
                return 1
        if new != text:
            p.write_text(new, encoding="utf-8")
            changed += 1
    print(f"sync 완료: {changed}개 파일 갱신")
    return 0


def check_universal(errors, skip_blocks):
    for need in ["ko-core.md"] + [f"{d}.md" for d in ALL_DOMAINS]:
        if not (UNIV / need).exists():
            errors.append(f"universal/{need} 없음")
    for gone in ("contract.md", "general.md"):
        if (UNIV / gone).exists():
            errors.append(f"universal/{gone}: 없앤 문서다. 전역 지침(AGENTS·CLAUDE·GEMINI.md)과 겹친다")
    if (UNIV / "ko-core.md").exists():
        core = read(UNIV / "ko-core.md")
        for kw in KO_CORE_KEYWORDS:
            if kw not in core:
                errors.append(f"universal/ko-core.md: 필수 키워드 누락 '{kw}'")
        for hit in research_hits(core):
            errors.append(f"universal/ko-core.md: 컨텍스트 지침에 리서치 표지 {hit}")
        ko_core = ko_core_text()
    else:
        ko_core = ""
    for f in sorted(UNIV.glob("*.md")):
        n = len(read(f).splitlines())
        if n > HARD_LIMIT:
            errors.append(f"universal/{f.name}: {n}줄 > {HARD_LIMIT}")
    for d in ALL_DOMAINS:
        p = UNIV / f"{d}.md"
        if not p.exists():
            continue
        rel = f"universal/{d}.md"
        text = read(p)
        if "## 1. 분야 규칙" not in text:
            errors.append(f"{rel}: '## 1. 분야 규칙' 절 없음")
        if not text.startswith("# "):
            errors.append(f"{rel}: 첫 줄이 H1 제목이 아님")
        if d in KO_DOMAINS:
            got = block_of(text, "ko-core")
            if got is None:
                errors.append(f"{rel}: ko-core 블록 마커 없음")
            elif not skip_blocks and got != ko_core:
                errors.append(f"{rel}: ko-core 블록이 원본과 다름 (sync 필요)")
        else:
            for phrase in GLOBAL_DUP_PHRASES:
                if phrase in text:
                    errors.append(f"{rel}: 전역 지침과 겹치는 표현 '{phrase}'")
            if EFFORT_PATTERN.search(text):
                errors.append(f"{rel}: 추론 강도 단계 언급 '{EFFORT_PATTERN.search(text).group(0)}'")
            g = block_of(text, "generic")
            if not g or not g.startswith("## 2. "):
                errors.append(f"{rel}: generic 블록('## 2. 어떤 모델이든 지킬 점')이 없음")
        for hit in research_hits(text):
            errors.append(f"{rel}: 컨텍스트 지침에 리서치 표지 {hit}")


def check_md(errors, warns, skip_blocks):
    count = 0
    for p in md_files():
        count += 1
        fam, model, dom = parts(p)
        rel = str(p.relative_to(ROOT))
        text = read(p)
        lines = text.splitlines()
        if dom not in ALL_DOMAINS:
            hint = " (general.md는 없앴다. 전역 지침이 그 역할을 한다)" if dom == "general" else ""
            errors.append(f"{rel}: 허용되지 않은 분야 이름 '{dom}'{hint}")
            continue
        if dom in KO_DOMAINS and fam_key(fam) not in KO_FAMILIES:
            errors.append(f"{rel}: 한국어 윤문 분야는 {', '.join(KO_FAMILIES)} 계열에만 둔다")
            continue
        if len(lines) > HARD_LIMIT:
            errors.append(f"{rel}: {len(lines)}줄 > {HARD_LIMIT}")
        elif len(lines) > SOFT_LIMIT:
            warns.append(f"{rel}: {len(lines)}줄 (권장 {SOFT_LIMIT} 이하)")
        if not lines or not lines[0].startswith("# "):
            errors.append(f"{rel}: 첫 줄이 H1 제목이 아님")
        domain = domain_part(dom) if (UNIV / f"{dom}.md").exists() else ""
        got = block_of(text, "domain")
        if got is None:
            errors.append(f"{rel}: domain 블록 마커 없음")
        elif not skip_blocks and got != domain:
            errors.append(f"{rel}: domain 블록이 원본과 다름 (sync 필요)")
        own = strip_blocks(text, ["domain", "model", "generic"])
        if dom in KO_DOMAINS:
            mtext = ko_model_text(fam, model)
            got = block_of(text, "model")
            if got is None:
                errors.append(f"{rel}: model 블록 마커 없음")
            elif mtext is None:
                errors.append(f"{rel}: 한국어 모델 지침 원본 파일 없음 ({KO_MODEL_SOURCE}.md)")
            elif not mtext.startswith("## 2. "):
                errors.append(f"{rel}: 한국어 모델 지침 블록이 '## 2. '로 시작해야 함")
            elif not skip_blocks and got != mtext:
                errors.append(f"{rel}: model 블록이 원본과 다름 (sync 필요)")
        else:
            if block_of(text, "model") is not None:
                errors.append(f"{rel}: model 블록은 한국어 윤문 문서에만 둔다. 모델 지침은 '## 2.' 절에 직접 쓴다")
            for phrase in GLOBAL_DUP_PHRASES:
                if phrase in text:
                    errors.append(f"{rel}: 전역 지침과 겹치는 표현 '{phrase}'")
            if EFFORT_PATTERN.search(text):
                errors.append(f"{rel}: 추론 강도 단계 언급 '{EFFORT_PATTERN.search(text).group(0)}'")
            for h in re.findall(r"^## .*$", own, re.M):
                if not h.startswith("## 2. "):
                    errors.append(f"{rel}: 분야 규칙 밖에는 '## 2.' 절만 둘 수 있음 ({h})")
            has_generic = block_of(text, "generic") is not None
            has_own = bool(re.search(r"^## 2\. ", own, re.M))
            if has_generic and has_own:
                errors.append(f"{rel}: 모델 전용 '## 2.' 절과 generic 블록이 함께 있음. 하나만 둔다")
            elif not has_generic and not has_own:
                warns.append(f"{rel}: '## 2.' 절도 generic 블록도 없음")
            elif has_generic and not skip_blocks and dom in DOMAINS and block_of(text, "generic") != generic_part(dom):
                errors.append(f"{rel}: generic 블록이 원본과 다름 (sync 필요)")
        for hit in research_hits(text):
            errors.append(f"{rel}: 컨텍스트 문서에 리서치 표지 {hit} — docs/로 옮긴다")
        for bad in ("TODO", "TBD", "[PROJECT_NAME]"):
            if bad in own:
                errors.append(f"{rel}: 자리표시자 '{bad}' 남아 있음")
    return count


def check_global_files(errors):
    """모델 폴더의 전역 지침(AGENTS·CLAUDE·GEMINI.md)도 200줄 아래, 리서치 표지 없음, 같은 줄 반복 없음을 지킨다."""
    for fam in FAMILIES:
        for p in sorted((MD / fam).glob("*/*.md")):
            if p.name not in GLOBAL_FILES:
                continue
            rel = str(p.relative_to(ROOT))
            text = read(p)
            n = len(text.splitlines())
            if n > HARD_LIMIT:
                errors.append(f"{rel}: {n}줄 > {HARD_LIMIT}")
            for hit in research_hits(text, skip_tags=True):
                errors.append(f"{rel}: 전역 지침에 리서치 표지 {hit}")
            if EFFORT_PATTERN.search(text):
                errors.append(f"{rel}: 추론 강도 단계 언급 '{EFFORT_PATTERN.search(text).group(0)}'")
            seen = set()
            for line in text.splitlines():
                if line.startswith("- "):
                    key = line[:40]
                    if key in seen:
                        errors.append(f"{rel}: 같은 항목이 반복됨 '{key}'")
                    seen.add(key)


FACT_HEAD = "시점에 민감한 사실"
FACT_HEDGE = "확정된 사실이 아니라"
FACT_LEVELS = {"확인", "부분", "미확인", "추정"}


def fact_rows(text):
    """'시점에 민감한 사실' 절의 표 행을 {항목: 셀 목록}으로 돌려준다. 표가 없으면 빈 dict."""
    if FACT_HEAD not in text:
        return {}
    body = text.split(FACT_HEAD, 1)[1].split("\n### ", 1)[0]
    rows = {}
    for line in body.splitlines():
        if line.startswith("| ") and not line.startswith("| 항목"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows[cells[0]] = cells
    return rows


def check_fact_tables(errors):
    """universal의 사실 표와 docs/_common/domain-rules의 근거 수준 표가 행 단위로 같은지 본다."""
    for d in DOMAINS:
        up = UNIV / f"{d}.md"
        if not up.exists():
            continue
        utext = read(up)
        urows = fact_rows(utext)
        if not urows:
            continue
        rel = f"universal/{d}.md"
        if FACT_HEDGE not in utext:
            errors.append(f"{rel}: 사실 표 위에 '확정된 사실이 아니라 확인의 출발점'이라는 명령문이 없음")
        dp = DOCS / "_common" / "domain-rules" / f"{d}.md"
        if not dp.exists():
            errors.append(f"docs/_common/domain-rules/{d}.md 없음 ({rel}에 사실 표가 있음)")
            continue
        drows = {}  # docs 표는 절 제목이 없어 표 행을 직접 읽는다
        for line in read(dp).splitlines():
            if line.startswith("| ") and not line.startswith("| 항목"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                drows[cells[0]] = cells
        for item, cells in urows.items():
            got = drows.get(item)
            if got is None:
                errors.append(f"docs/_common/domain-rules/{d}.md: 항목 '{item}'의 근거 수준 행 없음")
            elif len(got) < 3 or got[2] != cells[1]:
                errors.append(f"docs/_common/domain-rules/{d}.md: 항목 '{item}'의 내용이 {rel}와 다름")
            elif got[1] not in FACT_LEVELS:
                errors.append(f"docs/_common/domain-rules/{d}.md: 항목 '{item}'의 근거 수준 '{got[1]}'이 허용값이 아님")
        for item in drows:
            if item not in urows:
                errors.append(f"docs/_common/domain-rules/{d}.md: 항목 '{item}'이 {rel}에 없음")


def check_docs(errors, warns, complete):
    if not (DOCS / "README.md").exists():
        errors.append("docs/README.md 없음")
    models = {}
    for p in md_files():
        fam, model, dom = parts(p)
        models.setdefault((fam, model), set()).add(dom)
    for (fam, model), have in sorted(models.items()):
        need = DOMAINS + (KO_DOMAINS if fam_key(fam) in KO_FAMILIES else [])
        miss = [d for d in need if d not in have]
        if miss:
            msg = f"md/{fam}/{model}: 분야 문서 {len(miss)}개 누락 ({', '.join(miss)})"
            (errors if complete else warns).append(msg)
        mdir = DOCS / fam / model
        globals_ = [g for g in GLOBAL_FILES if (MD / fam / model / g).exists()]
        if len(globals_) != 1:
            msg = f"md/{fam}/{model}: 전역 지침({', '.join(GLOBAL_FILES)})이 정확히 하나여야 함 (현재 {len(globals_)}개)"
            (errors if complete else warns).append(msg)
        want = ["README.md", "sources.md"]
        want += [f"domains/{d}.md" for d in have if d in DOMAINS]
        want += ["korean-writing.md"] if have & set(KO_DOMAINS) else []
        for rel_name in want:
            if not (mdir / rel_name).exists():
                (errors if complete else warns).append(f"docs/{fam}/{model}/{rel_name} 없음 (md의 대응 조사 기록)")
    for fam in FAMILIES:
        for mdir in sorted(p for p in (DOCS / fam).glob("*") if p.is_dir()):
            for dp in sorted([*mdir.glob("*.md"), *(mdir / "domains").glob("*.md")]):
                rel = str(dp.relative_to(ROOT))
                in_domains = dp.parent.name == "domains"
                text = read(dp)
                if not text.startswith("# "):
                    errors.append(f"{rel}: 첫 줄이 H1 제목이 아님")
                if in_domains and dp.stem not in DOMAINS:
                    warns.append(f"{rel}: 대응하는 md 분야 이름이 아님")
                if not in_domains and dp.stem not in MODEL_DOC_NAMES:
                    warns.append(f"{rel}: 알려진 조사 기록 이름이 아님 ({', '.join(sorted(MODEL_DOC_NAMES))})")
                if (in_domains or dp.stem in ("sources", KO_DOC)) and "http" not in text:
                    errors.append(f"{rel}: 조사 기록에 출처 URL 없음")
                if len(text.splitlines()) > HARD_LIMIT:
                    errors.append(f"{rel}: {len(text.splitlines())}줄 > {HARD_LIMIT}")


def check(complete, skip_blocks=False):
    errors, warns = [], []
    for fam in FAMILIES:
        for old in (fam, fam_key(fam)):
            if (ROOT / old).exists():
                errors.append(f"{old}/: 옛 위치다. md/{fam}/ 와 docs/{fam}/ 로 나눈다")
    if (ROOT / "_shared").exists():
        errors.append("_shared/: 없앤 폴더다. 범용 지침은 universal/, 모델 지침은 md/에 둔다")
    check_universal(errors, skip_blocks)
    count = check_md(errors, warns, skip_blocks)
    check_global_files(errors)
    check_docs(errors, warns, complete)
    check_fact_tables(errors)
    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    models = {p.parent for p in md_files()}
    print(f"check: md 문서 {count}개, 모델 폴더 {len(models)}개, 경고 {len(warns)}, 오류 {len(errors)}")
    return 1 if errors else 0


def main(argv):
    if len(argv) >= 2 and argv[1] == "sync":
        return sync()
    if len(argv) >= 2 and argv[1] == "check":
        return check("--complete" in argv, "--skip-blocks" in argv)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
