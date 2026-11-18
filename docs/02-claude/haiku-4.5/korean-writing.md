# Claude Haiku 4.5 · 한국어 윤문 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-haiku-4-5-20251001` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`ko-academic`](../../../md/02-claude/haiku-4.5/ko-academic.md) · [`ko-everyday`](../../../md/02-claude/haiku-4.5/ko-everyday.md) · [`ko-literary`](../../../md/02-claude/haiku-4.5/ko-literary.md)
> 공통 조사(AI 말투 도구, 실측, 한국어 원리): [`docs/_common/korean-writing/`](../../_common/korean-writing/README.md)
> 이 모델의 일반 조사 기록: [`README.md`](README.md)

> **승계 문서.** Claude Haiku 4.5 전용 한국어 문체 측정은 아직 없다. 아래 평가·수치·가격은 같은 계열의 후속 모델 Claude Haiku 5.5을 조사한 것이며 Claude Haiku 4.5에는 [추정]으로만 옮겨 쓴다. Claude Haiku 4.5의 확인된 사양은 [`overview.md`](overview.md)를 따른다.

## 1. 이 모델에서 확인한 것 (글쓰기 제어 관점)
- 입력 $1 / 출력 $5, 컨텍스트 200K, 지식 컷오프 2025-02(Anthropic 신뢰 기준), 수동 확장 추론, effort 미지원 [확인].
- Haiku 4.5의 한국어 문체에 대한 독립 평가는 찾지 못했다. 지수 7(92개 중 91위)로 점수가 매우 낮아 긴 한국어 윤문의 품질을 가정하지 않는다 [확인: 읽은 지수 / 미확인: 한국어 품질].

## 2. 한국어 문체에 대해 알려진 것과 모르는 것
- Haiku 5.5 한국어 문체의 독립 평가를 찾지 못했다 [미확인].
- 이 문서가 모델 간 한국어 문체의 우열을 말하지 않는 이유: 사람이 평가한 독립 자료가 없고, 공개된 실측(`empirical-validation.md`)은 다른 모델 버전으로 한 것이다.

## 3. 모델 지침(md)의 근거

`md/02-claude/haiku-4.5/ko-*.md`의 '이 모델에서 지킬 점 (한국어 윤문)' 각 줄이 왜 그렇게 쓰였는지다. 순서가 같다.

1. 지침: 생각 과정이나 메모를 결과물에 섞지 않는다. 결과물에는 윤문한 글만 둔다. 진단 메모는 결과물 밖에 따로 쓴다.
   - 근거: 가이드 *Keep reasoning out of user-facing text* [확인]. 윤문에서는 진단 메모를 결과물 밖으로 분리하는 것으로 옮겼다 [추정].
2. 지침: 숫자, 고유명사, 인용, 약어, 날짜는 원문 그대로 둔다.
   - 근거: 윤문의 보존 원칙이다. 사실, 수치, 고유명사를 바꾸는 실패를 막는다. 공개 윤문 도구들도 같은 보존 규칙을 둔다(`ai-tell-projects.md` §3).
3. 지침: 결과물의 말투(존대, 평어)는 원문의 것을 끝까지 유지하고 중간에 바꾸지 않는다.
   - 근거: 경어법 일관성을 AI 문체 특징으로 보는 도구가 있고(humanizer-ko, im-not-ai E-7), 필자의 격식을 바꾸지 않는 것이 윤문의 기본 원칙이다.
4. 지침: 요청한 범위의 문장만 고친다.
   - 근거: Sonnet 5.5 가이드 *Steer initiative and scope*가 요청하지 않은 추가를 하는 경향과 이를 막는 문구를 제공한다 [확인]. 윤문에 맞게 '요청한 범위만'으로 옮겼다 [추정].

## 4. 근거와 한계
- [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5) [확인]
- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) [확인]
- 이 모델 문서의 사양·가격은 같은 폴더의 [`README.md`](README.md)가 안내하는 문서와 [`sources.md`](sources.md)를 따른다.
- 한계: 지침을 적용한 실제 출력을 사람이 읽고 평가한 적이 없다. 위 근거는 대부분 공식 가이드의 영어 기준 서술이거나 검색 요약이다.
