# Mistral Large 4 · 네이티브 — 조사 기록
> 제공자: Mistral AI · 모델 ID: `mistral-large-4-0`(문서 링크 표기, 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/12-mistral/mistral-large-4/native.md`](../../../../md/12-mistral/mistral-large-4/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
Mistral Large 4 전용 네이티브 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 컨텍스트 1M, 입력 $0.70 / 출력 $2.10. `high`에서 첫 토큰까지 70.5초, 지수 한 작업 20.0분, 출력 1.07억 토큰. 반복 코딩 루프에는 느리다.
- 독립 지수 26(`high`), `medium` 23. `high`가 3점 높지만 시간이 48% 더 든다(계산). 코딩 전용 점수는 찾지 못했다. [확인: 읽은 값 / 추정]
- 함수 호출·구조화 출력·배치·에이전트 기능이 있다. [확인: Mistral 문서]

**네이티브 작업에서 따로 확인할 것**
- 메모리 안전·동시성 버그 진단 정확도, 디버거·새니타이저 출력의 해석를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 네이티브 작업 성능으로 읽지 않는다. [추정]

## 4. 근거와 한계
- [Artificial Analysis: Mistral Large 4](https://artificialanalysis.ai/models/mistral-large-4)
- [Mistral docs: Mistral Large 4](https://docs.mistral.ai/models/mistral-large-4-0)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 네이티브 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
