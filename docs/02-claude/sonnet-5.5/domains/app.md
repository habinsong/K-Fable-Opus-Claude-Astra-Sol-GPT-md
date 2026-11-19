# Claude Sonnet 5.5 · 앱 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-sonnet-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/02-claude/sonnet-5.5/app.md`](../../../../md/02-claude/sonnet-5.5/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 기본 `high`(에이전트는 `medium`부터), `low`·`medium`에서 중간에 확인을 구하며 멈춤, 컴퓨터 사용은 `computer_toolset_20260801`.

- **모바일 앱 개발에 대한 Sonnet 5.5 전용 독립 평가는 찾지 못했다.** [미확인] 실기기 검증을 생략하지 않는다.
- **빌드-수정 반복에 경제적이다.** 가격이 입력 $2 / 출력 $10이고 캐시 읽기 $0.10이다. 컴파일 오류, 린트, 단위 테스트 수정처럼 짧은 루프는 `medium`으로 돌린다. `low`에서는 변경을 검사 없이 완료로 보고할 수 있으므로 "문법 검사만으로는 인정되지 않는다. 프로젝트 테스트·타입 체커·빌드를 돌려라, 못 돌리면 무엇을 왜 못 했는지 말하라"를 시스템 프롬프트에 넣는다. [확인]
- **긴 작업에서 중간에 멈춰 묻는다.** `low`·`medium`에서는 계획 확인이나 여러 부분 중 하나를 끝낸 뒤의 계속 여부를 묻고 멈추는 경향이 있다. "사용자가 요청한 일이 끝날 때까지 계속하고 사용자 없이 진행할 수 없거나 위험한 단계 앞에서만 멈춰라"를 쓰거나 effort를 올린다. 앱에서 승인이 필요한 단계는 서명 키 접근, 스토어 제출, 배포, 외부 전송이다(전역 지침). [확인]
- **시뮬레이터·에뮬레이터 조작은 컴퓨터 사용 도구로.** 이 모델은 `computer_toolset_20260801`을 쓴다. 이전 `computer_20251124`는 Claude API에서 400이고 Amazon Bedrock에서만 허용된다. 조작 결과는 스크린샷·로그·테스트 출력으로 확인한다. Sonnet 5.5의 컴퓨터 사용 성공률에 대한 독립 수치는 찾지 못했다. [확인/미확인]
- **스토어 규정은 검색으로 확인하게 한다.** 이 모델은 허용·요구·요금처럼 바뀐 세부를 학습 지식으로 답하는 경향이 있고 지식 평가 점수가 Opus 5.5보다 낮다(54% 대 66%). [확인/부분] §1.2 표를 작업 시점에 공식 문서로 다시 확인한다.
- **긴 출력을 스트리밍한다.** 에이전트 코딩에서는 `max_tokens`를 128K로 두고 스트리밍한다. 생각 토큰도 포함되는 상한이다. [확인]
- **요청하지 않은 추가를 막는다.** 테스트·문서·보조 파일을 덧붙이는 경향을 "요청하지 않은 것은 하지 말고 끝에서 제안만"으로 누른다. [확인]
- **서명 키, 프로파일, 스토어 제출·배포는 승인 후에만.**
- **지시를 문자 그대로 따른다.** "도구 호출을 최소화하라" 같은 표현을 엄격하게 적용한다. 범위와 예외, 의도를 함께 적는다. [부분: 단일 리뷰 서비스 관찰]
- **어려운 결함의 리뷰는 단독으로 맡기지 않는다.** 어려운 13건 중 6건만 잡았고 4건은 모든 설정에서 놓쳤다(Opus 5.5는 8~10건). 인증·동시성·메모리 변경은 Opus 5.5 이상이나 사람의 리뷰를 함께 둔다. [부분: 13건 표본]
- **`xhigh`까지만 쓴다.** `max`는 `xhigh`보다 출력 토큰이 약 3배 들고 한 작업이 30분을 넘으며 일부 평가에서는 오히려 낮았다. 독립 지수는 `max` 55, `xhigh` 50이다. [확인: Artificial Analysis 모델 페이지]
- **실제 저장소 변경은 Opus 5.5보다 약하다.** 어려운 변경은 Opus 5.5로 교차한다. 코딩 에이전트 지수의 저장소 변경 항목이 39 대 44다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **한 번에 답하는 질문은 Haiku보다 낮게 나온 시험이 있다.** 질문·조사성 일은 Opus 5.5로 올린다. [부분: 단일 시험]
- **낮은 effort의 Opus 5.5가 중간 effort의 Sonnet 5.5보다 낫다는 증언이 있다.** 두 쪽을 같은 과제로 비교한 뒤 고른다. [부분: HN 단일 증언]

## 4. 근거와 한계
- 검증 강제·계속 진행·컴퓨터 사용 도구: [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5), [What's new in Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5) [확인]
- 지식 평가 격차: [eesel.ai 리뷰](https://www.eesel.ai/blog/claude-sonnet-5-5-review) [부분]
- 추가 확인(2026-11-19 웹 검색): [CodeRabbit: Sonnet 5.5 model review](https://coderabbit.ai/blog/sonnet-5-5-model-review)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: claude-sonnet-5-5 모델 페이지](https://artificialanalysis.ai/models/claude-sonnet-5-5)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [Bito: Fable 5.2 대 Opus 5.5 비교 시험](https://bito.ai/blog/claude-fable-5-2-vs-opus-5-5-sonnet-haiku/)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Sonnet 5.5 스레드](https://news.ycombinator.com/item?id=49881850)
- 한계: 모바일 개발과 컴퓨터 사용에 대한 Sonnet 5.5 전용 독립 벤치마크는 없다.
