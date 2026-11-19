# GPT-6.2 Astra · 네이티브 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6.2-astra` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/01-gpt/gpt-6.2-astra/native.md`](../../../../md/01-gpt/gpt-6.2-astra/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

> **승계 문서.** GPT-6.2 Astra 전용 분야 측정은 아직 없다. 아래 평가·수치·가격은 직전 모델 GPT-6 Astra을 조사한 것이며 GPT-6.2 Astra에는 [추정]으로만 옮겨 쓴다. GPT-6.2 Astra의 확인된 사양은 [`overview.md`](../overview.md)를 따른다.

## 2. 이 모델의 네이티브 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: Responses API, effort 명시, 자기 평가를 증거로 쓰지 않는다.

- **시스템 수준 작업에 대한 근거는 대부분 벤더 시스템 카드다.** OpenAI는 커널 최적화에서 하드웨어 제약을 이해하고 정확성 문제를 디버깅하며 성능을 개선한다고 설명한다. 또 바이너리 262개(C·C++·Go·Rust, 다양한 컴파일·보호 설정, 펌웨어 포함)로 만든 리버스 엔지니어링 평가에서 pass@4 99.2%(GPT-5.6 Sol은 68.7%)를 보고했다. 독립 재현은 찾지 못했다. [부분]
  → 크래시 덤프·디스어셈블리·성능 병목 분석에 쓸 수 있지만, 분석 결과는 재현 가능한 명령(디버거 세션, 프로파일러 출력)으로 확인한 뒤에 채택한다.
- **수정이 새 버그를 만드는 사례가 있다.** 한 독립 테스트에서 Astra는 GPT-5.6의 실수를 잡아냈지만 동시에 동작을 깨는 버그를 넣었고, 찾는 데 몇 시간이 걸렸다. [부분]
  → 큰 변경을 한 번에 하지 않는다. 한 조각을 바꿀 때마다 해당 테스트와 sanitizer 빌드를 돌리고, 통과를 확인한 뒤에 다음 조각으로 간다(전역 지침).
- **과잉 설계를 막는다.** 시스템 코드에서 불필요한 추상화 계층, 보조 스크립트, 래퍼를 만들지 않는다. 공개 헤더·ABI·설정 형식을 건드린 변경은 `git diff`로 호출자 영향을 먼저 확인한다.
- **성능 주장은 측정으로만.** "최적화했다", "빨라졌다"는 모델의 자기 판단을 쓰지 않는다. 명령, 입력, 환경, 전후 수치를 같이 적는다.
- **지침 충돌을 점검한다.** 이 저장소는 하위 디렉터리마다 규칙이 다를 수 있다. 이 모델은 충돌하는 지침에 민감해 멈추거나 표류할 수 있으므로, 작업 위치에서 가장 가까운 지침 파일이 우선한다는 점을 확인하고 충돌이 있으면 인용해서 보고한다.
- **승인 필요 동작은 전역 지침 목록뿐이다.** 시스템 경로·레지스트리·드라이버·부트 설정 변경과 서명 키 접근은 사용자 승인 후에만 한다.
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
- 시스템 카드 수치(리버스 엔지니어링, 커널 최적화): [GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra) 검색 스니펫 [부분: 벤더 자체 평가]
- 새 버그 사례·종합 평가: [NeoTeo](https://www.neoteo.com/en/gpt-6-astra-improves-coding-and-computer-use-but-still-needs-supervision), [Layer3 Labs](https://www.layer3labs.io/guides/gpt-6-astra-review) [부분: 단일 후기]
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: gpt-6-2-astra 모델 페이지](https://artificialanalysis.ai/models/gpt-6-2-astra)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [GPTunneL: GPT-6.2 Astra·Sol 후기 모음](https://www.gptunnel.ru/en/blog/gpt-6-2-astra-sol-reviews)
- 추가 확인(2026-11-19 웹 검색): [Android Headlines: GPT-6.2 Astra·Sol 출시 평가](https://www.androidheadlines.com/2026/11/openai-gpt-6-2-astra-sol-release-reviews.html)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [HumanLayer: SlopCodeBench 2026-10 (독립 벤치마크)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: GPT-6.2 Astra·Sol 스레드](https://news.ycombinator.com/item?id=50535230)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Claude Opus 5.5 스레드](https://news.ycombinator.com/item?id=49803892)
- 한계: 네이티브 앱·데스크톱·드라이버 개발에 대한 독립 평가는 찾지 못했다. 다른 코딩 벤치마크에서는 모델 간 격차가 거의 없다는 분석도 있다. [부분]
