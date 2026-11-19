# Claude Sonnet 5.5 · 네이티브 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-sonnet-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/02-claude/sonnet-5.5/native.md`](../../../../md/02-claude/sonnet-5.5/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 기본 `high`(에이전트는 `medium`부터), `xhigh`·`max`는 요청하지 않은 점검 라운드를 시작함, 사이버 요청은 Sonnet 5로 넘어갈 수 있음.

- **시스템 코드는 `high`에서 시작하고 `xhigh`는 어려운 문제에만.** Anthropic은 가장 어려운 장시간 작업에는 Opus를 권한다. 경쟁 상태, 메모리 손상, 컴파일러 최적화가 얽힌 버그에서 같은 가설이 두 번 틀리면 Opus 5.5에 같은 재현 절차와 로그를 넘긴다. [확인/권고]
- **`xhigh`·`max`의 자체 점검 라운드를 끊는다.** 이 레벨에서는 요청한 일이 끝난 뒤에도 스스로 리뷰·강화 라운드를 돌리고 하위 에이전트를 띄워 관련 수정을 덧붙인다. 시간과 토큰이 크게 든다. "요청한 일이 끝나고 검사가 통과하면 멈추고 보고하라. 스스로 추가 리뷰를 시작하지 말고 요청이 없으면 리뷰어 하위 에이전트를 띄우지 말라"를 쓰면 `max`에서 세션 비용이 약 3분의 1 줄었다고 한다. 일상 작업은 `high` 이하에서 돌린다. [확인]
- **`low`에서는 검증을 건너뛴다.** 의존성이 설치되지 않았다는 이유로 프로젝트 테스트를 건너뛸 수 있다. 실제 검사(테스트, 타입 체커, 빌드, 바뀐 명령 자체)를 요구하고, 불가하면 어떤 검사를 왜 못 했는지 말하게 한다. sanitizer 빌드를 돌리지 못했으면 "미실행"으로 보고한다. [확인]
- **보안 인접 요청의 경계.** 소스에서 취약점을 찾는 일은 허용되고 위험도가 높은 이중 용도 사이버 작업은 제한된다. 거부(`cyber`)는 서버 쪽 대체로 Sonnet 5에서 재시도될 수 있고, 높은 위험의 사이버 요청이 눈에 띄게 Sonnet 5로 넘어간다는 보고가 있다. 정당한 작업이 막히면 Cyber Verification Program을 확인한다. [확인/부분]
- **도구 호출 이름이 어긋날 수 있다.** `bash`와 `Bash`처럼 대소문자가 다른 호출이나 조금 다른 매개변수 이름을 낼 수 있다. 하네스는 명확하면 받아 주거나 기대한 이름을 담은 `is_error: true` 결과를 돌려준다. [확인]
- **끈기가 약하다는 사용자 보고.** 답을 얻으려고 계속 시도하는 데 소극적이라 점수가 낮아진 사례가 있다. 개별 후기다. [부분] 같은 실패가 3번 반복되면 접근을 바꾸거나 막힌 지점을 보고하게 한다(전역 지침).
- **테스트에 맞춘 우회를 막는다.** 테스트·기대값·경고 설정이 바뀌었는지 `git diff`로 확인한다. 공개 헤더·ABI 변경은 호출자 영향부터 확인하고 범위 밖 변경은 되돌린다.
- **시스템 경로, 레지스트리, 드라이버, 부트 설정, 서명 키는 승인 없이 건드리지 않는다.**
- **지시를 문자 그대로 따른다.** "도구 호출을 최소화하라" 같은 표현을 엄격하게 적용한다. 범위와 예외, 의도를 함께 적는다. [부분: 단일 리뷰 서비스 관찰]
- **어려운 결함의 리뷰는 단독으로 맡기지 않는다.** 어려운 13건 중 6건만 잡았고 4건은 모든 설정에서 놓쳤다(Opus 5.5는 8~10건). 인증·동시성·메모리 변경은 Opus 5.5 이상이나 사람의 리뷰를 함께 둔다. [부분: 13건 표본]
- **`xhigh`까지만 쓴다.** `max`는 `xhigh`보다 출력 토큰이 약 3배 들고 한 작업이 30분을 넘으며 일부 평가에서는 오히려 낮았다. 독립 지수는 `max` 55, `xhigh` 50이다. [확인: Artificial Analysis 모델 페이지]
- **실제 저장소 변경은 Opus 5.5보다 약하다.** 어려운 변경은 Opus 5.5로 교차한다. 코딩 에이전트 지수의 저장소 변경 항목이 39 대 44다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **한 번에 답하는 질문은 Haiku보다 낮게 나온 시험이 있다.** 질문·조사성 일은 Opus 5.5로 올린다. [부분: 단일 시험]
- **사이버 안전장치에 Opus보다 덜 걸린다는 증언이 있다.** 분석·역공학이 Opus에서 막히면 이 모델로 옮겨 본다. [부분: HN 단일 증언]
- **낮은 effort의 Opus 5.5가 중간 effort의 Sonnet 5.5보다 낫다는 증언이 있다.** 두 쪽을 같은 과제로 비교한 뒤 고른다. [부분: HN 단일 증언]

## 4. 근거와 한계
- 자체 점검 라운드·검증·도구 호출 허용: [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5) [확인]
- 거부·대체: [What's new in Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5) [확인]
- 끈기·Opus와의 비교: [Thomas Wiegold 비교](https://thomas-wiegold.com/blog/claude-sonnet-5-5-review/), [AIToolsReview](https://aitoolsreview.co.uk/insights/claude-sonnet-5-5) [부분]
- 추가 확인(2026-11-19 웹 검색): [CodeRabbit: Sonnet 5.5 model review](https://coderabbit.ai/blog/sonnet-5-5-model-review)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: claude-sonnet-5-5 모델 페이지](https://artificialanalysis.ai/models/claude-sonnet-5-5)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [Bito: Fable 5.2 대 Opus 5.5 비교 시험](https://bito.ai/blog/claude-fable-5-2-vs-opus-5-5-sonnet-haiku/)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Sonnet 5.5 스레드](https://news.ycombinator.com/item?id=49881850)
- 한계: C·C++·Rust 시스템 코드에 대한 Sonnet 5.5 전용 독립 평가는 찾지 못했다.
