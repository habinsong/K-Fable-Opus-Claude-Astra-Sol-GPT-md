# GPT-6.2 Astra · 웹 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6.2-astra` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/01-gpt/gpt-6.2-astra/web.md`](../../../../md/01-gpt/gpt-6.2-astra/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

> **승계 문서.** GPT-6.2 Astra 전용 분야 측정은 아직 없다. 아래 평가·수치·가격은 직전 모델 GPT-6 Astra을 조사한 것이며 GPT-6.2 Astra에는 [추정]으로만 옮겨 쓴다. GPT-6.2 Astra의 확인된 사양은 [`overview.md`](../overview.md)를 따른다.

## 2. 이 모델의 웹 작업 운용
모델 전체 특성(API 규칙, effort, 비판적 평가)은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: Responses API 사용, `none`·`minimal` 불가, effort는 항상 명시.

- **UI 품질에 대한 평가가 갈린다.** 한 구조적 비교는 Astra가 다듬기 없이도 완성도 높은 첫 초안을 낸다고 했고, OpenAI는 스케치·참고 이미지·기존 UI를 동작하는 UI로 바꾸고 스크린샷으로 수정하는 용도를 안내한다. 반면 여러 개발자 후기는 UI 완성도(여백, 타이포그래피, 마감)가 Fable 5.1보다 약하다고 보고한다. 대부분 개별 후기이고 체계적 벤치마크가 아니다. [부분]
  → 라우팅·상태 관리·API 연동·테스트는 Astra에 맡기고, 시각 완성도는 스크린샷을 직접 대조해서 확인한다. 디자인 비중이 큰 화면은 같은 요구사항으로 Fable 5.1과 한 번 비교해 본다. [권고]
- **과잉 설계를 막는다.** 새 컴포넌트·유틸·스크립트를 만들기 전에 프로젝트에 이미 있는 것을 먼저 찾는다. 변경 후 `git diff --stat`으로 새로 생긴 파일이 요청에 필요한 것인지 확인한다.
- **완료 기준을 시작할 때 적는다.** 예: "해당 화면이 브라우저에서 열리고, 콘솔 오류가 없고, 키보드만으로 조작되며, 관련 테스트가 통과한다." 중간 검토를 위해 멈추라는 지시는 넣지 않는다(일찍 멈추는 쪽으로 기운다).
- **접근성·성능·보안을 "충족했다"는 자기 판단을 증거로 쓰지 않는다.** 이 모델의 자기 평가가 틀린 사례가 보고됐다. 접근성 도구, 브라우저 콘솔, 성능 측정 출력으로 확인한다.
- **시각 확인.** 스크린샷은 모델의 해석이 아니라 실제 렌더링과 대조한다. 확인하지 못했으면 "화면 미확인"이라고 보고한다.
- **`xhigh`를 쓰고 `max`는 쓰지 않는다.** 독립 지수가 같은데 출력 토큰이 약 2.4배 든다. [확인: Artificial Analysis 모델 페이지]
- **`low`는 코딩에 쓰지 않는다.** 코딩 에이전트 지수가 `max`보다 18점 낮다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **며칠씩 도는 자율 작업을 맡기지 않는다.** 컴파일러 이식에서 진척이 없고 오히려 느려진 사례와 사소한 질문에서 두 시간 뒤 멈춘 사례가 보고됐다. 목표 지표와 중단 기준을 먼저 정한다. [부분: 개발자 증언]
- **간단한 버그에 경계 사례 조사와 방어 코드를 덧붙인다.** 변경 범위를 요청에 묶는다. [부분: 커뮤니티 증언]
- **코드베이스에 없는 사실을 말하는 일이 보고됐다.** 파일이 열려 있어도 그렇다. 코드 설명은 원문과 대조한다. [부분: 커뮤니티 증언]
- **완료를 일찍 선언한다.** 요구사항 목록을 항목별로 대조한다. [부분: 팀 테스트]
- **보고서가 장황하고 저수준에 치우친다.** 상위 요약부터 쓰게 한다. [부분: 개발자 증언]
- **코드 리뷰와 미묘한 버그 찾기에는 쓸 만하다.** 개발자 증언과 리뷰 시험이 긍정적이다. [부분]
- **여러 요청에 걸쳐 웹 앱을 확장하는 일에 가장 낫다.** 다만 비용이 Sol의 약 3.6배다. [확인: Vals 평가]
- **`xhigh`는 비용이 약 3배인데 이득이 작다.** 반복 확장 평가에서 `xhigh`가 `medium`보다 아주 조금 나았다. 이전 세대 Astra의 측정이다. [부분: 독립 벤치마크 1회 실행]
- **요청을 문자 그대로 받아 모호한 점을 되묻는 편이다.** 의도와 완료 기준을 적는다. [부분: HN 다수 증언]
- **복잡한 작업에서는 Sol보다 처음부터 나은 결과를 낸다는 증언이 여러 건 있다.** 간단한 코딩은 Sol로 충분하다. [부분: HN 다수 증언]
- **구독 한도를 빨리 소진한다는 증언이 있다.** 5시간에 주간 한도의 70%를 썼다는 보고가 있다. 긴 작업 전에 남은 한도를 확인한다. [부분: HN 단일 증언]

## 4. 근거와 한계
- 모델 사양·API 규칙: [openai/codex 마이그레이션 가이드](https://raw.githubusercontent.com/openai/codex/main/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-6-astra.md) [확인]
- UI 평가: [Claude Fable 5.1 vs GPT-6 Astra for Product Design](https://eidosdesign.substack.com/p/claude-fable-51-vs-gpt-6-astra-for), [A Short Review of OpenAI's GPT 6 Astra](https://medium.com/jonathans-musings/a-short-review-of-openais-gpt-6-astra-091fa5beccf9) [부분: 개별 후기·단일 시험]
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: gpt-6-2-astra 모델 페이지](https://artificialanalysis.ai/models/gpt-6-2-astra)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [GPTunneL: GPT-6.2 Astra·Sol 후기 모음](https://www.gptunnel.ru/en/blog/gpt-6-2-astra-sol-reviews)
- 추가 확인(2026-11-19 웹 검색): [Android Headlines: GPT-6.2 Astra·Sol 출시 평가](https://www.androidheadlines.com/2026/11/openai-gpt-6-2-astra-sol-release-reviews.html)
- 추가 확인(2026-11-19 웹 검색): [Vals AI: Vibe Code Bench 1-100 v1.1 (2026-11-17)](https://www.vals.ai/benchmarks/vcb-1-100-v1-1)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [HumanLayer: SlopCodeBench 2026-10 (독립 벤치마크)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: GPT-6.2 Astra·Sol 스레드](https://news.ycombinator.com/item?id=50535230)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Claude Opus 5.5 스레드](https://news.ycombinator.com/item?id=49803892)
- 한계: 웹 UI에 대한 체계적 독립 벤치마크는 찾지 못했다. "Fable 5.1보다 약하다"는 평가도 "첫 초안이 낫다"는 평가도 재현 확인 전까지 잠정이다.
