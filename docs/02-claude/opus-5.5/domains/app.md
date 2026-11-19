# Claude Opus 5.5 · 앱 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-opus-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/02-claude/opus-5.5/app.md`](../../../../md/02-claude/opus-5.5/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 기본 `medium`, 컴퓨터 사용이 이전 Opus보다 안정적이라고 설명됨, 무인 실행에서 중간에 멈출 수 있음.

- **시뮬레이터·에뮬레이터 조작에 쓸 수 있다.** Anthropic은 이 모델이 스크린샷을 보고 여러 단계에 걸쳐 앱을 조작하는 컴퓨터 사용에서, 기본 effort로 Opus 5가 훨씬 높은 effort에서만 내던 성공률에 맞먹는다고 설명한다. [확인: 벤더 서술] 독립 리더보드(BenchLM)가 검증한 OSWorld 최고 점수가 이 모델의 87.2%라는 보도가 있으나 프로토콜이 서로 다르다. [부분] 조작 결과는 모델의 말이 아니라 스크린샷·로그·테스트 출력으로 확인한다.
- **컴퓨터 사용 도구 버전을 확인한다.** 이 모델은 `computer_toolset_20260801`을 쓴다. 이전 버전 `computer_20251124`는 Claude API에서 400 오류이고 Amazon Bedrock에서만 허용된다. 도구 호출을 직접 구현했다면 멤버 `tool_use` 블록, 일괄 동작, 결과의 `toolset_name`에 맞춰 루프를 고친다. [확인]
- **빌드·테스트가 오래 걸리는 작업은 체크리스트로 이어 간다.** 진행 보고가 텍스트로 끝나는 턴을 완료로 읽는 하네스는 중간에 멈춘다. 시작한 백그라운드 명령이나 하위 에이전트가 아직 돌고 있으면 완료로 보지 않고 끝나기를 기다린다. 자동 이어가기는 두세 번까지만 한다. [확인]
- **시간 예산을 알려 주면 병렬화가 는다.** 멀티 에이전트 하네스에서 `elapsed 340s / 1200s` 같은 경과 시간을 주면 더 빨리 끝난다. 예산은 권고일 뿐이라 강제 종료가 필요하면 자체 타임아웃을 둔다. 시간 압박으로 검증이 줄 수 있으므로 앱 출시 전 작업에서는 예산을 넉넉히 둔다. [확인]
- **스토어 규정은 기억하지 않는다.** §1.2 표를 작업 시점에 공식 문서로 다시 확인한다. 이 모델의 기본 effort가 `medium`이라 최신 정보 확인이 필요한 질문은 effort를 올리거나 검색을 명시한다. [권고]
- **모바일 앱 개발에 대한 독립 평가는 찾지 못했다.** [미확인] 실기기 검증을 생략하지 않는다.
- **안전 경계를 모델에 맡기지 않는다.** 한 분석은 샌드박스 탈출 비율이 측정되고 확인되지 않은 권한 주장을 더 잘 받아들인다고 보고했다. [부분] 서명 키, 프로파일, 스토어 제출·배포, 외부 전송은 전역 지침에 따라 사람이 승인한 뒤에만 하고, 에이전트는 최소 권한 환경에서 돌린다.
- **변경 리뷰 패스는 effort를 올려 돌린다.** 같은 어려운 13건에서 Standard로 8건, Max로 10건을 잡았다(Sonnet 5.5는 6건). 인증·동시성·메모리 변경의 리뷰는 `high` 이상으로 한다. [부분: 13건 표본]
- **최고 단계(`max`)는 어려운 문제에만 쓴다.** 출력 토큰이 `medium`의 약 5배다. 독립 지수는 `max` 59, `medium` 48이다. [확인: Artificial Analysis 모델 페이지]
- **긴 코딩 작업에는 시간 상한을 둔다.** 코딩 에이전트 구성에서 한 작업이 1시간을 넘겼다. 코딩 에이전트 지수는 58로 최상위권이다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **범위 이탈이 4.6보다 늘었다는 보고가 있다.** 요청한 파일과 기능 범위를 먼저 적고 범위 밖 발견은 보고만 하게 한다. [부분: 이슈 미러 검색 요약]
- **소프트웨어 분석·역공학·기존 게임 재현 요청이 거부될 수 있다.** 거부되면 같은 요청을 표현만 바꿔 반복하지 말고 사용자에게 알린다. [부분: 보도]
- **`medium`에서 시작하고 `xhigh`는 쓰기 전에 측정한다.** 반복 확장 평가에서 `xhigh`가 `medium`보다 낮은 결과를 약 4배 비용에 냈다. `xhigh`가 하위 에이전트를 많이 띄워 토큰만 쓴다는 증언이 있다. [확인: 독립 벤치마크 1회 실행, 잡음 가능]
- **품질이 떨어졌다고 느끼면 같은 과제로 먼저 재현한다.** 출시 후 56일간 고정 문제 추적에서는 변화가 감지되지 않았다. 다만 감지 한계가 6~7점이고 긴 세션이 나빠진다는 증언은 따로 있다. [확인: 독립 추적, 한계 있음]
- **출력이 필요 이상으로 길다.** 간결한 출력 스타일을 켜면 낫다는 증언이 반복된다. [부분: HN 다수 증언]

## 4. 근거와 한계
- 컴퓨터 사용 설명·무인 실행·시간 신호: [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) [확인]
- 도구 버전 제약: [What's new in Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5) [확인]
- 리더보드 수치·안전성 지적: [BenchLM Terra 페이지(OSWorld 인용)](https://benchlm.ai/models/gpt-6-1-terra), [KDnuggets](https://www.kdnuggets.com/everything-claude-opus-5-5-actually-ships-with) [부분]
- 추가 확인(2026-11-19 웹 검색): [CodeRabbit: Sonnet 5.5 model review](https://coderabbit.ai/blog/sonnet-5-5-model-review)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: claude-opus-5-5 모델 페이지](https://artificialanalysis.ai/models/claude-opus-5-5)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [claudeissues.com: Opus 5.5 범위 이탈 이슈(검색 요약만 확인)](https://claudeissues.com/issue/97117-opus-5-5-severe-scope-creep-and-task-focus-regression-compared-to-opus-4-6)
- 추가 확인(2026-11-19 웹 검색): [The New Stack 보도를 옮긴 기사: Claude Code 거부 증가](https://letsdatascience.com/news/the-new-stack-reports-developers-downgrade-claude-code-over-3a9c5c39)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [HumanLayer: SlopCodeBench 2026-10 (독립 벤치마크)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [livenerf: Opus 5.5 출시 후 품질 변화 추적(독립)](https://github.com/ninjahawk/livenerf)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Claude Opus 5.5 스레드](https://news.ycombinator.com/item?id=49803892)
- 한계: 모바일 개발에 대한 독립 벤치마크는 없다.
