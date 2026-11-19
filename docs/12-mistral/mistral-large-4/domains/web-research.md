# Mistral Large 4 · 웹 리서치 — 조사 기록
> 제공자: Mistral AI · 모델 ID: `mistral-large-4-0`(문서 링크 표기, 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/12-mistral/mistral-large-4/web-research.md`](../../../../md/12-mistral/mistral-large-4/web-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web-research.md`](../../../_common/domain-rules/web-research.md)

## 2. 이 모델의 웹 리서치 작업 운용
Mistral Large 4 전용 웹 리서치 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 추론 모델이고 입력은 텍스트·이미지다. 독립 지수 26은 오픈 가중치 중앙값 23보다 3점 위다.
- 작업당 비용 $2.06(`high`). 출력이 많아(1.07억 토큰) 단가가 낮아도 비용이 줄지 않을 수 있다.
- 출시일·컨텍스트·가중치 공개일이 출처마다 달라 이 모델 관련 서술은 공식 문서로 다시 확인한다. [충돌]

**웹 리서치 작업에서 따로 확인할 것**
- 검색 도구의 인용 정확도, 출처 날조 빈도, 긴 조사에서의 일관성를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 웹 리서치 작업 성능으로 읽지 않는다. [추정]
- **사실 질문에서 모르면 기권하는 편이다.** 기권을 오류로 취급하지 말고, 그래도 인용과 수치는 원문으로 확인한다. 사실 질문 기준 오답 비율이 28.2%다. [부분: 독립 측정을 옮긴 집계 페이지]

## 4. 근거와 한계
- [Artificial Analysis: Mistral Large 4](https://artificialanalysis.ai/models/mistral-large-4)
- [Mistral docs: Mistral Large 4](https://docs.mistral.ai/models/mistral-large-4-0)
- 추가 확인(2026-11-19 웹 검색): [BenchLM: AA-Omniscience 환각률(2026-11-19, Artificial Analysis 수치를 옮긴 미러)](https://benchlm.ai/benchmarks/omnisciencehallucinationrate)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 웹 리서치 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
