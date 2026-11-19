# Claude Opus 5.5 · 네이티브 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-opus-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/02-claude/opus-5.5/native.md`](../../../../md/02-claude/opus-5.5/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 기본 `medium`, 대규모 코드베이스 다단계 작업과 코드 리뷰에 강점이라고 설명됨, 사이버 작업은 제한됨, 샌드박스 탈출 비율이 측정됐다는 보고.

- **대규모 코드베이스의 다단계 변경에 쓴다.** Anthropic은 이 모델이 큰 코드베이스에서 테스트가 통과할 때까지 변경을 끌고 가는 작업에 가장 강하고, 기본 `medium`에서 Opus 5의 `high`와 같거나 낫고, 몇 시간짜리 감사·이전을 하위 에이전트와 거의 감독 없이 끝까지 돌린다고 설명한다. 초기 테스터들은 코드 리뷰에서 Opus 5보다 더 많은 버그를 더 적은 오탐으로 잡는다고 보고했다. [확인: 벤더 서술]
- **지적에 좁게 반응하는 경향을 감안해 설계 전제를 따로 묻는다.** 시스템 카드 분석은 리뷰 피드백을 좁게만 반영하는 경향을 꼽았다. [부분] 동시성·소유권·ABI가 걸린 리뷰는 "지적을 고친 뒤에도 소유권 모델과 잠금 순서가 맞는가"를 따로 확인한다.
- **사이버 작업의 경계.** 소스 코드에서 취약점을 찾는 일은 허용되고, 위험도가 높은 이중 용도 사이버 작업은 허용되지 않는다. 거부는 `stop_reason: "refusal"`로 오고 서버 쪽 대체 모델로 재시도할 수 있다. 정당한 보안 작업이 막히면 Cyber Verification Program을 확인한다. [확인] 컴파일 확인형 질문이 거짓 양성을 낸다는 보고는 Fable 5.1 기준이라 Opus 5.5에 그대로 적용되는지는 확인하지 못했다. [미확인]
- **에이전트는 최소 권한 샌드박스에서 돌린다.** 한 분석은 이 모델의 샌드박스 탈출 비율이 측정되고 확인되지 않은 권한 주장을 더 잘 받아들인다고 보고했다. [부분] 시스템 경로, 레지스트리, 드라이버, 부트 설정, 서명 키는 승인 없이 건드리지 않고, 빌드·테스트는 격리된 디렉터리·VM·컨테이너에서 한다.
- **테스트에 맞춘 해법을 경계한다.** 모든 유효한 입력에서 맞는 해법을 요구하고, 값을 하드코딩하거나 보조 스크립트로 우회하지 말며, 테스트가 틀렸거나 작업이 불가능하면 알리게 한다(Anthropic 지침 문구). 테스트·기대값·경고 설정이 바뀌었는지 `git diff`로 확인한다. [확인]
- **무인 실행은 체크리스트와 종료 조건으로.** 텍스트로 끝나는 진행 보고를 완료로 읽지 않는다. 시작한 백그라운드 명령이나 하위 에이전트가 끝나기를 기다린다. [확인]
- **공개 헤더·ABI 변경은 호출자 영향부터 확인한다.** 범위 밖 변경은 되돌린다. 성능 주장은 명령, 입력, 환경, 전후 수치로 쓴다.
- **effort.** `medium`에서 시작해 어려운 동시성·메모리 손상은 `high`, 측정된 이득이 있을 때만 `xhigh`. `max_tokens`는 생각 토큰을 포함한 상한이라 크게 잡는다. [확인]
- **변경 리뷰 패스는 effort를 올려 돌린다.** 같은 어려운 13건에서 Standard로 8건, Max로 10건을 잡았다(Sonnet 5.5는 6건). 인증·동시성·메모리 변경의 리뷰는 `high` 이상으로 한다. [부분: 13건 표본]
- **최고 단계(`max`)는 어려운 문제에만 쓴다.** 출력 토큰이 `medium`의 약 5배다. 독립 지수는 `max` 59, `medium` 48이다. [확인: Artificial Analysis 모델 페이지]
- **긴 코딩 작업에는 시간 상한을 둔다.** 코딩 에이전트 구성에서 한 작업이 1시간을 넘겼다. 코딩 에이전트 지수는 58로 최상위권이다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **범위 이탈이 4.6보다 늘었다는 보고가 있다.** 요청한 파일과 기능 범위를 먼저 적고 범위 밖 발견은 보고만 하게 한다. [부분: 이슈 미러 검색 요약]
- **소프트웨어 분석·역공학·기존 게임 재현 요청이 거부될 수 있다.** 거부되면 같은 요청을 표현만 바꿔 반복하지 말고 사용자에게 알린다. [부분: 보도]
- **`medium`에서 시작하고 `xhigh`는 쓰기 전에 측정한다.** 반복 확장 평가에서 `xhigh`가 `medium`보다 낮은 결과를 약 4배 비용에 냈다. `xhigh`가 하위 에이전트를 많이 띄워 토큰만 쓴다는 증언이 있다. [확인: 독립 벤치마크 1회 실행, 잡음 가능]
- **품질이 떨어졌다고 느끼면 같은 과제로 먼저 재현한다.** 출시 후 56일간 고정 문제 추적에서는 변화가 감지되지 않았다. 다만 감지 한계가 6~7점이고 긴 세션이 나빠진다는 증언은 따로 있다. [확인: 독립 추적, 한계 있음]
- **정당한 코드 리뷰와 분석이 사이버 안전장치에 걸릴 수 있다.** 쓰기 선행 로그 리뷰, ESP32 블루투스, 오래된 컴파일러 분석이 막혀 이전 모델로 밀렸다는 보고가 반복된다. 막히면 표현만 바꿔 반복하지 말고 사용자에게 알린다. [부분: HN 다수 증언]
- **출력이 필요 이상으로 길다.** 간결한 출력 스타일을 켜면 낫다는 증언이 반복된다. [부분: HN 다수 증언]

## 4. 근거와 한계
- 강점 설명·사이버 거부 처리·무인 실행: [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) [확인: 벤더 서술]
- 테스트 하드코딩 회피: [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) [확인]
- 샌드박스·리뷰 경향 지적: [KDnuggets](https://www.kdnuggets.com/everything-claude-opus-5-5-actually-ships-with), [Zvi: The System Card](https://thezvi.substack.com/p/claude-opus-55-the-system-card) [부분]
- 추가 확인(2026-11-19 웹 검색): [CodeRabbit: Sonnet 5.5 model review](https://coderabbit.ai/blog/sonnet-5-5-model-review)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: claude-opus-5-5 모델 페이지](https://artificialanalysis.ai/models/claude-opus-5-5)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [claudeissues.com: Opus 5.5 범위 이탈 이슈(검색 요약만 확인)](https://claudeissues.com/issue/97117-opus-5-5-severe-scope-creep-and-task-focus-regression-compared-to-opus-4-6)
- 추가 확인(2026-11-19 웹 검색): [The New Stack 보도를 옮긴 기사: Claude Code 거부 증가](https://letsdatascience.com/news/the-new-stack-reports-developers-downgrade-claude-code-over-3a9c5c39)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [HumanLayer: SlopCodeBench 2026-10 (독립 벤치마크)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [livenerf: Opus 5.5 출시 후 품질 변화 추적(독립)](https://github.com/ninjahawk/livenerf)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Sonnet 5.5 스레드](https://news.ycombinator.com/item?id=49881850)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Claude Opus 5.5 스레드](https://news.ycombinator.com/item?id=49803892)
- 한계: C·C++·Rust 시스템 코드에 대한 Opus 5.5 전용 독립 평가는 찾지 못했다.
