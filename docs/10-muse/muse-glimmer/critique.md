# Muse Glimmer — 비판적 평가·쓸 때와 쓰지 않을 때
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-glimmer`(Meta 오픈 가중치 30B) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/10-muse/muse-glimmer/general.md`](../../../md/10-muse/muse-glimmer/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.4 비판적 평가
- **독립 지수 35(`high`), 같은 사이트에서 Qwen3.6 27B(38)에 못 미치고 Gemma 4 31B(30)보다 높다.** Meta 자신의 비교 표는 Gemma 4 31B와 Qwen3.6 27B를 앞선다고 하지만 독립 측정에서는 Qwen3.6 27B보다 낮다. Llama 4 Maverick(14)에서는 크게 올랐다. 지수 버전이 다른 페이지(이전 Muse Wonder 페이지는 Glimmer 6으로 표기)와 맞지 않는다. [확인: 읽은 값 / 충돌]
- **Qwen3.6 27B와의 세부 비교(AA).** GDPval-AA v2 953 대 1141, Terminal-Bench v2.1 52% 대 61%, AA-Omniscience 환각률 82% 대 49%(낮을수록 좋음), τ³-Banking 24% 대 17%(앞섬). MMMU-Pro 74%, AA-Omniscience Index -33. [확인: 읽은 값]
- **Meta·Raon·Qwen 모델 카드에서 서로 다르게 읽힌다.** Raon-1 mini 카드는 Glimmer 30B를 SWE-Verified 72.0, GPQA-Diamond 82.6, Terminal-Bench Lite 70.7, IFBench 78.7로 적는다. Qwen3.8-27B 카드는 SWE-bench Pro 51.2, Terminal Bench 2.1 51.7이다. 같은 모델이 하네스에 따라 다른 값을 받는다. [확인: 두 모델 카드]
- **Qwen3.8-27B(Apache 2.0)가 같은 크기에서 대체로 앞선다.** SWE-bench Pro 61.7 대 51.2, Terminal Bench 2.1 73.0 대 51.7. 로컬 기본 후보로는 Qwen3.8-27B가 우선이다. [확인: 읽은 값]

#### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: Apache 2.0 오픈 가중치 30B가 필요하고 24~32GB 환경에서 Meta의 양자화 판을 쓰려는 경우, 멀티모달(비전) 입력.
- 쓰지 않는다: 환각에 민감한 사실 질의, 코딩·터미널 에이전트의 기본 모델(Qwen3.8-27B가 앞선다).

## 재확인 (2026-11-19, 웹 검색, 사용자·후기 글)
- **환각이 가장 큰 약점으로 반복 지적된다.** Artificial Analysis의 AA-Omniscience 환각률 82%(Qwen3.6 27B 49%). 리뷰들은 환각 통제·지식 보정을 상대적 약점으로 꼽는다. 코딩은 Qwen3.6-27B가 더 어려운 코딩·컴퓨터 사용 벤치마크에서 앞선다는 평(SWE-Bench Verified Glimmer 76.0 대 Qwen 77.2는 Meta 표). LM Studio 최소 시스템 메모리 26GB. 개인 사용자 Reddit 후기는 찾지 못했다. [부분] ([aitoolsreview](https://aitoolsreview.co.uk/insights/meta-muse-glimmer), [LM Studio](https://lmstudio.ai/models/meta/muse-glimmer), [layer3labs](https://www.layer3labs.io/guides/muse-glimmer-review))
