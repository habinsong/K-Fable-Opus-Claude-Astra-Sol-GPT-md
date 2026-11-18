# Tencent Hy4 — 운용
> 제공자: Tencent(Hunyuan) · 모델 ID: `tencent/hy4`(OpenRouter 표기) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/15-tencent/hy4/general.md`](../../../md/15-tencent/hy4/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.2 API·하네스를 직접 만들 때
- OpenRouter의 `tencent/hy4`가 지원하는 매개변수: `max_completion_tokens`, `max_tokens`, `reasoning`, `reasoning_effort`, `response_format`, `stop`, `temperature`, `tool_choice`, `tools`, `stream`. 값의 형식은 문서로 확인한다. [확인: 읽은 값]
- 응답 속도: OpenRouter 3일 창 기준 중앙값 약 63 tok/s, 첫 토큰 약 2.9초, 가용성 99.87%라는 보고가 있다. 출시 첫날 사용자는 60~70 tok/s를 "빠르지 않다"고 평했다. Tencent는 수요 초과로 추론 클러스터를 10배로 늘렸다고 하지만 피크 시간대에 한도가 부족할 수 있다. [부분]
- 외부 서비스(Tencent Cloud)로 가는 요청이다. 개인정보·영업비밀·미공개 코드·키는 보내지 않는다.

#### 2.3 행동 특성과 지침 문서를 쓰는 법
- Tencent는 Hy4가 최상위 폐쇄형 모델에 못 미치는 영역으로 연구 수준 수학과 장시간 코딩을 인정했다. 큰 저장소 전체를 건드리는 변경과 고난도 수학은 한계를 보고한다. [부분: 벤더 서술]
- 환각 감소: Tencent 내부 검색 평가에서 환각률이 15.76%에서 5.45%로, 추측 오류율이 23.1%에서 5.6%로 줄었다고 한다. 내부 평가이고 이전 모델(미리보기) 대비다. [부분, 벤더 주장]
