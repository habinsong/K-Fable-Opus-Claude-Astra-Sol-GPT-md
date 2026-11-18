# Muse Glimmer — 운용
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-glimmer`(Meta 오픈 가중치 30B) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/10-muse/muse-glimmer/general.md`](../../../md/10-muse/muse-glimmer/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.2 API·배포·로컬 실행
- 24GB 카드에는 K-Quant-17GB 구성이, 32GB 환경에는 K-Quant-Dynamic이 맞다. 인용된 디코딩 속도 향상은 4비트 기준이고 벤치마크 표는 BF16 기준이라 서로 다른 조건이다. [부분]
- 공식 지시 튜닝·안전 튜닝 판이 따로 나올지는 개발자 페이지에 없다. [미확인]

#### 2.3 행동 특성과 지침 문서를 쓰는 법
- Artificial Analysis는 환각률이 높다고 측정했다(AA-Omniscience 환각률 82%, Qwen3.6 27B 49%). 사실 질의는 검색·출처로 확인하게 한다. [확인: 읽은 값]
