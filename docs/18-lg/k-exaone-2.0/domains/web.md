# K-EXAONE 2.0 · 웹 — 조사 기록
> 제공자: LG AI Research · 모델 ID: `LGAI-EXAONE/K-EXAONE-2.0-750B-A37B` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/18-lg/k-exaone-2.0/web.md`](../../../../md/18-lg/k-exaone-2.0/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
K-EXAONE 2.0의 웹 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- Claw-Eval 77.7(GLM-5.1 84.4), τ3-Banking 14.2(DeepSeek V4 Pro 25.8). 도구 호출 파서는 `qwen3_coder`/`qwen3_xml`.
- SWE-bench Verified 68.2, Terminal-Bench 2.1 43.8, SciCode 37.4, τ3-Banking 14.2, Claw-Eval 77.7. 비교 4개 모델 중 코딩 항목에서 대체로 하위다.

**웹 작업에서 따로 확인할 것**
- 프런트엔드 과제의 자기 검증 능력, 도구 호출 형식, 반복 작업 단가를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [Hugging Face K-EXAONE-2.0](https://huggingface.co/LGAI-EXAONE/K-EXAONE-2.0-750B-A37B)
- [AsiaAI 트래커](https://asiaai.fyi/guides/south-korea-frontier-models-tracker/)
- [LG AI Research 보도](https://www.lgresearch.ai/news/view?seq=678)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 웹 작업을 직접 측정한 것이 아니다.
