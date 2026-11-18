# Nemotron 3.5 Bolt 74B-A9B 24GB — 개요·사양·라이선스
> 제공자: NVIDIA · 모델 ID: `nvidia/Nemotron-3.5-Bolt-74B-A9B-24GB`(저장소 표기 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/14-nvidia/nemotron-3.5-bolt-74b-a9b/general.md`](../../../md/14-nvidia/nemotron-3.5-bolt-74b-a9b/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 사양
- NVIDIA가 2026-10-15 Nemotron 3.5 Super VL과 함께 낸 "24GB에 들어가는" 오픈 모델이다. Super VL(120B/12B)을 Star Elastic(라우터 기반 아키텍처 탐색·압축)으로 줄인 것이다. 총 74B, 활성 9B(활성 비율 약 12.2%, 계산), Mamba-Transformer 하이브리드 MoE, 전문가 top-K를 22에서 9로 낮췄다. 목록에 7일(10-07)로 적은 곳도 있다. [확인: NVIDIA 연구 페이지 직접 읽음 / 충돌: 날짜]
- **양자화 구성**: 라우팅·공유 전문가의 FC1/FC2 가중치 IQ2_XXS(원소당 2.0625비트), Mamba 선형 층 NVFP4, LM 헤드·토큰 임베딩·어텐션·Latent MoE 가중치 Q8_0. 가중치만 양자화한다. 학습은 압축 후 시각 능력 복원, 시뮬레이션 환경 종단 강화 학습, 추론·도구 사용용 마지막 RL, 양자화 인식 증류(QAD)를 거쳤다. [확인]
- **속도**: 목표 80 TPS 이상, AIPerf SPEED-Bench-Coding에서 83.99 TPS(본문 반올림 84), Surface Laptop Ultra 128GB(RTX Spark, Windows 11 ARM x64), llama.cpp. 컨텍스트는 페이지에 없고 다른 출처가 256K를 적었다. [확인: 속도 / 부분: 컨텍스트]
- **LiLiCorr 추측 디코딩 초안**(1.13B, 7토큰 초안, 수락 길이 4.68 탐욕 / 4.25 확률적). 공개 체크포인트: 24GB 모델, BF16, 24GB GGUF, 초안 모델, 초안 GGUF. 라이선스는 페이지에 없고 집계 사이트는 OpenMDW v1.1이라고 적었다. [확인 / 부분]
