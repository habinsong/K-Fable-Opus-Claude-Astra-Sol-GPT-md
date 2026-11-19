# Inkling 2 Small · 앱 — 조사 기록
> 제공자: Thinking Machines Lab · 모델 ID: `inkling-2-small`(Cloudflare 표기) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/17-thinking-machines/inkling-2-small/app.md`](../../../../md/17-thinking-machines/inkling-2-small/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
Inkling 2 Small 전용 앱 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 총 5,940억(활성 170억), 컨텍스트 1M 평가, Apache 2.0 가중치(2026-11-12). NVFP4 체크포인트에 GPU 메모리 합계 500GB 이상.
- FrontierCode 2.0 25.4%(DeepSeek-V4.1-Flash 28.5), DeepSWE v1.1 72.1%(77.0), SWE-Atlas 61.9%(62.1), Terminal Bench Science v0.1 5.7%(12.9). 코딩은 DeepSeek V4.1 Flash에 대체로 뒤진다. [부분, 벤더 보고]
- 도구를 항상 최선으로 고르지 않는다(스킬이 많은 코드베이스). 슬래시를 과하게 쓴다. [확인: 블로그의 한계 절]

**앱 작업에서 따로 확인할 것**
- 모바일·데스크톱 빌드·서명 도구와의 호환, 긴 세션의 비용, 화면 입력 이해를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 앱 작업 성능으로 읽지 않는다. [추정]
- **출력 토큰이 많이 든다.** `max_tokens`와 토큰 예산을 넉넉히 잡고 작업당 총비용으로 비교한다. [부분: 2차 보도]
- **출시 시점에 가중치가 비공개였다.** 미공개 코드를 보내기 전에 약관과 데이터 처리 조건을 확인한다. [부분]
- **출력이 길므로 토큰 상한을 둔다.** 출력 토큰이 같은 급 중앙값의 약 1.5배다. 어려운 변경은 상위 모델로 교차한다. [확인: Artificial Analysis 모델 페이지]

## 4. 근거와 한계
- [Thinking Machines: Introducing Inkling 2 Small](https://thinkingmachines.ai/news/inkling-2-small/)
- [Cloudflare Workers AI: inkling-2-small](https://developers.cloudflare.com/workers-ai/models/inkling-2-small/)
- 추가 확인(2026-11-19 웹 검색): [Let's Data Science: Inkling 2 Small](https://letsdatascience.com/blog/inkling-2-small-30-cents-per-million-tokens-weights-still-locked)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: inkling-2-small 모델 페이지](https://artificialanalysis.ai/models/inkling-2-small)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 앱 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
