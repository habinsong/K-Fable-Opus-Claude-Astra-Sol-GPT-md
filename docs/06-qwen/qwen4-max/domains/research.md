# Qwen4-Max · 연구 — 조사 기록
> 제공자: Alibaba(Qwen) · 모델 ID: 미공개 [미확인] (보도자료 표기 `Qwen4-Max`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/06-qwen/qwen4-max/research.md`](../../../../md/06-qwen/qwen4-max/research.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/research.md`](../../../_common/domain-rules/research.md)

## 2. 이 모델의 연구 작업 운용
Qwen4-Max 전용 연구 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 첫 답 토큰까지 148.6초(중앙값 12.6초). 검색 도구 호출이 여러 번 이어지는 조사에서는 대기 시간이 누적된다.
- 독립 지수 43은 비교군 중앙값과 같다. 추론 집약 조사의 정확도 우위를 가정하지 않는다.
- 입력 $1.50 / 출력 $4.50, 블렌디드 $0.80. 출력 토큰이 많아(1.27억) 작업당 비용은 단가만으로 계산할 수 없다.

**연구 작업에서 따로 확인할 것**
- 논문 인용의 실재 여부, 통계 수치 처리, 가설과 사실의 구분를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 연구 작업 성능으로 읽지 않는다. [추정]
- **제작사가 내놓은 비교표만으로 판단하지 않는다.** 같은 과제로 직접 비교한다. [부분: 독립 평가 없음]
- **제작사 발표보다 낮게 본다.** 독립 지수가 같은 급 중앙값과 같고 느리고 출력이 길다. 시간·토큰 상한을 둔다. [확인: Artificial Analysis 모델 페이지]
- **사실 질문에서 모르면 기권하는 편이다.** 기권을 오류로 취급하지 말고, 그래도 인용과 수치는 원문으로 확인한다. 사실 질문 기준 오답 비율이 28.4%다. [부분: 독립 측정을 옮긴 집계 페이지]

## 4. 근거와 한계
- [Alibaba 보도자료: Qwen4-Max](https://www.alibabacloud.com/press-room/alibaba-unveils-qwen4-max)
- [Artificial Analysis: Qwen4 Max](https://artificialanalysis.ai/models/qwen4-max)
- 추가 확인(2026-11-19 웹 검색): [Cellcog: Qwen4-Max](https://cellcog.ai/blog/qwen-4-release-date/)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: qwen4-max 모델 페이지](https://artificialanalysis.ai/models/qwen4-max)
- 추가 확인(2026-11-19 웹 검색): [BenchLM: AA-Omniscience 환각률(2026-11-19, Artificial Analysis 수치를 옮긴 미러)](https://benchlm.ai/benchmarks/omnisciencehallucinationrate)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 연구 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
