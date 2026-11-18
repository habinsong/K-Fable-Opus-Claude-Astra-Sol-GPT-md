# Muse Ember — 개요·사양·라이선스
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-ember-1.0`(2차 보도 표기, 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/10-muse/muse-ember/general.md`](../../../md/10-muse/muse-ember/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 사양
- Meta Superintelligence Labs의 Muse 계열에서 가장 가볍고 비용 효율이 높은 모델이다. 2026-11-09에 공개됐고(Spark, 오픈 가중치 Glimmer, Wonder에 이은 네 번째 Muse 모델) 큰 모델(Wonder)이 계획하고 Ember가 파일 읽기·테스트 실행·국소 수정 같은 하위 작업을 맡는 구성을 겨냥한다. 모델 ID는 `muse-ember-1.0`이라는 보도가 있다. [확인: 날짜·위치 / 부분: ID]
- **가격**(100만 토큰당): 입력 $0.10 / 출력 $0.50, 블렌디드 $0.0728, 캐시 할인 96%. Muse Wonder($4/$20)의 40분의 1(계산). 컨텍스트 1M. [확인: Artificial Analysis 읽은 값]
- 입력은 Artificial Analysis가 텍스트·이미지, Meta 발표를 전한 보도가 텍스트·이미지·오디오·비디오로 적어 서로 다르다. 출력은 텍스트다. 폐쇄형이고 파라미터 수는 비공개다. 제공 경로는 Meta Model API와 Muse Code다. [확인/충돌]
- 추론 모델이고 `max`와 `xhigh` 단계가 측정됐다. [확인: Artificial Analysis]
