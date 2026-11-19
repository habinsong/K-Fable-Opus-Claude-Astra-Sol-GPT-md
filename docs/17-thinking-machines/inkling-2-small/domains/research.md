# Inkling 2 Small · 연구 — 조사 기록
> 제공자: Thinking Machines Lab · 모델 ID: `inkling-2-small`(Cloudflare 표기) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/17-thinking-machines/inkling-2-small/research.md`](../../../../md/17-thinking-machines/inkling-2-small/research.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/research.md`](../../../_common/domain-rules/research.md)

## 2. 이 모델의 연구 작업 운용
Inkling 2 Small 전용 연구 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- HLE-Diamond 28.7%, HLE(텍스트) 44.1%, ARC-AGI-2 81.7%(블로그 표기), BrowseComp 90.2%(압축 사용), AA-LCR v1.1 83.3%, LongBench v2 70.6%. [부분, 벤더 보고]
- AA-Omniscience 점수 16.1, 비환각률 73.3%. 약 4건 중 1건은 지어낼 수 있다는 뜻이다(계산). [부분]
- 금융 지표(Vals Finance Index 61.5%, Finance Agent v2.1 67.5%, Vals Legal Index 73.9%)가 강점이라고 한다. [부분, 벤더 보고]

**연구 작업에서 따로 확인할 것**
- 논문 인용의 실재 여부, 통계 수치 처리, 가설과 사실의 구분를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 연구 작업 성능으로 읽지 않는다. [추정]
- **출력 토큰이 많이 든다.** `max_tokens`와 토큰 예산을 넉넉히 잡고 작업당 총비용으로 비교한다. [부분: 2차 보도]
- **사실과 인용은 원문으로 대조한다.** 사실 질문의 환각률이 이전보다 낮아졌다는 측정이 있으나 제작사 쪽 수치다. [부분]
- **사실 질문에서 모르면 기권하는 편이다.** 기권을 오류로 취급하지 말고, 그래도 인용과 수치는 원문으로 확인한다. 사실 질문 기준 오답 비율이 26.7%다. [부분: 독립 측정을 옮긴 집계 페이지]

## 4. 근거와 한계
- [Thinking Machines: Introducing Inkling 2 Small](https://thinkingmachines.ai/news/inkling-2-small/)
- [Cloudflare Workers AI: inkling-2-small](https://developers.cloudflare.com/workers-ai/models/inkling-2-small/)
- 추가 확인(2026-11-19 웹 검색): [Let's Data Science: Inkling 2 Small](https://letsdatascience.com/blog/inkling-2-small-30-cents-per-million-tokens-weights-still-locked)
- 추가 확인(2026-11-19 웹 검색): [OfficeChai: Inkling 2 Small](https://officechai.com/ai/thinking-machines-releases-inkling-2-small-to-become-top-scoring-non-chinese-model-on-artificial-analysis-intelligence-index-once-weights-release/)
- 추가 확인(2026-11-19 웹 검색): [BenchLM: AA-Omniscience 환각률(2026-11-19, Artificial Analysis 수치를 옮긴 미러)](https://benchlm.ai/benchmarks/omnisciencehallucinationrate)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 연구 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
