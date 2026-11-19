# K-EXAONE 2.0 · 웹 리서치 — 조사 기록
> 제공자: LG AI Research · 모델 ID: `LGAI-EXAONE/K-EXAONE-2.0-750B-A37B` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/18-lg/k-exaone-2.0/web-research.md`](../../../../md/18-lg/k-exaone-2.0/web-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web-research.md`](../../../_common/domain-rules/web-research.md)

## 2. 이 모델의 웹 리서치 작업 운용
K-EXAONE 2.0의 웹 리서치 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- Claw-Eval 77.7(GLM-5.1 84.4), τ3-Banking 14.2(DeepSeek V4 Pro 25.8). 도구 호출 파서는 `qwen3_coder`/`qwen3_xml`.
- MMLU-Pro 83.5, GPQA-Diamond 82.2, HLE 18.3, AIME 2026 92.3, IMO Answer 78.6, PolyMath 71.3, MMMLU 86.6.

**웹 리서치 작업에서 따로 확인할 것**
- 검색 도구의 인용 정확도, 출처 날조 빈도, 긴 조사에서의 일관성를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **사실 질문의 오답 비율이 중간 수준이다.** 사실·수치·인용은 출처 원문으로 확인한다. 사실 질문 기준 오답 비율이 30.4%다. [부분: 독립 측정을 옮긴 집계 페이지]

## 4. 근거와 한계
- [Hugging Face K-EXAONE-2.0](https://huggingface.co/LGAI-EXAONE/K-EXAONE-2.0-750B-A37B)
- [AsiaAI 트래커](https://asiaai.fyi/guides/south-korea-frontier-models-tracker/)
- [LG AI Research 보도](https://www.lgresearch.ai/news/view?seq=678)
- 추가 확인(2026-11-19 웹 검색): [BenchLM: AA-Omniscience 환각률(2026-11-19, Artificial Analysis 수치를 옮긴 미러)](https://benchlm.ai/benchmarks/omnisciencehallucinationrate)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 웹 리서치 작업을 직접 측정한 것이 아니다.
