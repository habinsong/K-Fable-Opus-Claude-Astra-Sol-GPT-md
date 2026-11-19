# Muse Ember · 연구 — 조사 기록
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-ember-1.0`(2차 보도 표기, 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/10-muse/muse-ember/research.md`](../../../../md/10-muse/muse-ember/research.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/research.md`](../../../_common/domain-rules/research.md)

## 2. 이 모델의 연구 작업 운용
Muse Ember 전용 연구 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 독립 지수 36(`max`)이고 작업당 $0.14다. 대량 추출·분류에는 비용이 맞지만 사실 정확성이 중요한 조사에는 점수가 낮다.
- 출력 토큰이 많아(1.15억) 짧은 조사에서도 장황할 수 있다. 출력 길이를 명시한다.
- 입력 모달리티(텍스트·이미지 대 +오디오·비디오)가 출처마다 달라 비디오·오디오 처리를 가정하지 않는다.

**연구 작업에서 따로 확인할 것**
- 논문 인용의 실재 여부, 통계 수치 처리, 가설과 사실의 구분를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 연구 작업 성능으로 읽지 않는다. [추정]
- **사실 질문에서 모르면 기권하는 편이다.** 기권을 오류로 취급하지 말고, 그래도 인용과 수치는 원문으로 확인한다. 사실 질문 기준 오답 비율이 17.4%다. [부분: 독립 측정을 옮긴 집계 페이지]

## 4. 근거와 한계
- [Artificial Analysis: Muse Ember](https://artificialanalysis.ai/models/muse-ember)
- [Let's Data Science: Muse Ember](https://letsdatascience.com/news/meta-releases-muse-ember-a-low-cost-model-for-agent-executio-7b564cff)
- 추가 확인(2026-11-19 웹 검색): [BenchLM: AA-Omniscience 환각률(2026-11-19, Artificial Analysis 수치를 옮긴 미러)](https://benchlm.ai/benchmarks/omnisciencehallucinationrate)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 연구 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
