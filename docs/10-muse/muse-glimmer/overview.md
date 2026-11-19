# Muse Glimmer — 개요·사양·라이선스
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-glimmer`(Meta 오픈 가중치 30B) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/10-muse/muse-glimmer/AGENTS.md`](../../../md/10-muse/muse-glimmer/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 사양
- Meta의 오픈 가중치 모델이고 Llama 4 이후 16개월 만의 오픈 릴리즈다. 2026-08-10. **Apache 2.0**(Llama 라이선스의 월간 사용자 상한이 없다). Meta API로는 제공하지 않고 제3자 공급자가 가격·속도를 정한다. 학습 데이터는 공개하지 않아 오픈 가중치이지 완전한 오픈 소스가 아니다. [확인: Artificial Analysis 기사 직접 읽음]
- 30B 밀집 모델이고 비전 인코더 약 1.8B를 포함한다. 슬라이딩 윈도우 3층마다 전역 1층인 하이브리드 어텐션. 컨텍스트 128K(확장 전)에 확장을 더했다. Kimi K2.5(1T)의 약 33분의 1(계산). [확인]
- **메모리**: BF16 약 60 GB, 4비트 약 18 GB, KV 캐시는 128K에서 최소 약 1.8 GB. 128K 전체가 H100 한 장(BF16) 또는 고사양 MacBook·RTX 5090(4비트)에 들어간다. Meta 양자화 판: K-Quant-Dynamic(32GB 대상, 15개 벤치마크 평균 정확도 하락 0.2%), K-Quant-17GB(24GB 대상, 1%). 자체 추측 디코딩 초안을 동봉한다. [확인 / 부분: 정확도 하락은 Meta 주장]
- 런타임: 출시 당일 llama.cpp·MLX·vLLM·SGLang·Ollama·LM Studio 지원, Ollama 0.32.7 이상. [부분: 2차 정리]
