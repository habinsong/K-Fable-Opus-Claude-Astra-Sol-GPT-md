# Qwen4-Max · 웹 리서치 — 조사 기록
> 제공자: Alibaba(Qwen) · 모델 ID: 미공개 [미확인] (보도자료 표기 `Qwen4-Max`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/06-qwen/qwen4-max/web-research.md`](../../../../md/06-qwen/qwen4-max/web-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web-research.md`](../../../_common/domain-rules/web-research.md)

## 2. 이 모델의 웹 리서치 작업 운용
Qwen4-Max 전용 웹 리서치 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 첫 답 토큰까지 148.6초(중앙값 12.6초). 검색 도구 호출이 여러 번 이어지는 조사에서는 대기 시간이 누적된다.
- 독립 지수 43은 비교군 중앙값과 같다. 추론 집약 조사의 정확도 우위를 가정하지 않는다.
- 입력 $1.50 / 출력 $4.50, 블렌디드 $0.80. 출력 토큰이 많아(1.27억) 작업당 비용은 단가만으로 계산할 수 없다.

**웹 리서치 작업에서 따로 확인할 것**
- 검색 도구의 인용 정확도, 출처 날조 빈도, 긴 조사에서의 일관성를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 웹 리서치 작업 성능으로 읽지 않는다. [추정]

## 4. 근거와 한계
- [Alibaba 보도자료: Qwen4-Max](https://www.alibabacloud.com/press-room/alibaba-unveils-qwen4-max)
- [Artificial Analysis: Qwen4 Max](https://artificialanalysis.ai/models/qwen4-max)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 웹 리서치 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
