# Inkling 2 Small — 개요·사양·라이선스
> 제공자: Thinking Machines Lab · 모델 ID: `inkling-2-small`(Cloudflare 표기) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/17-thinking-machines/inkling-2-small/AGENTS.md`](../../../md/17-thinking-machines/inkling-2-small/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 사양
- Thinking Machines Lab의 2세대 모델이다("Small"이라는 이름이지만 소형이 아니다). 2026-11-05 공개(Tinker 제공)했고 **2026-11-12에 가중치가 Hugging Face에 올라왔다**(블로그 갱신). 라이선스는 Apache 2.0이다. 1세대 Inkling Small보다 전반적으로 낫고 특히 장시간 자율 작업이 낫다고 한다. [확인: 공식 블로그 직접 읽음]
- 총 5,940억 파라미터 MoE, 토큰당 활성 170억(활성 비율 약 2.9%, 계산). Cloudflare는 활성 180억으로 적는다. 비전 인코더 2.92억(Perception Encoder 기반). 입력은 텍스트·이미지, 오디오는 지원하지 않는다. [확인: 블로그 / 충돌: 활성 수]
- 컨텍스트: 블로그는 단일 수치를 적지 않았다. 강화 학습 256K, 사전 학습 2단계 512K, 3단계 1M으로 학습했고 평가의 궤적 한도는 1M 토큰이다(1세대는 256K). Cloudflare 목록은 1,048,576 토큰이다. [확인: 학습·평가 / 부분: Cloudflare]
- **가격**(100만 토큰당): Cloudflare Workers AI 입력 $0.30 / 출력 $1.00. Thinking Machines 페이지에는 토큰 단가가 없다. 제공 경로: Tinker(추론·샘플링·미세조정), NVIDIA, Fireworks, Together, Baseten, Nebius, Modal, Cloudflare, Snowflake Cortex. [확인: 블로그 제공 목록 / 부분: 가격]
- 학습 규모: 사전 학습 1단계 8.4조 토큰(NVIDIA GB300 NVL72에서 68시간, NVFP4), 2단계 3.8조, 3단계 약 3,200억(추론·에이전트 궤적), 4단계 약 340억. 주 강화 학습: 1,075 스텝, 롤아웃 1,700만 건 이상, 토큰 3조 이상, GPU 2,048개로 9일. 롤아웃 구성: 코딩 38.5%, 비전 13.9%, 사무·지식 업무 9.1%. [확인]
- 하드웨어: 모델 카드를 전한 보도는 NVFP4 체크포인트에 GPU 메모리 합계 500GB 이상, MXFP8에 800GB 이상이 필요하다고 적었다. [부분]
