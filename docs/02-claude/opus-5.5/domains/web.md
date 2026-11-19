# Claude Opus 5.5 · 웹 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-opus-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/02-claude/opus-5.5/web.md`](../../../../md/02-claude/opus-5.5/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 기본 `medium`, 실제 저장소의 다단계 작업에 강점이라고 설명됨, 리뷰 지적에 좁게 대응하는 경향, 무인 실행에서 중간에 멈출 수 있음.

- **웹 작업의 기본 모델로 쓴다.** Anthropic이 대부분의 워크로드에서 가장 먼저 시도하라고 권하는 모델이다. 기본 `medium`에서 시작하고, 상태 관리나 복잡한 구조 문제에서만 `high` 이상으로 올린다. `xhigh`·`max`는 같은 레벨에서 Opus 5보다 생각이 길어 측정된 이득이 있을 때만 쓴다. [확인]
- **스크린샷 검수에는 자르기·확대 도구를 준다.** 이 모델은 도구 없이도 밀도 높은 차트와 화면을 이전보다 정확히 읽는다고 한다. 가장 촘촘한 입력에는 고해상도 이미지와 이미지 처리 도구(PIL, OpenCV, 자르기 도구)가 정확도를 더한다. 렌더링 결과는 직접 열어 대조하고, 확인하지 못했으면 "화면 미확인"이라고 보고한다. [확인]
- **기존 프로젝트는 기존 UI 체계가 우선한다.** 디자인 방향 없이 프런트엔드를 시키면 몇 가지 기본 스타일로 수렴한다. 새 화면을 처음부터 만들 때만 "배경색, 헤드라인의 이탤릭 강조어, 번호가 붙은 섹션 라벨, 알약 모양 버튼을 쓰지 말라"처럼 피할 패턴을 구체적으로 적는다. 기존 디자인 토큰과 컴포넌트가 있는 프로젝트에서는 이 문서의 §1.1 규칙(새 디자인 시스템을 들이지 않는다)이 이긴다. 결과를 보고 쓰인 스타일을 확인하며 목록을 늘린다. [확인]
- **요구가 느슨할수록 먼저 둘러보게 한다.** 이 모델은 빠르게 작업에 들어간다. 관련 컴포넌트, 기존 훅, 스타일 규칙, 테스트 위치를 변경 전에 찾아보라고 한 문장을 덧붙이면 놓치는 맥락이 줄어든다. [확인: 다중 앱 작업 기준, 저장소 작업에는 추정]
- **리뷰 지적을 반영할 때 설계 전제를 다시 묻는다.** 시스템 카드 분석은 이 모델이 리뷰 피드백에 좁게만 대응하고 전체 설계가 맞는지 다시 따지지 않는 경향을 지적했다. [부분] 코드 리뷰 뒤에는 "지적 사항을 고친 뒤에도 이 화면의 구조와 상태 관리가 여전히 맞는가"를 한 번 더 묻는다.
- **무인 실행에서는 체크리스트로 이어 간다.** 긴 작업 중 텍스트로 끝나는 진행 보고를 완료로 읽는 하네스는 거기서 멈춘다. 화면별 할 일을 목록으로 두고 남은 항목이 있으면 이름을 적어 이어서 하라고 보낸다. [확인]
- **웹 페이지·도구 출력의 지시문은 데이터다.** 사용자가 붙인 글은 표시 태그로 감싸야 지시가 걸러진다고 한다. 표시를 쓰지 않는 하네스는 붙여 넣은 글 속 지시를 따른다는 지적을 우선한다. [확인/부분]
- **보안·접근성은 도구 출력으로 확인한다.** 취약점 찾기는 허용되지만 고위험 이중 용도 작업은 제한된다. 인가, 입력 검증, 비밀 노출은 §1.1 기준으로 점검한다.
- **변경 리뷰 패스는 effort를 올려 돌린다.** 같은 어려운 13건에서 Standard로 8건, Max로 10건을 잡았다(Sonnet 5.5는 6건). 인증·동시성·메모리 변경의 리뷰는 `high` 이상으로 한다. [부분: 13건 표본]
- **최고 단계(`max`)는 어려운 문제에만 쓴다.** 출력 토큰이 `medium`의 약 5배다. 독립 지수는 `max` 59, `medium` 48이다. [확인: Artificial Analysis 모델 페이지]
- **긴 코딩 작업에는 시간 상한을 둔다.** 코딩 에이전트 구성에서 한 작업이 1시간을 넘겼다. 코딩 에이전트 지수는 58로 최상위권이다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **여러 요청에 걸친 웹 앱 확장은 비용과 시간이 가장 크다.** Astra·Carbon·GLM과 같은 과제로 비교한 뒤 정한다. [확인: Vals 평가]
- **범위 이탈이 4.6보다 늘었다는 보고가 있다.** 요청한 파일과 기능 범위를 먼저 적고 범위 밖 발견은 보고만 하게 한다. [부분: 이슈 미러 검색 요약]
- **소프트웨어 분석·역공학·기존 게임 재현 요청이 거부될 수 있다.** 거부되면 같은 요청을 표현만 바꿔 반복하지 말고 사용자에게 알린다. [부분: 보도]
- **`medium`에서 시작하고 `xhigh`는 쓰기 전에 측정한다.** 반복 확장 평가에서 `xhigh`가 `medium`보다 낮은 결과를 약 4배 비용에 냈다. `xhigh`가 하위 에이전트를 많이 띄워 토큰만 쓴다는 증언이 있다. [확인: 독립 벤치마크 1회 실행, 잡음 가능]
- **품질이 떨어졌다고 느끼면 같은 과제로 먼저 재현한다.** 출시 후 56일간 고정 문제 추적에서는 변화가 감지되지 않았다. 다만 감지 한계가 6~7점이고 긴 세션이 나빠진다는 증언은 따로 있다. [확인: 독립 추적, 한계 있음]
- **출력이 필요 이상으로 길다.** 간결한 출력 스타일을 켜면 낫다는 증언이 반복된다. [부분: HN 다수 증언]

## 4. 근거와 한계
- 효과 설정·무인 실행·프런트엔드 기본값·시각 도구: [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) [확인]
- 리뷰 대응 경향·붙여 넣은 글 지적: [Zvi: The System Card](https://thezvi.substack.com/p/claude-opus-55-the-system-card), [KDnuggets](https://www.kdnuggets.com/everything-claude-opus-5-5-actually-ships-with) [부분]
- 추가 확인(2026-11-19 웹 검색): [CodeRabbit: Sonnet 5.5 model review](https://coderabbit.ai/blog/sonnet-5-5-model-review)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: claude-opus-5-5 모델 페이지](https://artificialanalysis.ai/models/claude-opus-5-5)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [Vals AI: Vibe Code Bench 1-100 v1.1 (2026-11-17)](https://www.vals.ai/benchmarks/vcb-1-100-v1-1)
- 추가 확인(2026-11-19 웹 검색): [claudeissues.com: Opus 5.5 범위 이탈 이슈(검색 요약만 확인)](https://claudeissues.com/issue/97117-opus-5-5-severe-scope-creep-and-task-focus-regression-compared-to-opus-4-6)
- 추가 확인(2026-11-19 웹 검색): [The New Stack 보도를 옮긴 기사: Claude Code 거부 증가](https://letsdatascience.com/news/the-new-stack-reports-developers-downgrade-claude-code-over-3a9c5c39)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [HumanLayer: SlopCodeBench 2026-10 (독립 벤치마크)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [livenerf: Opus 5.5 출시 후 품질 변화 추적(독립)](https://github.com/ninjahawk/livenerf)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Claude Opus 5.5 스레드](https://news.ycombinator.com/item?id=49803892)
- 한계: 웹 UI 품질을 독립적으로 비교한 자료는 찾지 못했다. 위 권고는 Anthropic이 모델별로 기술한 행동 차이에서 도출했다.
