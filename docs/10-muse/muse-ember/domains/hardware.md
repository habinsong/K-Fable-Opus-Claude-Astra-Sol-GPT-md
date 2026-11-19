# Muse Ember · 하드웨어 — 조사 기록
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-ember-1.0`(2차 보도 표기, 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/10-muse/muse-ember/hardware.md`](../../../../md/10-muse/muse-ember/hardware.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/hardware.md`](../../../_common/domain-rules/hardware.md)

## 2. 이 모델의 하드웨어 작업 운용
Muse Ember 전용 하드웨어 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 컨텍스트 1M, 입력 $0.10 / 출력 $0.50(100만 토큰당), 캐시 할인 96%. 출력 속도 459 tok/s(`max`), 지수 한 작업 3.1분.
- 독립 지수 36(`max`)은 Wonder 44, Hydrogen 51, GPT-6.2 Sol 57보다 낮다. 국소 수정·반복 하위 작업용으로 보고 설계 작업에는 쓰지 않는다. [추정]
- Meta는 큰 모델이 계획하고 Ember가 파일 읽기·테스트 실행·국소 수정을 맡는 구성을 권한다. [부분]

**하드웨어 작업에서 따로 확인할 것**
- 데이터시트·회로도 입력의 정확도, HDL 시뮬레이션 루프, 수치·단위 환각 빈도를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 하드웨어 작업 성능으로 읽지 않는다. [추정]
- **사실 질문에서 모르면 기권하는 편이다.** 기권을 오류로 취급하지 말고, 그래도 인용과 수치는 원문으로 확인한다. 사실 질문 기준 오답 비율이 17.4%다. [부분: 독립 측정을 옮긴 집계 페이지]

## 4. 근거와 한계
- [Artificial Analysis: Muse Ember](https://artificialanalysis.ai/models/muse-ember)
- [Let's Data Science: Muse Ember](https://letsdatascience.com/news/meta-releases-muse-ember-a-low-cost-model-for-agent-executio-7b564cff)
- 추가 확인(2026-11-19 웹 검색): [BenchLM: AA-Omniscience 환각률(2026-11-19, Artificial Analysis 수치를 옮긴 미러)](https://benchlm.ai/benchmarks/omnisciencehallucinationrate)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 하드웨어 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
