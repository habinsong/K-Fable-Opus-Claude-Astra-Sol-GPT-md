# Solar Open 2 — 비판적 평가·쓸 때와 쓰지 않을 때
> 제공자: Upstage · 모델 ID: `upstage/Solar-Open2-250B` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/20-upstage/solar-open-2/AGENTS.md`](../../../md/20-upstage/solar-open-2/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.4 비판적 평가
- **영어 지식·코딩은 DeepSeek-V4-Flash(284B/13B)와 비슷하거나 낮다.** MMLU-Pro 86.2(85.9), LiveCodeBench v6 92.4(92.3)는 앞서지만 GPQA-Diamond 86.3(88.9), HLE 28.8(32.3), SWE-Bench Verified 70.4(73.8), Terminal Bench Hard 28.3(34.1; MiMo-V2.5 41.7), τ³-banking 19.6(22.3), GDPval-AA 1128(1187)로 뒤진다. [확인: 읽은 값, 벤더 보고]
- **한국어는 가장 강하다.** CLIcK 90.7(DeepSeek-V4-Flash 89.2, GPT-5.4 mini 89.6), HAE-RAE 73.8, KBL 75.5, 사내 Ko-GDPval 86.8(DeepSeek 85.0, GPT-5.4 mini 59.4). 그러나 KMMLU-Pro 78.4는 DeepSeek 78.9보다 낮고 Ko-AIME'25 97.7도 98.0에 뒤진다. [확인: 읽은 값]
- **Solar Open 1(102B/12B) 대비 큰 도약이다.** SWE-Bench Verified 15.4에서 70.4(+55.0), HLE 11.5에서 28.8, LiveCodeBench 56.5에서 92.4, τ³-banking 7.4에서 19.6(계산). 단 같은 벤더가 고른 기준선이다. [확인: 읽은 값]
- **독립 평가가 없고 서빙 장벽이 높다.** 4×H200 이상과 포크 vLLM이 필요하다. [확인 / 미확인]

#### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 한국어 업무 평가(CLIcK·KBL·금융)가 중요한 서버급 자체 호스팅, 가중치 수정이 필요한 국내 구축.
- 쓰지 않는다: 영어 코딩 에이전트 기본 모델(SWE-Bench Verified 70.4, Terminal Bench Hard 28.3), 라이선스 표기 의무를 피해야 하는 제품.

## 재확인 (2026-11-19, 웹 검색, 사용자·후기 글)
- 독립된 사용자 후기를 찾지 못했다. 검색에 나온 것은 제조사 발표·출시 보도·판매 사이트 정리뿐이다. [확인: 부재] Reddit·LocalLLaMA 로컬 실행 후기도 없다.
- [Will It Run AI](https://willitrunai.com/models/solar-open2-250b)의 추정: Q4_K_M 권장, VRAM 약 155~182GB(페이지마다 다름), M3 Ultra 256GB에서 약 18 tok/s. 계산기 사이트의 추정이지 실측이 아니다. [부분: 추정치]
- 한 블로그는 영어 평가에서 DeepSeek V4 Flash가 SWE-Bench Verified에서 이미 앞서고 카드의 Ko-GDPval 86.8이 DeepSeek-V4-Pro 86.9와 비슷하다고 짚었고, 독립 실험실의 자체 측정은 없다고 했다. [부분] ([OrcaRouter](https://www.orcarouter.ai/blog/solar-open-2-250b-explained))
