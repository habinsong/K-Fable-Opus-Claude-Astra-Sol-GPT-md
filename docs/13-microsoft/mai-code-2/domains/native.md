# MAI Code 2 · 네이티브 — 조사 기록
> 제공자: Microsoft AI · 모델 ID: 미공개 [미확인] (GitHub Copilot 모델 이름 `MAI Code 2`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/13-microsoft/mai-code-2/native.md`](../../../../md/13-microsoft/mai-code-2/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
MAI Code 2 전용 네이티브 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 입력 $0.50 / 출력 $2.50(프로모션, 2027-05-17까지), 정가 $1.00 / $5.00(100만 토큰당). 컨텍스트와 파라미터는 미확인.
- Microsoft 보고: DeepSWE 1.1 73.2, Terminal-Bench 2.1 84.6, SWE-Atlas 43.1, FrontierCode v1.1 52.0, 평균 63.2(GPT-6.1 Sol 64.1, Opus 5.5 65.3). [부분, 벤더 주장]
- 작업당 평균 비용 $0.309(프로모션). 정가가 되면 약 $0.618로 두 배가 된다(계산).

**네이티브 작업에서 따로 확인할 것**
- 메모리 안전·동시성 버그 진단 정확도, 디버거·새니타이저 출력의 해석를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 네이티브 작업 성능으로 읽지 않는다. [추정]

## 4. 근거와 한계
- [InfoWorld: MAI Code 2 보도](https://www.infoworld.com/article/4250152/microsoft-launches-mai-code-2-models-to-challenge-openai-and-anthropic-in-ai-coding.html)
- [Unite.AI: MAI Code 2 출시](https://www.unite.ai/microsoft-ai-releases-mai-code-2-and-mai-code-2-flash-for-enterprises/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 네이티브 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
