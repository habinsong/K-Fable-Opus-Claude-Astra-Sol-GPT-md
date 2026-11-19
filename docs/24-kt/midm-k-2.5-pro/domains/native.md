# Mi:dm K 2.5 Pro · 네이티브 — 조사 기록
> 제공자: KT · 모델 ID: 미공개 [미확인] (논문 표기 `Mi:dm K 2.5 Pro`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/24-kt/midm-k-2.5-pro/native.md`](../../../../md/24-kt/midm-k-2.5-pro/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
Mi:dm K 2.5 Pro의 네이티브 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- LiveCodeBench 90.85, HumanEval+ 78.00, MBPP(3-shot) 71.20(지속 사전 학습 2단계).
- 32B, 비공개. 공개 가중치·API 정보 없음.

**네이티브 작업에서 따로 확인할 것**
- 메모리 안전·동시성 버그 진단 정확도, 디버거·새니타이저 출력의 해석를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [arXiv 2603.18788](https://arxiv.org/html/2603.18788)
- [AsiaAI 트래커](https://asiaai.fyi/guides/south-korea-frontier-models-tracker/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 네이티브 작업을 직접 측정한 것이 아니다.
