# GPT-6.2 Astra · 앱 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6.2-astra` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/01-gpt/gpt-6.2-astra/app.md`](../../../../md/01-gpt/gpt-6.2-astra/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

> **승계 문서.** GPT-6.2 Astra 전용 분야 측정은 아직 없다. 아래 평가·수치·가격은 직전 모델 GPT-6 Astra을 조사한 것이며 GPT-6.2 Astra에는 [추정]으로만 옮겨 쓴다. GPT-6.2 Astra의 확인된 사양은 [`overview.md`](../overview.md)를 따른다.

## 2. 이 모델의 앱 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: Responses API, effort 명시, 지침 충돌과 반복 규칙에 민감.

- **모바일 특화 평가는 찾지 못했다.** iOS·Android 앱 개발에 대한 독립 평가나 공개 벤치마크는 확인하지 못했다. [미확인] 컴퓨터 사용 성능(아래)과 일반 코딩 평가로 유추할 뿐이므로, 실기기 검증을 생략하지 않는다.
- **시뮬레이터·에뮬레이터를 모델에게 조작시킬 때.** OpenAI의 OSWorld 2.0(오프라인 세트) 수치는 72.6%, 작업당 약 40분(GPT-5.6 Sol은 65.7%, 약 75분)이다. 속도 비교는 지연 시뮬레이션이고, 독립 테스트(ARC Prize)는 헤드라인 수치가 하네스에 크게 좌우된다고 지적했다. 성공률이 72.6%라는 것은 네 건 중 한 건 가까이 실패한다는 뜻이다. [부분]
  → 화면 조작 결과는 모델의 "됐다"는 말이 아니라 스크린샷·로그·테스트 출력으로 확인한다.
- **빌드가 길고 로그가 크다.** 이 모델은 긴 자율 작업에서 세부에 매몰되고 토큰을 많이 쓴다는 평가가 있다. 빌드·테스트 출력은 파일로 한 번 저장한 뒤 실패한 구간만 읽고, 같은 빌드를 필터만 바꿔 반복하지 않는다.
- **Fast 모드에 의존하지 않는다.** Astra의 Fast 모드는 지연 SLA가 없고 EU 데이터 레지던시에서 쓸 수 없다. CI·릴리즈 절차의 시간 제한을 Fast 모드에 맞춰 잡지 않는다. [확인]
- **승인 필요 동작은 전역 지침 목록뿐이다.** 서명 키 접근, 스토어 제출, 배포, 외부 전송은 사용자 승인 전에 하지 않는다. 그 밖의 읽기·편집·로컬 빌드는 묻지 않고 진행한다.
- **스토어 정책은 기억하지 않는다.** §1.2 표의 날짜와 요건은 작업 시점에 공식 문서로 다시 확인한다. 이 모델이 아는 값이 기준일 이후와 다를 수 있다.
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
- API 규칙: [openai/codex 마이그레이션 가이드](https://raw.githubusercontent.com/openai/codex/main/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-6-astra.md) [확인]
- 컴퓨터 사용 수치: [OpenAI 발표 페이지](https://openai.com/index/gpt-6-astra/) 검색 스니펫, [CryptoBriefing 요약](https://cryptobriefing.com/openai-gpt-6-astra-computer-use-agents/) [부분: 벤더 수치를 2차 출처가 재인용]
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: gpt-6-2-astra 모델 페이지](https://artificialanalysis.ai/models/gpt-6-2-astra)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [GPTunneL: GPT-6.2 Astra·Sol 후기 모음](https://www.gptunnel.ru/en/blog/gpt-6-2-astra-sol-reviews)
- 추가 확인(2026-11-19 웹 검색): [Android Headlines: GPT-6.2 Astra·Sol 출시 평가](https://www.androidheadlines.com/2026/11/openai-gpt-6-2-astra-sol-release-reviews.html)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [HumanLayer: SlopCodeBench 2026-10 (독립 벤치마크)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: GPT-6.2 Astra·Sol 스레드](https://news.ycombinator.com/item?id=50535230)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Claude Opus 5.5 스레드](https://news.ycombinator.com/item?id=49803892)
- 한계: 모바일 개발에 대한 근거가 없어 이 문서의 모델별 권고는 일반 특성에서 끌어온 것이다. 이 모델로 앱 작업을 해 보고 실제로 겪은 실패를 §2에 추가한다.
