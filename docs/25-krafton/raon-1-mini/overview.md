# Raon-1 mini (preview) — 개요·사양·라이선스
> 제공자: Krafton · 모델 ID: `KRAFTON/Raon-1-mini-preview` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/25-krafton/raon-1-mini/AGENTS.md`](../../../md/25-krafton/raon-1-mini/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 사양
- Krafton AI의 오픈 가중치 MoE 프리뷰다. 2026-10-21 공개(보도 날짜). 가중치와 설정은 Apache 2.0, 호스팅 API·플레이그라운드는 별도 약관. 저장소는 접근 요청이 필요한 게이트다. "프리뷰이며 최종 버전 전에 사양과 결과가 바뀔 수 있다"고 카드가 밝혔다. [확인: GitHub README 직접 읽음]
- 총 28.8B(제목 표기 30B-A4B), 토큰당 활성 4.3B(활성 비율 약 14.9%, 계산). 25층 중 18층이 Raon Delta Attention(RDA, 선형·고정 크기 상태)이고 7층이 Gated MLA(KV 캐시)로 3:1이다. 은닉 2,560, 헤드 40개, 라우팅 전문가 128개(라우팅 6 + 공유 1 활성), 전문가 중간 크기 1,088, 어휘 259,840, NoPE, Raon-mHC 잔차(4 스트림). 컨텍스트 262,144, KV 캐시는 BF16 토큰당 약 8 KiB. [확인]
- 텍스트 전용이다(PDF는 사전 OCR). 변형: MXFP8 기반, NVFP4, GGUF(Q4_K_M), MLX, 추측 디코딩용 DFlash2 초안 모델. [확인]
- 권장 샘플링: 온도 1.0, top_p 0.95, top_k 20, min_p 0, presence_penalty 일반 1.5 / 코딩·수학 0, 추론 모드 권장. [확인]
