"""입버릇 낱말 규칙: 규칙마다 걸리는 글과 안 걸리는 글. 여러 번 나와야 세는 규칙은 반복해서 넣는다."""
import unittest

import _path  # noqa: F401
from ai_smell.detect import analyze
from ai_smell.rules import ko_tics

# (규칙 id, 걸려야 하는 한 문장, 걸리면 안 되는 한 문장, 반복 횟수)
CASES = [
    ("ko.tic.value-figurative", "그 일은 해 볼 값어치가 있다.", "입력값을 검증한다.", 1),
    ("ko.tic.value-bare", "값이 바뀐다. 값을 읽는다.", "기본값이 바뀐다. 반환값을 읽는다.", 5),
    ("ko.tic.judge", "그렇게 판단한다.", "그렇게 정한다.", 5),
    ("ko.tic.criterion-becomes", "이 수치가 기준이 된다.", "이 수치를 쓴다.", 2),
    ("ko.tic.criterion-bare", "기준을 정한다.", "조건을 정한다.", 6),
    ("ko.tic.test-heavy", "시험을 돌린다.", "검사를 돌린다.", 6),
    ("ko.tic.test-bench", "이번 일이 시험대에 올랐다.", "이번 일을 마쳤다.", 1),
    ("ko.tic.pivotal", "속도가 관건이다.", "속도가 필요하다.", 1),
    ("ko.tic.trail", "조건이 따라붙는다.", "조건이 있다.", 2),
    ("ko.tic.defer", "결정을 미뤘다.", "결정을 했다.", 2),
    ("ko.tic.crossover", "다음 주제로 넘어갑니다.", "다음 주제를 봅니다.", 3),
    ("ko.tic.continues", "문제가 다른 문제로 이어집니다.", "문제가 다른 문제를 낳는다.", 4),
    ("ko.tic.draw-line", "여기서 선을 긋는다.", "여기서 멈춘다.", 1),
    ("ko.tic.win-lose", "이 모델이 이겼다. 저 모델은 밀렸다.", "이 모델이 앞선다.", 1),
    ("ko.tic.stand", "그 모델이 우위에 선다. 저 모델은 뒤에 섭니다.", "의자에 앉는다.", 1),
    ("ko.tic.exceed", "기준을 웃돈다.", "기준에 못 미친다.", 2),
    ("ko.tic.put-forward", "장점을 내세운다.", "장점을 쓴다.", 2),
    ("ko.tic.claim", "그렇게 주장한다.", "그렇게 말한다.", 5),
    ("ko.tic.demand", "조건을 요구한다.", "조건을 둔다.", 5),
    ("ko.tic.widen", "범위를 넓힌다.", "범위가 넓다.", 2),
    ("ko.tic.apply", "규칙을 적용한다.", "규칙을 쓴다.", 5),
    ("ko.tic.dress-up", "보고를 그럴듯하게 꾸민다.", "보고를 쓴다.", 2),
    ("ko.tic.back-up", "자료가 주장을 뒷받침한다.", "자료가 주장에 힘을 싣는다.", 2),
    ("ko.tic.adapt", "환경에 적응한다.", "환경에 맞춘다.", 3),
    ("ko.term.release", "릴리스 노트를 쓴다.", "릴리즈 노트를 쓴다.", 1),
    ("ko.term.harness", "하네즈를 만든다.", "하네스를 만든다.", 1),
    ("ko.tic.corpus", "말뭉치를 만든다.", "자료를 만든다.", 2),
    ("ko.tic.shape", "경로는 이런 모양입니다.", "경로는 이렇게 씁니다.", 1),
    ("ko.tic.unrelated", "이 숫자는 지침의 뜻과는 상관이 없습니다.", "이 숫자는 정렬에 씁니다.", 1),
    ("ko.tic.whole", "전체 목록을 본다. 계열 전체를 본다.", "목록을 본다.", 4),
    ("ko.tic.contract-word", "응답 계약을 따른다.", "공통 규칙을 따른다.", 1),
    ("ko.tic.same-as", "어느 문서든 같은 순서로 이루어져 있습니다.", "어느 문서든 순서가 있습니다.", 1),
    ("ko.tic.among", "답은 세 가지 중 하나다.", "답은 하나다.", 2),
    ("ko.tic.empty-answer", "빈 답변이 돌아왔다.", "답이 돌아왔다.", 2),
]


class TicRules(unittest.TestCase):
    def test_every_rule_has_a_case(self):
        self.assertEqual({r.id for r in ko_tics.RULES}, {c[0] for c in CASES})

    def test_cases(self):
        for rid, pos, neg, n in CASES:
            hit = {f.rule_id for f in analyze((pos + " ") * n).findings}
            miss = {f.rule_id for f in analyze((neg + " ") * n).findings}
            with self.subTest(rule=rid):
                self.assertIn(rid, hit, f"걸려야 한다: {pos!r}")
                self.assertNotIn(rid, miss, f"걸리면 안 된다: {neg!r}")

    def test_only_the_fixed_spellings_edit_text(self):
        for r in ko_tics.RULES:
            if r.id in ("ko.term.release", "ko.term.harness"):
                self.assertEqual(r.tier, "safe", r.id)
            else:
                self.assertEqual(r.tier, "none", r.id)


if __name__ == "__main__":
    unittest.main()
