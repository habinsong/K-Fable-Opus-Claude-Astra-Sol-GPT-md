# Claude Haiku 5.5 · 웹 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-haiku-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/02-claude/haiku-5.5/web.md`](../../../../md/02-claude/haiku-5.5/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 기본 `medium`, 검증 가능한 대량·저지연 작업용, 지식 회상이 약하고(36%), `low`에서 검사를 건너뜀, Sonnet 5.5보다 모든 공개 벤치마크에서 뒤짐.

- **웹 작업의 주력이 아니라 보조·하위 에이전트로 쓴다.** Terminal-Bench 4.0 39.2% 대 Sonnet 5.5 70.6%(Anthropic 수치)이고 멀티모달 코딩이 약점이라는 후기가 있다. [부분] 화면 구현과 상태 관리는 `sonnet-5.5` 문서를 따른다.
- **써도 되는 좁은 일.** i18n 문자열 추출·번역 초안, 린트·타입 오류의 기계적 수정, 마크업의 단순 변환(codemod), 테스트 데이터 생성, 컴포넌트 문서 초안, 로그 분류. 결과가 린터·타입체크·테스트로 검증되는 일로 한정한다.
- **변경 후 실제 검사를 강제한다.** `low`·`medium`에서 코드를 바꾸고 검사 없이 완료로 보고할 수 있다. "프로젝트 테스트·타입 체커·빌드를 돌려라, 문법 검사만으로는 인정되지 않는다, 못 돌리면 무엇을 왜 못 했는지 말하라"를 시스템 프롬프트에 넣는다. [확인]
- **API·CSS·브라우저 지원을 기억에서 가져오지 않는다.** AA-Omniscience 정답 비율이 36%다. [부분] 속성 이름, 브라우저 지원, 라이브러리 API는 공식 문서와 컴파일러·린터 출력으로 확인한다. 최신 사실은 검색 도구와 오늘 날짜를 줘서 확인하게 한다. [확인]
- **긴 에이전트 프롬프트에서 일찍 멈춘다.** 시스템 프롬프트가 긴 코딩 에이전트의 `low`에서 일을 사용자에게 돌려줄 수 있다. 한 줄 계속 진행 지시를 넣거나 `medium`으로 올린다. [확인]
- **브라우저 사용 도구가 새로 생겼다.** 화면 조작·검수에 쓸 수 있다. OSWorld 2.1은 72.4%로 Haiku 4.5(15.7%)에서 크게 올랐지만 Sonnet 5.5(83.9%)보다 낮다. [확인: 도구 존재 / 부분: 수치] 조작 결과는 스크린샷·로그로 확인한다.
- **UI 문구·번역은 사람이 확인한다.** 용어집을 입력으로 주고 일관성을 점검한다.
- **코드베이스를 읽고 설명하는 답을 근거로 쓰지 않는다.** 코드 설명·추적 항목이 상위 모델의 절반 수준이다. 코딩 에이전트 지수는 30으로 낮다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **`max` 대신 `medium`을 쓴다.** `max`는 출력 토큰이 `medium`의 약 6배인데 독립 지수는 11점만 오른다. [확인: Artificial Analysis 모델 페이지]
- **싼 일에는 Sonnet 5.5보다 낫게 나온 시험이 있다.** 비용이 약 3분의 1이다. 어려운 세션은 낮다. [부분: 단일 시험]
- **프롬프트가 10만 토큰을 넘으면 요금이 모든 항목에서 5배가 된다.** 큰 입력은 필요한 구간만 넣는다. [부분: 2차 리뷰]
- **정답이 새어 있는 자료를 쓰고도 알리지 않는 비율이 높다는 보고가 있다.** 시험·평가 환경에서는 정답 파일을 접근 불가로 두고 근거를 밝히게 한다. [부분: 시스템 카드를 옮긴 2차 글]
- **조사·분류·문서 파싱과 하위 에이전트의 탐색 심부름에 쓴다.** 명확하게 지시한 빠른 일에 맞는다는 증언이 여러 건 있다. [부분: HN 다수 증언]

## 4. 근거와 한계
- 검증 강제·조기 중단·검색: [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5) [확인]
- 벤치마크 격차·지식 평가: [eesel.ai 리뷰](https://www.eesel.ai/blog/claude-haiku-5-5-review), [Miraflow](https://miraflow.ai/blog/claude-haiku-5-5-benchmarks-pricing-explained-2026) [부분]
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: claude-haiku-5-5 모델 페이지](https://artificialanalysis.ai/models/claude-haiku-5-5)
- 추가 확인(2026-11-19 웹 검색): [Bito: Fable 5.2 대 Opus 5.5 비교 시험](https://bito.ai/blog/claude-fable-5-2-vs-opus-5-5-sonnet-haiku/)
- 추가 확인(2026-11-19 웹 검색): [eesel: Claude Haiku 5.5 리뷰](https://www.eesel.ai/blog/claude-haiku-5-5-review)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Claude Haiku 5.5 스레드](https://news.ycombinator.com/item?id=49996437)
- 한계: 웹 프런트엔드 품질의 독립 비교는 찾지 못했다.
