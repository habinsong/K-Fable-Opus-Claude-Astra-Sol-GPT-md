# Claude Haiku 5.5 · 앱 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-haiku-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/02-claude/haiku-5.5/app.md`](../../../../md/02-claude/haiku-5.5/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 기본 `medium`, 대량·저지연 보조 작업용, 지식 회상이 약함(36%), 컴퓨터 사용 도구는 `computer_toolset_20260801`.

- **앱 기능 구현의 주력으로 쓰지 않는다.** 수명주기, 권한, 비동기 처리가 걸린 구현은 Sonnet 5.5 이상 문서를 따른다. Terminal-Bench 4.0에서 Sonnet 5.5에 크게 뒤지고 모바일 개발 전용 평가는 찾지 못했다. [부분/미확인]
- **써도 되는 좁은 일.** 문자열 리소스 변환(Android `strings.xml`, iOS `Localizable`), 다국어 번역 초안, 크래시 로그와 빌드 로그의 분류·요약, 스토어 메타데이터 초안, 스키마가 정해진 JSON 생성, 빌드 결과를 읽어 실패 구간을 알려 주는 하위 에이전트. 결과는 파서·린터·빌드로 검증되는 일로 한정한다.
- **스토어 정책과 플랫폼 요건은 기억에서 가져오지 않는다.** 정답 비율 36%(AA-Omniscience)이고 학습 데이터는 오늘보다 훨씬 앞에서 끝난다. [부분] 검색 도구와 오늘 날짜를 주고 "바뀌었을 수 있는 사실은 확신이 있어도 검색하라"를 넣는다. §1.2 표는 작업 시점에 공식 문서로 다시 확인한다. [확인]
- **번역은 사람이 확인한다.** 출시 전에 원어민 검수를 거치고 용어집으로 일관성을 점검한다.
- **컴퓨터 사용 도구를 새 버전으로 옮긴다.** `computer_20250124`는 400이다. `computer_toolset_20260801`을 쓰고 Amazon Bedrock에서만 `computer_20251124`도 된다. 시뮬레이터 조작 결과는 스크린샷·로그로 확인한다. OSWorld 2.1은 Sonnet 5.5(83.9%)보다 낮은 72.4%다. [확인/부분]
- **개인정보·권한 문구는 직접 검토한다.** 권한 사용 목적 문구와 개인정보 처리 설명이 실제 동작과 일치하는지 사람이 확인한다.
- **하위 에이전트의 입력이 길면 비용을 실측한다.** 프롬프트 약 10만 토큰을 넘으면 가격이 오르고 `max`에서는 토큰을 많이 쓴다는 지적이 있다. [부분]
- **서명 키, 프로파일, 스토어 제출·배포는 승인 후에만.**
- **코드베이스를 읽고 설명하는 답을 근거로 쓰지 않는다.** 코드 설명·추적 항목이 상위 모델의 절반 수준이다. 코딩 에이전트 지수는 30으로 낮다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **`max` 대신 `medium`을 쓴다.** `max`는 출력 토큰이 `medium`의 약 6배인데 독립 지수는 11점만 오른다. [확인: Artificial Analysis 모델 페이지]
- **싼 일에는 Sonnet 5.5보다 낫게 나온 시험이 있다.** 비용이 약 3분의 1이다. 어려운 세션은 낮다. [부분: 단일 시험]
- **프롬프트가 10만 토큰을 넘으면 요금이 모든 항목에서 5배가 된다.** 큰 입력은 필요한 구간만 넣는다. [부분: 2차 리뷰]
- **정답이 새어 있는 자료를 쓰고도 알리지 않는 비율이 높다는 보고가 있다.** 시험·평가 환경에서는 정답 파일을 접근 불가로 두고 근거를 밝히게 한다. [부분: 시스템 카드를 옮긴 2차 글]
- **조사·분류·문서 파싱과 하위 에이전트의 탐색 심부름에 쓴다.** 명확하게 지시한 빠른 일에 맞는다는 증언이 여러 건 있다. [부분: HN 다수 증언]

## 4. 근거와 한계
- 검색 지침·컴퓨터 사용 도구: [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5), [What's new in Claude Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5) [확인]
- 정답 비율·비용·OSWorld: [eesel.ai 리뷰](https://www.eesel.ai/blog/claude-haiku-5-5-review), [Beam](https://beam.ai/agentic-insights/claude-haiku-5-5-subagents) [부분]
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: claude-haiku-5-5 모델 페이지](https://artificialanalysis.ai/models/claude-haiku-5-5)
- 추가 확인(2026-11-19 웹 검색): [Bito: Fable 5.2 대 Opus 5.5 비교 시험](https://bito.ai/blog/claude-fable-5-2-vs-opus-5-5-sonnet-haiku/)
- 추가 확인(2026-11-19 웹 검색): [eesel: Claude Haiku 5.5 리뷰](https://www.eesel.ai/blog/claude-haiku-5-5-review)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Claude Haiku 5.5 스레드](https://news.ycombinator.com/item?id=49996437)
- 한계: 모바일 개발에 대한 Haiku 5.5 전용 평가는 없다.
