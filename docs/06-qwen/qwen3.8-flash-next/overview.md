# Qwen3.8-Flash-Next — 개요·사양·라이선스
> 제공자: Alibaba(Qwen) · 모델 ID: `Qwen/Qwen3.8-Flash-Next` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/06-qwen/qwen3.8-flash-next/general.md`](../../../md/06-qwen/qwen3.8-flash-next/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 사양
- Alibaba가 Qwen4 세대 구조의 "실험적 미리보기"로 낸 오픈 가중치 모델이다. 2026-08-26(Hugging Face 컬렉션 갱신), 일부 정리는 08-24. 라이선스는 **qwen-community-1.0**(Apache 2.0이 아님, 조항은 확인 못 함). 이미지·비디오·텍스트 입력. [확인: 모델 카드 직접 읽음 / 충돌: 날짜]
- 본체 125B(전문가·어텐션·은닉), 토큰당 활성 6B(활성 비율 4.8%, 계산)에 **N-gram 임베딩 51B와 MTP 4B가 별도**다. Hub의 Safetensors 합계는 180B다. 정리에 따라 176B·180B로 갈리는 이유는 MTP 4B를 세는지에 있다. 48층, 은닉 2,560, 12개 블록 = [Gated DeltaNet → MoE] 3번 + [Qwen Sparse Attention → MoE] 1번. [확인]
- Gated DeltaNet: V 48 / QK 16 헤드, 헤드 차원 128. Qwen Sparse Attention: 질의 24 / KV 2 헤드, 헤드 차원 256, 인덱서(MQA 4 질의 + 공유 키 1), 예산 512 블록 또는 2,048 토큰. MoE: 전문가 512개(라우팅 10 + 공유 1), 전문가 차원 640, 잔차 4 분기, 어휘 248,320, N-gram 표 2,000만 항목(2-gram·3-gram, 층 2). [확인]
- 컨텍스트 262,144 → YaRN으로 1,000,000. 추론 노력 `xhigh`(기본) / `medium` / `low`. 출력은 추론 262,144, 최종 응답 131,072 권장. 권장 샘플링: 추론 모드 온도 1.0, top_p 0.95, top_k 20, presence 0.0; 비추론 모드 온도 0.7, top_p 0.80, top_k 20, presence 1.5. [확인]
