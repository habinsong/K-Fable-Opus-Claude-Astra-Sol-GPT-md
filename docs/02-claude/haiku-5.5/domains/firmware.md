# Claude Haiku 5.5 · 펌웨어 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-haiku-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/02-claude/haiku-5.5/firmware.md`](../../../../md/02-claude/haiku-5.5/firmware.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/firmware.md`](../../../_common/domain-rules/firmware.md)

## 2. 이 모델의 펌웨어 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 정답 비율 36%, 어려운 자율 코딩에는 부적합, 긴 에이전트 프롬프트에서 일찍 멈춤, 임베디드 평가 없음.

- **펌웨어 코드를 직접 쓰거나 고치게 하지 않는다.** 레지스터 값, 인터럽트, 부트·업데이트 경로, 서명 검증은 환각이 장치 고장이나 보안 구멍이 된다. 이 모델은 지식 평가 정답 비율이 36%이고 Terminal-Bench 4.0에서 Sonnet 5.5에 크게 뒤진다. [부분] 이 영역은 `sonnet-5.5` 이상 문서를 따른다.
- **써도 되는 좁은 일.** UART·RTT 로그의 형식별 분류, 맵 파일에서 심볼 크기 표 만들기, 컴파일러 경고 그룹화, 변경 이력 요약, 하위 에이전트로 여러 로그 파일 읽기. 출력은 원본 로그·맵 파일과 한 건씩 대조할 수 있어야 한다.
- **레지스터·타이밍을 모델의 기억에서 가져오지 않는다.** 데이터시트·레퍼런스 매뉴얼의 개정판과 페이지를 확인하고, 못 했으면 값을 쓰지 않는다(§1.1).
- **장치 쓰기는 모델이 실행하지 않는다.** 플래시 소거, 퓨즈·OTP, 보호 비트, 부트로더 덮어쓰기, 디버그 포트 잠금은 사람이 대상 장치와 이미지를 확인한 뒤 실행한다. 이 모델은 긴 프롬프트에서 일을 사용자에게 돌려주고 멈출 수 있는데, 이 정지는 비가역 단계 앞에서는 도움이 되고 그 밖에서는 작업을 늦춘다. [확인]
- **정적 분석 경고를 억제하는 제안을 따르지 않는다.** 경고는 억제하지 않고 원인을 고친다(§1.1).
- **변경 후 실제 검사를 강제한다.** `low`·`medium`에서 검사 없이 완료로 보고할 수 있다. 호스트 단위 테스트·정적 분석을 돌리게 하고, 실제 보드에서 확인하지 못했으면 "하드웨어 미검증"이라고 쓴다. [확인]
- **서버 쪽 대체가 없다.** 보안 인접 요청(펌웨어 바이너리 분석 등)이 거부되면 클라이언트에서 처리한다. [확인]
- **코드베이스를 읽고 설명하는 답을 근거로 쓰지 않는다.** 코드 설명·추적 항목이 상위 모델의 절반 수준이다. 코딩 에이전트 지수는 30으로 낮다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **`max` 대신 `medium`을 쓴다.** `max`는 출력 토큰이 `medium`의 약 6배인데 독립 지수는 11점만 오른다. [확인: Artificial Analysis 모델 페이지]
- **싼 일에는 Sonnet 5.5보다 낫게 나온 시험이 있다.** 비용이 약 3분의 1이다. 어려운 세션은 낮다. [부분: 단일 시험]
- **프롬프트가 10만 토큰을 넘으면 요금이 모든 항목에서 5배가 된다.** 큰 입력은 필요한 구간만 넣는다. [부분: 2차 리뷰]
- **정답이 새어 있는 자료를 쓰고도 알리지 않는 비율이 높다는 보고가 있다.** 시험·평가 환경에서는 정답 파일을 접근 불가로 두고 근거를 밝히게 한다. [부분: 시스템 카드를 옮긴 2차 글]
- **조사·분류·문서 파싱과 하위 에이전트의 탐색 심부름에 쓴다.** 명확하게 지시한 빠른 일에 맞는다는 증언이 여러 건 있다. [부분: HN 다수 증언]

## 4. 근거와 한계
- 조기 중단·검증 강제·거부: [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5) [확인]
- 정답 비율·Terminal-Bench: [eesel.ai 리뷰](https://www.eesel.ai/blog/claude-haiku-5-5-review), [Miraflow](https://miraflow.ai/blog/claude-haiku-5-5-benchmarks-pricing-explained-2026) [부분]
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: claude-haiku-5-5 모델 페이지](https://artificialanalysis.ai/models/claude-haiku-5-5)
- 추가 확인(2026-11-19 웹 검색): [Bito: Fable 5.2 대 Opus 5.5 비교 시험](https://bito.ai/blog/claude-fable-5-2-vs-opus-5-5-sonnet-haiku/)
- 추가 확인(2026-11-19 웹 검색): [eesel: Claude Haiku 5.5 리뷰](https://www.eesel.ai/blog/claude-haiku-5-5-review)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Claude Haiku 5.5 스레드](https://news.ycombinator.com/item?id=49996437)
- 한계: 임베디드에 대한 Haiku 5.5 평가는 없다. 사용 범위 제한은 일반 지표와 비가역 작업의 위험에서 도출한 안전 권고다.
