# Raon-1 mini (preview) — 비판적 평가·쓸 때와 쓰지 않을 때
> 제공자: Krafton · 모델 ID: `KRAFTON/Raon-1-mini-preview` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/25-krafton/raon-1-mini/AGENTS.md`](../../../md/25-krafton/raon-1-mini/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.4 비판적 평가
- **같은 크기대 비교에서 지식은 약하고 한국어 대화는 강하다.** MMLU-Pro 76.5(Qwen3.6-35B-A3B 85.9, Gemma 4 26B-A4B 82.9), HMMT 84.1(84.5), GPQA-Diamond 84.3(83.2로 앞섬), IFBench 84.2(66.6 / 80.9)로 앞서고 "Chatbot Korean" 92.9가 최고다(74.5 / 90.6, 사내 평가·비공개). [확인: 읽은 값, 벤더 보고]
- **에이전트·도구 지표가 약하다.** Terminal-Bench Lite 47.0(Qwen3.6 63.3, Gemma 4 52.0), BFCL v4 59.8(64.7 / 65.8), AutomationBench 29.7(공개 분할, Gemma 36.2), AA-LCR 67.3(69.3). 반면 SWE-Verified 70.8(63.2 / 61.6)과 BrowseComp Plus 55.7(34.8 / 32.2)은 앞선다. [확인: 읽은 값]
- **참고용으로 표에 넣은 밀집 모델에는 진다.** Qwen3.8-27B는 SWE-Verified 74.6, AIME 2026 98.8, BrowseComp Plus 58.0이고 Muse Glimmer 30B는 SWE-Verified 72.0, Terminal-Bench Lite 70.7이다. [확인: 읽은 값]
- **심판 모델이 GPT-5.6 Luna다.** 평가자 편향 가능성이 있다. 한국어 사내 평가는 방법·데이터가 공개되지 않았다. [확인: 카드 서술 / 추정]
- **프리뷰라 변동 가능하고 접근이 게이트다.** [확인]

#### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: RTX 5090급 개인 장비에서 한국어 대화·지시 수행이 중요한 로컬 모델을 시험할 때.
- 쓰지 않는다: 도구 호출·터미널 에이전트 기본 모델, 최종 사양이 필요한 구축(프리뷰).

## 재확인 (2026-11-19, 웹 검색, 사용자·후기 글)
- 독립된 사용자 후기를 찾지 못했다. 검색에 나온 것은 제조사 발표·출시 보도·판매 사이트 정리뿐이다. [확인: 부재] RTX 5090 실측 후기도 없다.
- [llmrun.dev](https://llmrun.dev/model/krafton-raon-1-mini-preview): Q4_K_M GGUF 19.69GB(추정치). MindStudio 가이드는 NVFP4 단일 5090 구성을 되풀이하고 표준·MXFP8 판은 단일 소비자 GPU용이 아니라고 적었다. 두 곳 모두 Krafton 서술을 옮긴 것이다. [부분] ([MindStudio](https://www.mindstudio.ai/blog/run-raon-1-mini-locally-rtx-5090))
- 정식 출시 전 프리뷰이고 Krafton이 성능 문제를 다듬어 가며 업데이트하겠다고 밝혔다. [확인: 보도]
