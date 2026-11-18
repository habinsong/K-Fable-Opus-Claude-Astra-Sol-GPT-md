# A.X K1 · 펌웨어 — 조사 기록
> 제공자: SK Telecom · 모델 ID: `skt/A.X-K1` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/19-sk-telecom/a.x-k1/firmware.md`](../../../../md/19-sk-telecom/a.x-k1/firmware.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/firmware.md`](../../../_common/domain-rules/firmware.md)

## 2. 이 모델의 펌웨어 작업 운용
A.X K1의 펌웨어 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- LiveCodeBench v6 75.8(GLM-4.6 76.0), HumanEval+ 87.2, MBPP+ 93.0, SciCode 32.4. 비생각 모드 HumanEval+ 79.9.
- KMMLU 80.2, CLIcK 84.9, MMLU-Pro 81.5, GPQA-Diamond 74.0, AIME25 89.8, HLE 8.6.

**펌웨어 작업에서 따로 확인할 것**
- 레지스터·타이밍 수치의 환각 빈도, 장치 쓰기 전 승인 규칙 준수, 크로스 컴파일 도구 호출를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [Hugging Face A.X-K1](https://huggingface.co/skt/A.X-K1)
- [SK텔레콤 보도자료](https://www.sktelecom.com/en/press/press_detail.do?idx=1651)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 펌웨어 작업을 직접 측정한 것이 아니다.
