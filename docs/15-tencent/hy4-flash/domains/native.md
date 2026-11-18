# Tencent Hy4 Flash · 네이티브 — 조사 기록
> 제공자: Tencent(Hunyuan) · 모델 ID: 미공개 [미확인] (보도자료 표기 `Hy4 flash`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/15-tencent/hy4-flash/native.md`](../../../../md/15-tencent/hy4-flash/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
Tencent Hy4 Flash 전용 네이티브 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 컨텍스트 최대 1M, 총 2,240억(활성 120억), 디코딩 150 tok/s 초과(벤더). 입력 $0.07 / 출력 $0.281(100만 토큰당).
- 숫자 벤치마크가 없다. 슬라이드 편집 시험에서 Flash 74.0 대 Hy4 78.9(Tencent 시험). 코딩 능력은 직접 시험해야 한다. [부분]
- 작업당 출력 토큰 50% 감소(강화 학습)를 벤더가 주장한다. 짧은 출력이 장점이지만 코드 완결성은 별개다. [부분, 벤더 주장]

**네이티브 작업에서 따로 확인할 것**
- 메모리 안전·동시성 버그 진단 정확도, 디버거·새니타이저 출력의 해석를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 네이티브 작업 성능으로 읽지 않는다. [추정]

## 4. 근거와 한계
- [Tencent 보도자료(newswire)](https://www.newswire.ca/news-releases/tencent-launches-hy4-flash-to-power-high-speed-cost-efficient-ai-deployment-for-everyday-workflows-804953901.html)
- [Hy4 Flash 정리(neurohive)](https://neurohive.io/en/news/tencent-hy4-flash-open-weights/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 네이티브 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
