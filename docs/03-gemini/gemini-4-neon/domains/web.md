# Gemini 4 Neon · 웹 — 조사 기록
> 제공자: Google · 모델 ID: 미공개 [미확인] (코드에서 `gemini-4-neon` 문자열이 관찰됨) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/03-gemini/gemini-4-neon/web.md`](../../../../md/03-gemini/gemini-4-neon/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용 (잠정)
2026-11-19 기준 Gemini 4 Neon은 공식 발표가 없고 모델 ID·사양이 확인되지 않았다.
모델 상태와 공개 시 확인 체크리스트는 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 공개 전에는 `03-gemini/gemini-4-carbon/web.md`(Gemini 4 Carbon)의 규칙을 잠정 기준선으로 삼는다. [추정]

**공개 뒤 웹 작업에서 따로 확인할 것**
- 함수 호출 하네스 요건, 프런트엔드 과제의 자기 검증 능력, 반복 작업 단가를 같은 과제로 Gemini 4 Carbon와 비교한다.
- 모델 ID, 가격, 컨텍스트, `thinking_level` 범위가 공식 모델 페이지에서 확인되기 전에는 이 문서의 어떤 문장도 성능이나 동작을 단정하지 않는다.
- **단계 수에 상한을 둔다.** 한 작업에 177단계를 쓰고 입력 토큰이 크다. 코딩 에이전트 지수는 58.6으로 최상위권이다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **낮은 effort 결과를 일반화하지 않는다.** `xhigh` 한 가지 구성만 측정됐다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **점수의 상당 부분이 Antigravity 하네스에서 나온다.** 다른 하네스에서는 결과가 크게 낮을 수 있으므로 쓰는 하네스로 직접 시험한다. [부분: 보도]
- **설계는 더 강한 모델이 하고 구현 위임에 쓴다.** 초기 사용자 평에서 Carbon보다 품질은 낮지만 훨씬 빠르고 비용이 약 절반이다. [부분: HN 초기 후기 2건]

## 4. 근거와 한계
- 상태와 출처: 같은 폴더의 [`sources.md`](../sources.md) 참조. 공식 발표를 찾지 못했다. [미확인]
- 관찰 출처(2차 전언): [https://www.testingcatalog.com/google-prepares-to-release-gemini-4-neon-model-on-apis/](https://www.testingcatalog.com/google-prepares-to-release-gemini-4-neon-model-on-apis/) [부분]
- 잠정 규칙: 같은 저장소의 `03-gemini/gemini-4-carbon/web.md`.
- 추가 확인(2026-11-19 웹 검색): [Orcarouter: Gemini 4 Neon과 Coding Agent Index](https://www.orcarouter.ai/blog/gemini-4-neon-coding-agent-index)
- 추가 확인(2026-11-19 웹 검색): [The New Stack: Gemini 4 Neon과 Antigravity 하네스](https://thenewstack.io/gemini-neon-antigravity-harness/)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Gemini 4 Neon 스레드](https://news.ycombinator.com/item?id=50552424)
- 한계: Gemini 4 Neon의 웹 작업 성능에 대한 정보는 없다. 이 문서는 확인 항목 목록이며 모델 특성이 아니다.
