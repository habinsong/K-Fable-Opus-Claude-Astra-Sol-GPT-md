# Muse Wonder — 개요·사양·라이선스
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-wonder-1.0`(한 출처의 표기, 확인 필요), 상위 변형 Wonder Full은 `muse-wonder-full-1.0`(카탈로그 전용, 한 출처의 표기) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/10-muse/muse-wonder/general.md`](../../../md/10-muse/muse-wonder/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 접근 경로
- **2026-10-12**에 Meta가 공개한 Muse 계열 최상위 모델이다. 개인·전문 업무용 에이전트를 내세운다. 2026-04 Muse Spark, 2026-09 개인용 Muse 에이전트에 이어 나왔다.
- **두 모델이 있고 접근 경로가 다르다.** Muse Wonder는 Meta Model API와 Muse Code(Meta의 터미널 코딩 에이전트)에서 쓰고, **Wonder Full은 Muse Code 구독자(Power Usage 또는 Maximum Usage 요금제)만** 쓴다. 공개 API는 Wonder만 제공한다. 따라서 Wonder Full의 벤치마크 헤드라인은 지금 호출할 수 없는 모델을 설명할 수 있다. Muse 앱에도 순차 적용된다고 하나 일정은 없다. [부분]
- 모델은 폐쇄형이며 가중치를 받을 수 없다. 모델 카드가 구조·학습에 관해 알려 주는 정보가 거의 없다는 지적이 있다. [부분]

#### 2.2 사양 (출처마다 다를 수 있음)
- 컨텍스트 100만 토큰, 장시간 에이전트·컴퓨터 사용을 겨냥. 가격은 Meta Model API에서 입력 $4 / 출력 $20 (100만 토큰당)이다. 한 매체는 Opus 5.5와 비슷한 가격대인데 벤치마크에서는 뒤처진다고 보도했다. [부분]
- **Active Memory**(대화를 넘어 맥락을 유지하고 관련 정보를 다시 꺼냄)와 **Active Focus**(긴 작업에서 대안을 시도하고, 막히면 우회하고, 중대한 행동 전에 확인 질문을 함)가 Meta가 내세운 두 기능이다. 두 기능이 API에서 어떻게 노출되는지, Active Memory가 데이터를 어디에 얼마나 보관하는지는 찾지 못했다. [미확인]
- 노력 단계: 벤치마크 대부분이 `max` 단계의 값이다(Wonder Full의 SWE-Marathon만 `xhigh`). 일반 제공 단계와 다를 수 있다. [부분]

## 재확인 (2026-11-19, 웹 검색)
- 2026-10-12 이후 새 Muse 모델 발표는 찾지 못했다. Muse Spark Open(2026-10-15, 총 8,160억 파라미터 오픈 가중치)은 `muse-spark` 폴더가 다룬다. [부분: [딥러닝닷AI The Batch](https://www.deeplearning.ai/the-batch/meta-releases-wonder-opens-spark)]

## 재확인 (2026-11-19, Artificial Analysis 직접 읽기)
- [Artificial Analysis: Muse Wonder](https://artificialanalysis.ai/models/muse-wonder) 값: 지수 **44(`max`, 92개 중 44위)**, 41(`high`). 출력 속도 120 / 130 tok/s, 첫 답 토큰 19.7 / 9.6초, 지수 한 작업 13.3 / 8.7분, 지수 한 번에 출력 1.13억 / 7,280만 토큰. 가격 입력 $4 / 출력 $20(블렌디드 $2.94, 캐시 할인 95%), 작업당 비용 $6.95. 컨텍스트 1M, 입력 텍스트·이미지·음성·비디오, 출력 텍스트, 출시일 2026-10-12, 폐쇄형. [확인: 읽은 값, 측정은 제3자]
- 같은 페이지의 다른 Meta 모델: Muse Wonder Full 50, Muse Ember 36, Muse Spark Open 25, Muse Glimmer 6. [확인: 읽은 값]
- **이 문서 §2.x에 적힌 이전 점수(Wonder 52, Wonder Full 56)와 지금 읽은 값(44, 50)이 다르다.** 지수 버전이 갱신됐거나 effort 기준이 달라졌을 가능성이 있으나 확인하지 못했다. 점수를 인용할 때 읽은 날짜를 적는다. [미확인]
- 2026-11-09에 더 작고 싼 Muse Ember가 나왔다. 큰 모델이 계획하고 Ember가 하위 작업을 맡는 구성을 Meta가 겨냥한다. Ember는 `docs/10-muse/muse-ember/`에서 다룬다. [부분]
