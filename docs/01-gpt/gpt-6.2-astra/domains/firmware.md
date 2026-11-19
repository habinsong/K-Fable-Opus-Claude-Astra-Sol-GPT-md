# GPT-6.2 Astra · 펌웨어 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6.2-astra` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/01-gpt/gpt-6.2-astra/firmware.md`](../../../../md/01-gpt/gpt-6.2-astra/firmware.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/firmware.md`](../../../_common/domain-rules/firmware.md)

> **승계 문서.** GPT-6.2 Astra 전용 분야 측정은 아직 없다. 아래 평가·수치·가격은 직전 모델 GPT-6 Astra을 조사한 것이며 GPT-6.2 Astra에는 [추정]으로만 옮겨 쓴다. GPT-6.2 Astra의 확인된 사양은 [`overview.md`](../overview.md)를 따른다.

## 2. 이 모델의 펌웨어 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 자율적으로 끝까지 가려는 경향, 자기 평가 불신, 과잉 설계 주의.

- **임베디드 개발에 대한 공개 평가는 찾지 못했다.** RTOS, 드라이버, 브링업에 대한 결과는 없다. [미확인] 가장 가까운 근거는 시스템 카드의 리버스 엔지니어링 평가(펌웨어 바이너리 포함)와 커널 최적화 평가인데, 벤더 자체 평가이고 개발 작업의 정확성을 보증하지 않는다. [부분]
  → 바이너리 분석, 레지스터 접근 코드 읽기, 인터럽트·타이밍 문제의 가설 세우기에는 쓰되, 결론은 맵 파일·디스어셈블리·로직 분석기 캡처 같은 증거로 확인한다.
- **터미널 작업이 만능은 아니다.** Terminal-Bench 4.0 점수는 57.7%와 57.9%로 출처마다 다르게 적혀 있고 절반 가까이는 실패한다는 뜻이다. [부분] 빌드·플래시 스크립트를 모델이 만들었다면 실행 전에 읽는다.
- **자율 진행 경향 때문에 정지점을 명시한다.** 이 모델은 사용자가 따로 묻지 않아도 끝까지 이어가려 한다. 그래서 되돌릴 수 없는 단계(플래시 소거, 퓨즈·OTP 쓰기, 보호 비트, 부트로더 덮어쓰기, 디버그 포트 잠금) 앞에서만 멈추고 대상 장치와 이미지를 확인받는다. 그 밖의 단계에는 정지점을 넣지 않는다(일찍 멈추는 쪽으로 기운다).
- **레지스터와 타이밍은 문서로 확인한다.** 비트 필드, 클럭 설정, 인터럽트 번호를 기억으로 쓰지 않는다. 데이터시트·레퍼런스 매뉴얼의 개정판과 페이지를 근거로 남기고, 확인하지 못했으면 값을 쓰지 않는다.
- **호스트에서 돌릴 수 있게 나눈다.** 하드웨어 추상화 뒤쪽 로직은 호스트 단위 테스트가 가능하도록 분리하라고 지시한다. 과잉 설계를 막기 위해 새 추상화 계층은 테스트에 꼭 필요한 한 겹으로 제한한다.
- **"통과했다"는 자기 판단을 쓰지 않는다.** 컴파일 성공이나 모델의 요약을 동작 확인으로 보고하지 않는다. 실제 보드에서 확인하지 못했으면 "하드웨어 미검증"이라고 쓴다.
- **`xhigh`를 쓰고 `max`는 쓰지 않는다.** 독립 지수가 같은데 출력 토큰이 약 2.4배 든다. [확인: Artificial Analysis 모델 페이지]
- **`low`는 코딩에 쓰지 않는다.** 코딩 에이전트 지수가 `max`보다 18점 낮다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **며칠씩 도는 자율 작업을 맡기지 않는다.** 컴파일러 이식에서 진척이 없고 오히려 느려진 사례와 사소한 질문에서 두 시간 뒤 멈춘 사례가 보고됐다. 목표 지표와 중단 기준을 먼저 정한다. [부분: 개발자 증언]
- **간단한 버그에 경계 사례 조사와 방어 코드를 덧붙인다.** 변경 범위를 요청에 묶는다. [부분: 커뮤니티 증언]
- **코드베이스에 없는 사실을 말하는 일이 보고됐다.** 파일이 열려 있어도 그렇다. 코드 설명은 원문과 대조한다. [부분: 커뮤니티 증언]
- **완료를 일찍 선언한다.** 요구사항 목록을 항목별로 대조한다. [부분: 팀 테스트]
- **보고서가 장황하고 저수준에 치우친다.** 상위 요약부터 쓰게 한다. [부분: 개발자 증언]
- **코드 리뷰와 미묘한 버그 찾기에는 쓸 만하다.** 개발자 증언과 리뷰 시험이 긍정적이다. [부분]
- **`xhigh`는 비용이 약 3배인데 이득이 작다.** 반복 확장 평가에서 `xhigh`가 `medium`보다 아주 조금 나았다. 이전 세대 Astra의 측정이다. [부분: 독립 벤치마크 1회 실행]
- **요청을 문자 그대로 받아 모호한 점을 되묻는 편이다.** 의도와 완료 기준을 적는다. [부분: HN 다수 증언]
- **복잡한 작업에서는 Sol보다 처음부터 나은 결과를 낸다는 증언이 여러 건 있다.** 간단한 코딩은 Sol로 충분하다. [부분: HN 다수 증언]
- **구독 한도를 빨리 소진한다는 증언이 있다.** 5시간에 주간 한도의 70%를 썼다는 보고가 있다. 긴 작업 전에 남은 한도를 확인한다. [부분: HN 단일 증언]

## 4. 근거와 한계
- 리버스 엔지니어링·커널 최적화: [GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra), [The New Stack](https://thenewstack.io/openai-gpt6-astra-benchmarks/) [부분: 벤더 자체 평가]
- Terminal-Bench 수치 불일치: [Vellum](https://www.vellum.ai/blog/gpt-6-astra-benchmarks-explained), [DataCamp](https://www.datacamp.com/blog/gpt-6-astra) [부분]
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: gpt-6-2-astra 모델 페이지](https://artificialanalysis.ai/models/gpt-6-2-astra)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [GPTunneL: GPT-6.2 Astra·Sol 후기 모음](https://www.gptunnel.ru/en/blog/gpt-6-2-astra-sol-reviews)
- 추가 확인(2026-11-19 웹 검색): [Android Headlines: GPT-6.2 Astra·Sol 출시 평가](https://www.androidheadlines.com/2026/11/openai-gpt-6-2-astra-sol-release-reviews.html)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [HumanLayer: SlopCodeBench 2026-10 (독립 벤치마크)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: GPT-6.2 Astra·Sol 스레드](https://news.ycombinator.com/item?id=50535230)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Claude Opus 5.5 스레드](https://news.ycombinator.com/item?id=49803892)
- 한계: 임베디드·드라이버·브링업에 대한 독립 근거가 없다. 이 문서의 정지점 규칙은 모델의 자율 진행 경향(OpenAI 지침)과 비가역 작업의 위험에서 도출한 안전 권고이며, 실험으로 검증된 규칙이 아니다.
