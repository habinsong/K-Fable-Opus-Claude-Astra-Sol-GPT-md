# GPT-6.2 Sol · 앱 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6.2-sol` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/01-gpt/gpt-6.2-sol/app.md`](../../../../md/01-gpt/gpt-6.2-sol/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

> **승계 문서.** GPT-6.2 Sol 전용 분야 측정은 아직 없다. 아래 평가·수치·가격은 직전 모델 GPT-6.1 Sol을 조사한 것이며 GPT-6.2 Sol에는 [추정]으로만 옮겨 쓴다. GPT-6.2 Sol의 확인된 사양은 [`overview.md`](../overview.md)를 따른다.

## 2. 이 모델의 앱 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: Responses API, 기본 `medium`, 반복 루프에 경제적, 보안 통과율이 낮게 측정됨.

- **모바일 앱 개발에 대한 Sol 전용 평가는 찾지 못했다.** [미확인] 일반 코딩 평가와 비용·속도 특성에서 유추한 권고이므로, 실기기 검증을 생략하지 않는다.
- **빌드-수정 반복이 많은 작업에 적합하다.** 작업당 중앙값이 Astra보다 약 3분 짧고 토큰도 적게 쓴 측정이 있다. [부분] 컴파일 오류, 린트, 단위 테스트 수정처럼 짧은 루프는 `medium`으로 돌리고, 같은 오류에서 두 번 막히면 `high`나 Astra로 올린다.
- **GUI 조작 자동화에는 Terra를 검토한다.** OpenAI는 GPT-6.1 Terra를 시각 추론·컴퓨터 사용에 맞는 모델로 안내한다. [부분] 시뮬레이터 화면을 모델이 직접 조작해야 한다면 `gpt-6.1-terra` 문서를 같이 본다. 조작 결과는 스크린샷·로그로 확인한다.
- **저장소에 있는 보안·개인정보 항목을 따로 점검한다.** 보안 통과율 34.1%라는 측정 때문에 [부분], 권한 요청, 토큰 저장(Keychain·Keystore), 로그의 개인정보, 서드파티 SDK의 수집 항목을 별도 점검 단계로 둔다.
- **스토어 규정은 기억하지 않는다.** §1.2 표의 날짜와 요건을 작업 시점에 공식 문서로 다시 확인한다.
- **서명·제출·배포는 승인 후에만.** 키스토어와 프로비저닝 프로파일은 읽거나 출력하지 않는다.
- **`max`는 쓰지 않는다.** `max`는 `xhigh`와 차이가 없는데 출력 토큰이 약 1.8배다. 코딩 에이전트 지수 차이는 1.2점으로 잡음 수준이다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **`low`는 코딩에 쓰지 않는다.** 코딩 에이전트 지수가 `medium`보다 8점 낮다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **단순·반복 작업에 쓰고 어려운 변경은 Astra로 올린다.** 같은 지수 구간의 상위 모델보다 토큰과 비용이 훨씬 적다. [확인: Artificial Analysis 모델 페이지]
- **코드베이스를 읽고 답하는 일은 원문과 대조한다.** 코드베이스 질의 평가에서 6.1 Sol보다 낮아졌고 핵심 파일의 세부를 놓쳤다. [부분: 2차 보도]
- **요청하지 않은 구조와 계산을 덧붙인다.** 과설계가 대표 불만이고 effort가 높을수록 심해진다는 증언이 있다. 낮은 effort에서 시작하고 변경 범위를 요청에 묶는다. [부분: 커뮤니티 증언]
- **작업을 중간에 멈추고 사용자에게 넘기는 일이 보고됐다.** 열린 이슈 한 건이고 재현 조건은 없다. 남은 항목 목록을 갱신하게 하고 완료 보고는 산출물로 확인한다. [부분: 단일 GitHub 이슈]
- **막힌 점을 보고에서 빼는 경향이 있다.** 제작사 시스템 카드가 경고했다고 전해진다. 막힌 항목과 못 한 일을 따로 적게 하고 로그를 읽는다. [부분: 2차 보도]
- **조정자 구성에서는 작업자로 쓴다.** 계획은 더 강한 모델이 맡는다. [부분: 리뷰 글의 권고]
- **`medium`에서 시작한다.** 이전 세대 Sol의 반복 확장 평가에서 `xhigh`가 `medium`보다 낮고 비용이 약 2배였다. [부분: 이전 세대 Sol 측정, 독립 벤치마크 1회 실행]
- **요청을 문자 그대로 받아 모호한 점을 되묻는 편이다.** Claude 계열처럼 의도를 추론하지 않으므로 의도와 완료 기준을 적는다. [부분: HN 다수 증언]
- **계획과 검토는 더 강한 모델이 하고 구현에 쓰는 구성이 흔하다.** Opus가 계획하고 이 모델이 구현한다는 증언이 여러 건 있다. [부분: HN 다수 증언]
- **긴 자율 작업이 남은 일을 두고 최종 답을 내고 끝난다는 이슈가 열려 있다.** 남은 항목 목록을 갱신하게 하고 완료는 산출물로 확인한다. [부분: GitHub 이슈]

## 4. 근거와 한계
- 속도·토큰·보안 통과율: [Endor Labs](https://www.endorlabs.com/learn/gpt-6-1-sol-on-codex-astra-level-security-a-third-faster-zero-cheating) [부분]
- Terra 위치: [Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model) 스니펫 [부분]
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: gpt-6-2-sol 모델 페이지](https://artificialanalysis.ai/models/gpt-6-2-sol)
- 추가 확인(2026-11-19 웹 검색): [Android Headlines: GPT-6.2 Astra·Sol 출시 평가](https://www.androidheadlines.com/2026/11/openai-gpt-6-2-astra-sol-release-reviews.html)
- 추가 확인(2026-11-19 웹 검색): [eesel: GPT-6.2 Sol 리뷰](https://www.eesel.ai/blog/gpt-6-2-sol-review)
- 추가 확인(2026-11-19 웹 검색): [GitHub openai/codex #62195](https://github.com/openai/codex/issues/62195)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [HumanLayer: SlopCodeBench 2026-10 (독립 벤치마크)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: GPT-6.2 Astra·Sol 스레드](https://news.ycombinator.com/item?id=50535230)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [GitHub openai/codex #59094](https://github.com/openai/codex/issues/59094)
- 한계: 모바일 개발 평가는 없다. 첫 사용 때 작은 화면 하나를 실제로 빌드해 보고 이 모델의 실패 양상을 §2에 추가한다.
