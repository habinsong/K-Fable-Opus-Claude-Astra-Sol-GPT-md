# Qwen3.8-Flash-Next · 웹 — 조사 기록
> 제공자: Alibaba(Qwen) · 모델 ID: `Qwen/Qwen3.8-Flash-Next` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/06-qwen/qwen3.8-flash-next/web.md`](../../../../md/06-qwen/qwen3.8-flash-next/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
Qwen3.8-Flash-Next의 웹 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- Toolathlon 73.5(27B 67.1), CoWorkBench 73.9, JobBench 55.7, AndroidWorld 84.5, OSWorld 2.0 Binary 19.4 / Partial 52.3.
- SWE-bench Pro 62.5(27B 61.7, DeepSeek-V4-Flash 56.0), DeepSWE 1.1 58.7(42.2), SWE-bench Multilingual 81.0, NL2Repo 48.1, LiveCodeBench v6 91.9.

**웹 작업에서 따로 확인할 것**
- 프런트엔드 과제의 자기 검증 능력, 도구 호출 형식, 반복 작업 단가를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [Hugging Face Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- [Qwen 블로그](https://qwen.ai/blog?id=qwen3.8-flash-next)
- [Akash 분석](https://akash.network/the-bid/qwen3-8-flash-next-architecture-gpu-requirements/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 웹 작업을 직접 측정한 것이 아니다.
