# Motif 3 · 웹 — 조사 기록
> 제공자: Motif Technologies · 모델 ID: `Motif-Technologies/Motif-3` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/21-motif/motif-3/web.md`](../../../../md/21-motif/motif-3/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
Motif 3의 웹 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- τ³-Banking 35.3(1위), τ²-Bench Telecom 94.7(GLM-5.1 97.7), ITBench 51.5(1위), GDPVal v2 38.7.
- SWE-Bench Verified 76.2(Qwen-3.7 max 80.4), Terminal-Bench 2.1 74.9(비교 최상위권), SciCode 40.6(53.5).

**웹 작업에서 따로 확인할 것**
- 프런트엔드 과제의 자기 검증 능력, 도구 호출 형식, 반복 작업 단가를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [Hugging Face Motif-3](https://huggingface.co/Motif-Technologies/Motif-3)
- [OrcaRouter Motif 3](https://www.orcarouter.ai/blog/motif-3-base-release)
- [AsiaAI 트래커](https://asiaai.fyi/guides/south-korea-frontier-models-tracker/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 웹 작업을 직접 측정한 것이 아니다.
