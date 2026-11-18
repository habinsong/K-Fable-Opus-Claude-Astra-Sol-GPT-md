# Nemotron 3.5 Super VL — 개요·사양·라이선스
> 제공자: NVIDIA · 모델 ID: `nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16`(Hugging Face), `nvidia/nemotron-3.5-super-vl`(OpenRouter) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/14-nvidia/nemotron-3.5-super-vl/general.md`](../../../md/14-nvidia/nemotron-3.5-super-vl/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 사양
- NVIDIA의 오픈 비전-언어 모델이다. 2026-10-15 공개됐다. 같은 날 Bolt 74B-A9B(2비트 양자화로 24GB, 10-16부터 RTX Spark 노트북)와 Bolt E4B(4GB, 10-23)가 함께 발표됐고 Lightning(8월)·Ultra는 별도 라인업이다. [확인: NVIDIA 블로그·모델 카드 직접 읽음]
- **120B 총, 12B 활성**(활성 비율 10%, 계산). Mamba-2와 Transformer를 섞은 하이브리드 MoE이고 MoE 층마다 라우팅 전문가 512개, C-RADIO 비전 인코더를 쓴다. 컨텍스트 최대 100만 토큰(배포 레시피에 따라 더 작은 창). Hugging Face BF16 저장소 이름은 120B-A12B이고 한 2차 서술은 124B로 적었다. [확인: 모델 카드 / 충돌: 124B]
- 입력: 텍스트, 이미지(JPEG·PNG), 비디오(MP4, 최대 2분). 출력은 텍스트. 이미지·웹페이지·PDF에서 OCR·표·차트에 강하다고 한다. [확인: 모델 카드]
- **라이선스**: OpenMDW-1.1(OpenMDW License Agreement 1.1). 가중치·데이터셋·학습 레시피를 공개한다. 학습: 사전·연속 사전 학습 약 26조 토큰, 후학습 약 380만 샘플과 수십 개 환경의 강화 학습. [확인: 블로그·모델 카드]
- **하드웨어**: H100 4장 또는 GB200 2장(Linux, Hopper·Blackwell). vLLM(`v0.32.0`)·SGLang 레시피가 있다. 권장 샘플링은 텍스트 온도 1.0·top_p 0.95, 비전 0.6·0.95이고 추론은 `enable_thinking`으로 켠다(중간 effort 옵션 있음). 추론 토큰과 답은 `max_tokens`를 공유한다. 네이티브 MTP(다중 토큰 예측)로 초안 토큰 5개를 쓴다. [확인: 모델 카드]
- **가격/제공**: NVIDIA NIM, OpenRouter(`nvidia/nemotron-3.5-super-vl`), ModelScope, 양자화판(NVFP4, GGUF). 토큰 단가는 확인하지 못했다. [부분]
