# Claude Sonnet 5.5 · 웹 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-sonnet-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/02-claude/sonnet-5.5/web.md`](../../../../md/02-claude/sonnet-5.5/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 기본 `high`(에이전트는 `medium`부터), `low`에서 검증을 건너뜀, 요청하지 않은 테스트·문서·파일을 덧붙임, `max`는 비싸고 점수가 떨어진 사례.

- **화면·컴포넌트 구현의 주력으로 쓴다.** 속도와 지능의 균형형이고 가격이 Opus 5.5의 절반 수준이다. 잘 정의된 화면 작업은 `medium`, 상태 관리나 긴 작업은 `high`에서 시작한다. `max`는 쓰지 않는다. 한 평가에서 `max`가 `xhigh`보다 낮고 작업당 비용도 Opus 5.5보다 높았다. [확인/부분]
- **요청하지 않은 추가를 막는다.** 이 모델은 모든 effort에서 저장소 관례에 맞는 테스트, 문서, 작은 보조 파일을 덧붙이고 effort가 높을수록 많다. 변경 자체는 요청에 가깝다. 이 저장소는 최소 변경이 원칙이므로(전역 지침) "요청한 일이 끝나고 확인되면 멈추고 보고하라. 요청하지 않은 기능·테스트·파일·문서·리팩터링은 하지 말고 끝에서 제안만 하라"를 시스템 프롬프트에 둔다. [확인]
- **`low`에서는 변경 후 실제 검사를 강제한다.** 코드를 바꾸고 테스트·빌드를 돌리지 않은 채 완료라고 보고할 수 있다. "문법 검사만으로는 인정되지 않는다. 실행 가능한 코드를 바꿨으면 프로젝트 테스트·타입 체커·빌드를 돌려라"를 넣는다. 의존성이 없을 뿐이면 프로젝트 패키지 관리자로 설치하고 `sudo`나 시스템 패키지 관리자는 쓰지 않는다. [확인]
- **브라우저 지원·표준·요건은 검색으로 확인하게 한다.** 허용·요구·요금처럼 바뀐 세부를 학습 지식으로 답하는 경향이 있다. Artificial Analysis 지식 평가에서 Sonnet 5.5는 54%, Opus 5.5는 66%였다. [확인/부분] 도구 사용을 억제하는 문구를 지우고 확인을 명시한다.
- **UI 확인에는 자르기·확대 도구를 준다.** 차트는 모든 effort에서, 기술 도면은 `high` 이상에서 효과가 있다. 렌더링 결과는 직접 열어 대조하고 확인하지 못했으면 "화면 미확인"이라고 보고한다. [확인]
- **채팅형 UI 호출은 지연에 맞춰 `medium`·`low`.** `medium` 이상은 인사에도 짧게 생각해 첫 토큰이 늦다. 추론 없이 답하려면 `between_tools`(`high` 이하)를 쓰되 도구가 없는 요청에서는 생각 없이 답한다는 점을 안다. [확인]
- **사용자 입력을 작업 중 받는 UI.** 사용자 글을 `tool_result`에 넣지 않고 같은 사용자 메시지의 텍스트 블록으로 보낸다. 토큰 카운트다운을 도구 결과마다 붙이지 않는다. 주입으로 오해할 수 있다. [확인]
- **UI 디자인 품질에 대한 Sonnet 5.5 전용 평가는 찾지 못했다.** [미확인] 기존 프로젝트는 기존 UI 체계가 우선한다(§1.1).
- **지시를 문자 그대로 따른다.** "도구 호출을 최소화하라" 같은 표현을 엄격하게 적용한다. 범위와 예외, 의도를 함께 적는다. [부분: 단일 리뷰 서비스 관찰]
- **어려운 결함의 리뷰는 단독으로 맡기지 않는다.** 어려운 13건 중 6건만 잡았고 4건은 모든 설정에서 놓쳤다(Opus 5.5는 8~10건). 인증·동시성·메모리 변경은 Opus 5.5 이상이나 사람의 리뷰를 함께 둔다. [부분: 13건 표본]
- **`xhigh`까지만 쓴다.** `max`는 `xhigh`보다 출력 토큰이 약 3배 들고 한 작업이 30분을 넘으며 일부 평가에서는 오히려 낮았다. 독립 지수는 `max` 55, `xhigh` 50이다. [확인: Artificial Analysis 모델 페이지]
- **실제 저장소 변경은 Opus 5.5보다 약하다.** 어려운 변경은 Opus 5.5로 교차한다. 코딩 에이전트 지수의 저장소 변경 항목이 39 대 44다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **한 번에 답하는 질문은 Haiku보다 낮게 나온 시험이 있다.** 질문·조사성 일은 Opus 5.5로 올린다. [부분: 단일 시험]
- **낮은 effort의 Opus 5.5가 중간 effort의 Sonnet 5.5보다 낫다는 증언이 있다.** 두 쪽을 같은 과제로 비교한 뒤 고른다. [부분: HN 단일 증언]

## 4. 근거와 한계
- 범위 억제·검증 강제·검색·mid-turn 메시지: [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5) [확인]
- `max` 비용·지식 평가: [eesel.ai 리뷰](https://www.eesel.ai/blog/claude-sonnet-5-5-review), [Claude 5.5 is brilliant, confusing, and very hungry](https://dreasays.substack.com/p/claude-55-is-brilliant-confusing) [부분]
- 추가 확인(2026-11-19 웹 검색): [CodeRabbit: Sonnet 5.5 model review](https://coderabbit.ai/blog/sonnet-5-5-model-review)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: claude-sonnet-5-5 모델 페이지](https://artificialanalysis.ai/models/claude-sonnet-5-5)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [Bito: Fable 5.2 대 Opus 5.5 비교 시험](https://bito.ai/blog/claude-fable-5-2-vs-opus-5-5-sonnet-haiku/)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Sonnet 5.5 스레드](https://news.ycombinator.com/item?id=49881850)
- 한계: 웹 프런트엔드 품질의 독립 비교는 찾지 못했다.
