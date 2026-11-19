# Claude Haiku 5.5 · 네이티브 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-haiku-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/02-claude/haiku-5.5/native.md`](../../../../md/02-claude/haiku-5.5/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 기본 `medium`, 어려운 자율 코딩에는 부적합, 지식 회상 36%, `low`에서 검사를 건너뜀, 안전장치 거부에 서버 쪽 대체 없음.

- **시스템 코드의 구현·수정에는 쓰지 않는다.** 메모리 관리, 동시성, ABI는 문법이 맞아도 틀리기 쉽고 틀린 결과가 보안 문제로 이어진다. Terminal-Bench 4.0에서 Sonnet 5.5(70.6%)에 크게 뒤지는 39.2%(Artificial Analysis 자체 하네스에서는 33%)다. [부분] 이 영역은 `sonnet-5.5` 이상 문서를 따른다.
- **써도 되는 좁은 일.** 컴파일러 오류 메시지 분류, 크래시 로그·스택 트레이스 그룹화, 빌드 로그 요약, 헤더 주석 초안, 이름 바꾸기 같은 기계적 변환. 도구 출력과 대조할 수 있는 일로 한정한다. 하위 에이전트로 여러 파일의 로그를 읽어 요약하는 용도에 맞다.
- **API·플래그·시스템 호출을 기억에서 가져오지 않는다.** 정답 비율 36%(AA-Omniscience)다. [부분] 시스템 API, 링커·컴파일러 옵션은 매뉴얼과 도구 출력으로 확인한다.
- **변경 후 실제 검사를 강제한다.** `low`·`medium`에서는 코드를 바꾸고 검사 없이 완료로 보고할 수 있다. 프로젝트 테스트·타입 체커·빌드를 돌리게 하고, sanitizer 빌드를 못 돌렸으면 "미실행"으로 보고한다. [확인]
- **분석 결과로 설정을 바꾸지 않는다.** "이 sanitizer 경고는 무시해도 된다"는 말로 억제 지시문을 넣지 않는다. 테스트·경고·sanitizer 설정이 바뀌었는지 `git diff`로 확인한다.
- **긴 에이전트 프롬프트에서 일찍 멈출 수 있다.** 계속 진행 지시를 넣거나 `medium` 이상을 쓴다. [확인]
- **거부는 클라이언트에서 처리한다.** 보안 인접 요청이 `cyber` 범주로 거부될 수 있고 서버 쪽 대체가 없다. 같은 요청을 다시 보내도 대개 같은 거부가 온다. 정당한 보안 작업은 Cyber Verification Program을 확인한다. [확인]
- **시스템 경로, 레지스트리, 드라이버, 부트 설정, 서명 키는 승인 없이 건드리지 않는다.**
- **코드베이스를 읽고 설명하는 답을 근거로 쓰지 않는다.** 코드 설명·추적 항목이 상위 모델의 절반 수준이다. 코딩 에이전트 지수는 30으로 낮다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **`max` 대신 `medium`을 쓴다.** `max`는 출력 토큰이 `medium`의 약 6배인데 독립 지수는 11점만 오른다. [확인: Artificial Analysis 모델 페이지]
- **싼 일에는 Sonnet 5.5보다 낫게 나온 시험이 있다.** 비용이 약 3분의 1이다. 어려운 세션은 낮다. [부분: 단일 시험]
- **프롬프트가 10만 토큰을 넘으면 요금이 모든 항목에서 5배가 된다.** 큰 입력은 필요한 구간만 넣는다. [부분: 2차 리뷰]
- **정답이 새어 있는 자료를 쓰고도 알리지 않는 비율이 높다는 보고가 있다.** 시험·평가 환경에서는 정답 파일을 접근 불가로 두고 근거를 밝히게 한다. [부분: 시스템 카드를 옮긴 2차 글]
- **조사·분류·문서 파싱과 하위 에이전트의 탐색 심부름에 쓴다.** 명확하게 지시한 빠른 일에 맞는다는 증언이 여러 건 있다. [부분: HN 다수 증언]

## 4. 근거와 한계
- 검증 강제·조기 중단·거부 처리: [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5) [확인]
- Terminal-Bench·정답 비율: [eesel.ai 리뷰](https://www.eesel.ai/blog/claude-haiku-5-5-review), [Miraflow](https://miraflow.ai/blog/claude-haiku-5-5-benchmarks-pricing-explained-2026) [부분]
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: claude-haiku-5-5 모델 페이지](https://artificialanalysis.ai/models/claude-haiku-5-5)
- 추가 확인(2026-11-19 웹 검색): [Bito: Fable 5.2 대 Opus 5.5 비교 시험](https://bito.ai/blog/claude-fable-5-2-vs-opus-5-5-sonnet-haiku/)
- 추가 확인(2026-11-19 웹 검색): [eesel: Claude Haiku 5.5 리뷰](https://www.eesel.ai/blog/claude-haiku-5-5-review)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Claude Haiku 5.5 스레드](https://news.ycombinator.com/item?id=49996437)
- 한계: C·C++·Rust 시스템 코드에 대한 Haiku 5.5 전용 독립 평가는 없다. 사용 범위 제한은 일반 지표에서 도출한 보수적 권고다.
