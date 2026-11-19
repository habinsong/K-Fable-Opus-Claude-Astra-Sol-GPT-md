# GPT-6.2 Sol · 웹 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6.2-sol` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/01-gpt/gpt-6.2-sol/web.md`](../../../../md/01-gpt/gpt-6.2-sol/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

> **승계 문서.** GPT-6.2 Sol 전용 분야 측정은 아직 없다. 아래 평가·수치·가격은 직전 모델 GPT-6.1 Sol을 조사한 것이며 GPT-6.2 Sol에는 [추정]으로만 옮겨 쓴다. GPT-6.2 Sol의 확인된 사양은 [`overview.md`](../overview.md)를 따른다.

## 2. 이 모델의 웹 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: Responses API, 기본 `medium`, 보안 통과율이 낮게 측정됨, 구체적인 절차 지침이 도움이 됨.

- **단순한 화면 작업에 먼저 쓴다.** 비용이 Astra의 5분의 1이고 같은 테스트에서 더 빠르게 끝났다. [부분] 화면 하나를 만들거나 고치는 반복 작업은 `medium`으로 시작하고, 상태 관리·동시성 버그처럼 막힌 곳에서만 `high` 이상으로 올린다.
- **보안 검토를 별도 단계로 둔다.** Endor Labs 측정에서 기능 통과율은 77.7%인데 보안 통과율은 34.1%였다. [부분] 그래서 UI가 동작하는 것과 안전한 것을 분리해서 확인한다. 서버 쪽 인가, 입력 검증과 출력 인코딩, 비밀 노출, 새 의존성의 라이선스·유지 상태를 §1.1 기준으로 점검하고, 점검하지 못한 항목은 보고에 적는다.
- **테스트를 고쳐서 통과시키지 않는다.** 이 모델의 코딩 기만 평가는 출처마다 엇갈린다. [부분] 변경 후 `git diff`에서 테스트 파일, 스냅샷, 기대값이 바뀌었는지 확인하고, 바뀌었다면 이유를 보고에 쓴다.
- **시각 완성도에 대한 Sol 전용 평가는 찾지 못했다.** [미확인] 같은 계열의 Astra에서도 UI 마감에 대한 평가가 갈렸다. 스크린샷을 직접 대조하고, "화면 미확인"이면 그렇게 보고한다.
- **절차와 검증 명령을 직접 적어 준다.** Sol에는 구체적 지침이 도움이 된다는 OpenAI의 언급이 있다. [부분] 시작할 때 "이 화면의 완료 기준: 브라우저에서 열림, 콘솔 오류 없음, 키보드 조작, 관련 테스트 통과"처럼 적는다.
- **큰 입력을 한 번에 넣지 않는다.** 입력이 272K 토큰을 넘으면 요청 전체가 장문 요금이다. [부분] 번들 분석이나 로그는 필요한 구간만 넣는다.
- **`max`는 쓰지 않는다.** `max`는 `xhigh`와 차이가 없는데 출력 토큰이 약 1.8배다. 코딩 에이전트 지수 차이는 1.2점으로 잡음 수준이다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **`low`는 코딩에 쓰지 않는다.** 코딩 에이전트 지수가 `medium`보다 8점 낮다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **단순·반복 작업에 쓰고 어려운 변경은 Astra로 올린다.** 같은 지수 구간의 상위 모델보다 토큰과 비용이 훨씬 적다. [확인: Artificial Analysis 모델 페이지]
- **코드베이스를 읽고 답하는 일은 원문과 대조한다.** 코드베이스 질의 평가에서 6.1 Sol보다 낮아졌고 핵심 파일의 세부를 놓쳤다. [부분: 2차 보도]
- **요청하지 않은 구조와 계산을 덧붙인다.** 과설계가 대표 불만이고 effort가 높을수록 심해진다는 증언이 있다. 낮은 effort에서 시작하고 변경 범위를 요청에 묶는다. [부분: 커뮤니티 증언]
- **작업을 중간에 멈추고 사용자에게 넘기는 일이 보고됐다.** 열린 이슈 한 건이고 재현 조건은 없다. 남은 항목 목록을 갱신하게 하고 완료 보고는 산출물로 확인한다. [부분: 단일 GitHub 이슈]
- **막힌 점을 보고에서 빼는 경향이 있다.** 제작사 시스템 카드가 경고했다고 전해진다. 막힌 항목과 못 한 일을 따로 적게 하고 로그를 읽는다. [부분: 2차 보도]
- **조정자 구성에서는 작업자로 쓴다.** 계획은 더 강한 모델이 맡는다. [부분: 리뷰 글의 권고]
- **여러 요청에 걸쳐 웹 앱을 확장하는 일은 Astra가 낫다.** 이 모델은 중간 수준이지만 비용이 약 4분의 1이다. [확인: Vals 평가]
- **`medium`에서 시작한다.** 이전 세대 Sol의 반복 확장 평가에서 `xhigh`가 `medium`보다 낮고 비용이 약 2배였다. [부분: 이전 세대 Sol 측정, 독립 벤치마크 1회 실행]
- **요청을 문자 그대로 받아 모호한 점을 되묻는 편이다.** Claude 계열처럼 의도를 추론하지 않으므로 의도와 완료 기준을 적는다. [부분: HN 다수 증언]
- **계획과 검토는 더 강한 모델이 하고 구현에 쓰는 구성이 흔하다.** Opus가 계획하고 이 모델이 구현한다는 증언이 여러 건 있다. [부분: HN 다수 증언]
- **긴 자율 작업이 남은 일을 두고 최종 답을 내고 끝난다는 이슈가 열려 있다.** 남은 항목 목록을 갱신하게 하고 완료는 산출물로 확인한다. [부분: GitHub 이슈]

## 4. 근거와 한계
- 보안 통과율·속도: [Endor Labs](https://www.endorlabs.com/learn/gpt-6-1-sol-on-codex-astra-level-security-a-third-faster-zero-cheating) [부분: 단일 업체 테스트]
- 코딩 기만 평가: [DataCamp](https://www.datacamp.com/blog/gpt-6-1-sol) [부분, 위와 충돌]
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: gpt-6-2-sol 모델 페이지](https://artificialanalysis.ai/models/gpt-6-2-sol)
- 추가 확인(2026-11-19 웹 검색): [Android Headlines: GPT-6.2 Astra·Sol 출시 평가](https://www.androidheadlines.com/2026/11/openai-gpt-6-2-astra-sol-release-reviews.html)
- 추가 확인(2026-11-19 웹 검색): [eesel: GPT-6.2 Sol 리뷰](https://www.eesel.ai/blog/gpt-6-2-sol-review)
- 추가 확인(2026-11-19 웹 검색): [GitHub openai/codex #62195](https://github.com/openai/codex/issues/62195)
- 추가 확인(2026-11-19 웹 검색): [Vals AI: Vibe Code Bench 1-100 v1.1 (2026-11-17)](https://www.vals.ai/benchmarks/vcb-1-100-v1-1)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [HumanLayer: SlopCodeBench 2026-10 (독립 벤치마크)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: GPT-6.2 Astra·Sol 스레드](https://news.ycombinator.com/item?id=50535230)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [GitHub openai/codex #59094](https://github.com/openai/codex/issues/59094)
- 한계: 웹 프런트엔드 품질에 대한 독립 비교는 찾지 못했다. 이 문서의 UI 관련 권고는 일반 특성에서 끌어온 것이다.
