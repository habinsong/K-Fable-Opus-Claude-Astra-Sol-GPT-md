# K-EXAONE 2.0 · 기술 연구 — 조사 기록
> 제공자: LG AI Research · 모델 ID: `LGAI-EXAONE/K-EXAONE-2.0-750B-A37B` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/18-lg/k-exaone-2.0/tech-research.md`](../../../../md/18-lg/k-exaone-2.0/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 연구 작업 운용
K-EXAONE 2.0의 기술 연구 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- H200 8장 노드 2대(16장), 텐서 병렬 16. LG 포크 vLLM·SGLang 필요. 컨텍스트 262,144.
- MMLU-Pro 83.5, GPQA-Diamond 82.2, HLE 18.3, AIME 2026 92.3, IMO Answer 78.6, PolyMath 71.3, MMMLU 86.6.

**기술 연구 작업에서 따로 확인할 것**
- 벤치마크 해석, 가격·사양 수치 인용 정확도, 비교 결론의 근거 제시를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [Hugging Face K-EXAONE-2.0](https://huggingface.co/LGAI-EXAONE/K-EXAONE-2.0-750B-A37B)
- [AsiaAI 트래커](https://asiaai.fyi/guides/south-korea-frontier-models-tracker/)
- [LG AI Research 보도](https://www.lgresearch.ai/news/view?seq=678)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 기술 연구 작업을 직접 측정한 것이 아니다.
