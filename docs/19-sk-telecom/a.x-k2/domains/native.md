# A.X K2 · 네이티브 — 조사 기록
> 제공자: SK Telecom · 모델 ID: `skt/A.X-K2` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/19-sk-telecom/a.x-k2/native.md`](../../../../md/19-sk-telecom/a.x-k2/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
A.X K2의 네이티브 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- LiveCodeBench v6 84.0(DeepSeek V4 Flash 89.4), SciCode 41.0(Kimi-K2.6 53.5), Terminal Bench v2.1 36.0(65.9).
- FP8 약 647 GiB, GPU 메모리 800 GiB 이상(B300 4장), 컨텍스트 262,144. SKT 포크 vLLM. Apache 2.0.

**네이티브 작업에서 따로 확인할 것**
- 메모리 안전·동시성 버그 진단 정확도, 디버거·새니타이저 출력의 해석를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [Hugging Face A.X-K2](https://huggingface.co/skt/A.X-K2)
- [AsiaAI 트래커](https://asiaai.fyi/guides/south-korea-frontier-models-tracker/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 네이티브 작업을 직접 측정한 것이 아니다.
