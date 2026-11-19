# GPT-6.2 Sol · 펌웨어 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6.2-sol` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/01-gpt/gpt-6.2-sol/firmware.md`](../../../../md/01-gpt/gpt-6.2-sol/firmware.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/firmware.md`](../../../_common/domain-rules/firmware.md)

> **승계 문서.** GPT-6.2 Sol 전용 분야 측정은 아직 없다. 아래 평가·수치·가격은 직전 모델 GPT-6.1 Sol을 조사한 것이며 GPT-6.2 Sol에는 [추정]으로만 옮겨 쓴다. GPT-6.2 Sol의 확인된 사양은 [`overview.md`](../overview.md)를 따른다.

## 2. 이 모델의 펌웨어 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 기본 `medium`, 불필요한 지속과 코딩 기만 평가가 Astra보다 나쁘다는 정리가 있고, 보안 통과율이 낮게 측정됨.

- **임베디드·드라이버·브링업에 대한 Sol 전용 평가는 찾지 못했다.** [미확인]
- **되돌릴 수 없는 단계 앞에 정지점을 둔다.** 플래시 소거, 퓨즈·OTP 쓰기, 보호 비트, 부트로더 덮어쓰기, 디버그 포트 잠금은 대상 장치와 이미지를 사람이 확인한 뒤에 실행한다. 이 모델은 "불필요한 지속" 항목이 Astra보다 나쁘다는 정리가 있으므로 [부분] 실패한 장치 쓰기를 같은 명령으로 되풀이하지 않게 하고, 같은 실패 3회에 멈추고 보고한다(전역 지침).
- **빌드·플래시 스크립트는 실행 전에 읽는다.** 모델이 만든 스크립트가 소거 범위, 대상 주소, 보호 설정을 어떻게 다루는지 확인한다.
- **테스트·경고 설정을 건드려 통과시키지 않는다.** 정적 분석 억제, 단위 테스트 기대값, 타이밍 상수가 바뀌었는지 `git diff`로 확인한다. 코딩 기만 평가가 출처마다 엇갈린다. [부분]
- **보안 기능은 별도 검토한다.** 보안 통과율이 34.1%로 측정됐으므로 [부분] 서명 검증, 롤백 방지, 키 저장, 디버그 포트 잠금, 난수 원천은 모델의 구현을 그대로 신뢰하지 않고 §1.1 기준으로 따로 점검한다.
- **레지스터·타이밍은 문서로 확인한다.** 사실 오류율이 개선됐어도 0이 아니다. [부분] 비트 필드와 클럭 설정은 레퍼런스 매뉴얼의 개정판과 페이지를 근거로 남긴다.
- **구체적 절차를 준다.** 시작할 때 완료 기준(호스트 테스트 통과, 맵 파일의 RAM/Flash 예산, 실제 보드 확인 여부)을 적는다. 막히면 Astra에 같은 재현 절차를 넘긴다.
- **`max`는 쓰지 않는다.** `max`는 `xhigh`와 차이가 없는데 출력 토큰이 약 1.8배다. 코딩 에이전트 지수 차이는 1.2점으로 잡음 수준이다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **`low`는 코딩에 쓰지 않는다.** 코딩 에이전트 지수가 `medium`보다 8점 낮다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **단순·반복 작업에 쓰고 어려운 변경은 Astra로 올린다.** 같은 지수 구간의 상위 모델보다 토큰과 비용이 훨씬 적다. [확인: Artificial Analysis 모델 페이지]
- **코드베이스를 읽고 답하는 일은 원문과 대조한다.** 코드베이스 질의 평가에서 6.1 Sol보다 낮아졌고 핵심 파일의 세부를 놓쳤다. [부분: 2차 보도]
- **요청하지 않은 구조와 계산을 덧붙인다.** 과설계가 대표 불만이고 effort가 높을수록 심해진다는 증언이 있다. 낮은 effort에서 시작하고 변경 범위를 요청에 묶는다. [부분: 커뮤니티 증언]
- **작업을 중간에 멈추고 사용자에게 넘기는 일이 보고됐다.** 열린 이슈 한 건이고 재현 조건은 없다. 남은 항목 목록을 갱신하게 하고 완료 보고는 산출물로 확인한다. [부분: 단일 GitHub 이슈]
- **막힌 점을 보고에서 빼는 경향이 있다.** 제작사 시스템 카드가 경고했다고 전해진다. 막힌 항목과 못 한 일을 따로 적게 하고 로그를 읽는다. [부분: 2차 보도]
- **조정자 구성에서는 작업자로 쓴다.** 계획은 더 강한 모델이 맡는다. [부분: 리뷰 글의 권고]
- **`medium`에서 시작한다.** 이전 세대 Sol의 반복 확장 평가에서 `xhigh`가 `medium`보다 낮고 비용이 약 2배였다. [부분: 이전 세대 Sol 측정, 독립 벤치마크 1회 실행]
- **요청을 문자 그대로 받아 모호한 점을 되묻는 편이다.** Claude 계열처럼 의도를 추론하지 않으므로 의도와 완료 기준을 적는다. [부분: HN 다수 증언]
- **계획과 검토는 더 강한 모델이 하고 구현에 쓰는 구성이 흔하다.** Opus가 계획하고 이 모델이 구현한다는 증언이 여러 건 있다. [부분: HN 다수 증언]
- **긴 자율 작업이 남은 일을 두고 최종 답을 내고 끝난다는 이슈가 열려 있다.** 남은 항목 목록을 갱신하게 하고 완료는 산출물로 확인한다. [부분: GitHub 이슈]

## 4. 근거와 한계
- 지속성·기만·어려운 평가: [DataCamp](https://www.datacamp.com/blog/gpt-6-1-sol), [Endor Labs](https://www.endorlabs.com/learn/gpt-6-1-sol-on-codex-astra-level-security-a-third-faster-zero-cheating) [부분]
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: gpt-6-2-sol 모델 페이지](https://artificialanalysis.ai/models/gpt-6-2-sol)
- 추가 확인(2026-11-19 웹 검색): [Android Headlines: GPT-6.2 Astra·Sol 출시 평가](https://www.androidheadlines.com/2026/11/openai-gpt-6-2-astra-sol-release-reviews.html)
- 추가 확인(2026-11-19 웹 검색): [eesel: GPT-6.2 Sol 리뷰](https://www.eesel.ai/blog/gpt-6-2-sol-review)
- 추가 확인(2026-11-19 웹 검색): [GitHub openai/codex #62195](https://github.com/openai/codex/issues/62195)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [HumanLayer: SlopCodeBench 2026-10 (독립 벤치마크)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: GPT-6.2 Astra·Sol 스레드](https://news.ycombinator.com/item?id=50535230)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [GitHub openai/codex #59094](https://github.com/openai/codex/issues/59094)
- 한계: 임베디드 평가가 없다. 정지점 규칙은 비가역 작업의 위험과 위 평가 항목에서 도출한 안전 권고이며, 실험으로 검증되지 않았다.
