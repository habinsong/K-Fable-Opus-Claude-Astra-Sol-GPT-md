# A.X K2 · 웹 리서치 — 조사 기록
> 제공자: SK Telecom · 모델 ID: `skt/A.X-K2` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/19-sk-telecom/a.x-k2/web-research.md`](../../../../md/19-sk-telecom/a.x-k2/web-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web-research.md`](../../../_common/domain-rules/web-research.md)

## 2. 이 모델의 웹 리서치 작업 운용
A.X K2의 웹 리서치 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- τ²-Bench Telecom 98.0(1위), τ³-Banking 13.0(22.9), BrowseComp(검색 10회 이내) 9.3(GLM-5.1 29.1). 카드가 에이전트 성능을 "보통"이라고 적었다.
- AIME26 97.1, KMMLU-Pro 80.5, CLIcK 91.6, GPQA-Diamond 85.6, HLE 27.8, AA-Omniscience 39.6, KMO26 92.5.

**웹 리서치 작업에서 따로 확인할 것**
- 검색 도구의 인용 정확도, 출처 날조 빈도, 긴 조사에서의 일관성를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **긴 도구 사용 작업과 웹 탐색은 직접 평가한 뒤 맡긴다.** 모델 카드가 에이전트 성능이 중간 수준이고 웹 탐색 평가에서 상위 모델에 못 미친다고 밝혔다. [부분: 2차 해설]
- **어려운 코딩과 조사에 쓰지 않는다.** 독립 지수가 9로 같은 크기의 공개 모델 중 가장 낮은 축이다. 도구 호출 위주의 좁은 일로 제한한다. [확인: Artificial Analysis 모델 페이지]
- **사실 질문의 오답 비율이 중간 수준이다.** 사실·수치·인용은 출처 원문으로 확인한다. 사실 질문 기준 오답 비율이 30.9%다. [부분: 독립 측정을 옮긴 집계 페이지]

## 4. 근거와 한계
- [Hugging Face A.X-K2](https://huggingface.co/skt/A.X-K2)
- [AsiaAI 트래커](https://asiaai.fyi/guides/south-korea-frontier-models-tracker/)
- 추가 확인(2026-11-19 웹 검색): [NYU RITS: A.X K2 해설](https://rits.shanghai.nyu.edu/ai/sk-telecom-opens-a-x-k2-688b-parameters-and-one-telling-benchmark)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: a-x-k2 모델 페이지](https://artificialanalysis.ai/models/a-x-k2)
- 추가 확인(2026-11-19 웹 검색): [BenchLM: AA-Omniscience 환각률(2026-11-19, Artificial Analysis 수치를 옮긴 미러)](https://benchlm.ai/benchmarks/omnisciencehallucinationrate)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 웹 리서치 작업을 직접 측정한 것이 아니다.
