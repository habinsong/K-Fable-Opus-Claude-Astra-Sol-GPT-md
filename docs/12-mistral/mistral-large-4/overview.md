# Mistral Large 4 — 개요·사양·라이선스
> 제공자: Mistral AI · 모델 ID: `mistral-large-4-0`(문서 링크 표기, 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/12-mistral/mistral-large-4/general.md`](../../../md/12-mistral/mistral-large-4/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 사양
- Mistral AI의 플래그십이다(애칭 "Le Chonk"). 이 저장소에서 "Mistral Large"는 현재 최신인 Large 4로 해석했다. **출시일이 출처마다 다르다**: 공개 미리보기 2026-10-06(2차 보도), Artificial Analysis FAQ 2026-10-29, Mistral 문서 목록의 버전 `v26.10`·날짜 2026-11-05. 가중치 공개일도 2026-10-27 또는 10-29로 갈린다. [확인: 문서·지표 사이트 / 충돌: 날짜]
- 총 1.05조(Artificial Analysis는 1.1조) MoE, 토큰당 활성 520억(활성 비율 약 5.0%, 계산), 비전 인코더 16억이 별도다. 입력은 텍스트·이미지, 출력은 텍스트다. 추론 모델이다. [확인: Mistral 문서·Artificial Analysis]
- 컨텍스트 100만 토큰(Mistral 문서·Artificial Analysis). 이 저장소가 읽은 2차 정리 중에는 미리보기 API가 51만 2천 토큰까지만 열렸다거나 Artificial Analysis가 524,288로 적었다는 서술도 있었다. 최대 출력은 문서에 없고 OpenRouter 항목은 262,144 완료 토큰을 적었다는 2차 서술이 있다. [확인 / 충돌]
- **가격**(100만 토큰당): 입력 $0.70 / 캐시 입력 $0.07 / 출력 $2.10(Mistral 문서). 블렌디드 $0.40, 캐시 할인 90%. 미리보기 정가는 $1.36/$4.18이었고 출시 할인이 약 절반이라는 2차 서술이 있다. [확인: 문서·Artificial Analysis / 부분: 미리보기 가격]
- **라이선스**: Mistral Ecosystem Open-Weight License. 상업 사용은 되지만 서비스형 모델(MaaS) 사업자는 별도 라이선스가 필요하다는 서술이 있다. 가중치는 Hugging Face에 있다. [확인: 이름 / 부분: 조항]
- 기능: 구조화 출력, 함수 호출, 문서 질의, 접두 입력, Chat Completions, 대화(conversations), 배치, 에이전트, 내장 도구. [확인: Mistral 문서]
