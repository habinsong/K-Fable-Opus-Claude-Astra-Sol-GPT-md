# MAI Code 2 Flash · 앱 — 조사 기록
> 제공자: Microsoft AI · 모델 ID: 미공개 [미확인] (GitHub Copilot 모델 이름 `MAI Code 2 Flash`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/13-microsoft/mai-code-2-flash/app.md`](../../../../md/13-microsoft/mai-code-2-flash/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
MAI Code 2 Flash 전용 앱 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 입력 $0.05 / 출력 $0.25(프로모션), 정가 $0.10 / $0.50(100만 토큰당). 컨텍스트·파라미터·속도는 미확인.
- Microsoft 보고: DeepSWE 1.1 59.9, Terminal-Bench 2.1 78.3, SWE-Atlas 44.8, 평균 61.0(GPT-6 Luna 55.1, Haiku 5.5 53.9). [부분, 벤더 주장]
- 작업당 평균 비용 $0.052(프로모션). 정가가 되면 약 $0.104로 Luna($0.080)보다 비싸진다(계산).

**앱 작업에서 따로 확인할 것**
- 모바일·데스크톱 빌드·서명 도구와의 호환, 긴 세션의 비용, 화면 입력 이해를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 앱 작업 성능으로 읽지 않는다. [추정]

## 4. 근거와 한계
- [InfoWorld: MAI Code 2 보도](https://www.infoworld.com/article/4250152/microsoft-launches-mai-code-2-models-to-challenge-openai-and-anthropic-in-ai-coding.html)
- [Unite.AI: MAI Code 2 출시](https://www.unite.ai/microsoft-ai-releases-mai-code-2-and-mai-code-2-flash-for-enterprises/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 앱 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
