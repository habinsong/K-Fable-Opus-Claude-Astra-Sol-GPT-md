# A.X K1 · 앱 — 조사 기록
> 제공자: SK Telecom · 모델 ID: `skt/A.X-K1` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/19-sk-telecom/a.x-k1/app.md`](../../../../md/19-sk-telecom/a.x-k1/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
A.X K1의 앱 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- LiveCodeBench v6 75.8(GLM-4.6 76.0), HumanEval+ 87.2, MBPP+ 93.0, SciCode 32.4. 비생각 모드 HumanEval+ 79.9.
- BF16, 4노드 텐서 병렬 32 검증, 컨텍스트 131,072. 양자화 판 없음. Apache 2.0.

**앱 작업에서 따로 확인할 것**
- 모바일·데스크톱 빌드·서명 도구와의 호환, 긴 세션의 비용, 화면 입력 이해를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [Hugging Face A.X-K1](https://huggingface.co/skt/A.X-K1)
- [SK텔레콤 보도자료](https://www.sktelecom.com/en/press/press_detail.do?idx=1651)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 앱 작업을 직접 측정한 것이 아니다.
