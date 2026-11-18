# Qwen4-Max · 앱 — 조사 기록
> 제공자: Alibaba(Qwen) · 모델 ID: 미공개 [미확인] (보도자료 표기 `Qwen4-Max`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/06-qwen/qwen4-max/app.md`](../../../../md/06-qwen/qwen4-max/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
Qwen4-Max 전용 앱 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 컨텍스트 100만(Alibaba) 또는 984K(Artificial Analysis), 최대 출력 미확인. 입력 $1.50 / 출력 $4.50(100만 토큰당).
- 독립 지수 43(92개 중 47위)이고 지수 한 작업에 32.3분, 출력 1.27억 토큰, 작업당 $3.27이다. 지연에 민감한 반복 루프에는 맞지 않는다.
- Alibaba는 Code Arena 6위를 내세우지만 점수·하네스가 공개되지 않았다. [부분]

**앱 작업에서 따로 확인할 것**
- 모바일·데스크톱 빌드·서명 도구와의 호환, 긴 세션의 비용, 화면 입력 이해를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 앱 작업 성능으로 읽지 않는다. [추정]

## 4. 근거와 한계
- [Alibaba 보도자료: Qwen4-Max](https://www.alibabacloud.com/press-room/alibaba-unveils-qwen4-max)
- [Artificial Analysis: Qwen4 Max](https://artificialanalysis.ai/models/qwen4-max)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 앱 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
