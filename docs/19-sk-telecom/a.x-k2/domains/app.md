# A.X K2 · 앱 — 조사 기록
> 제공자: SK Telecom · 모델 ID: `skt/A.X-K2` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/19-sk-telecom/a.x-k2/app.md`](../../../../md/19-sk-telecom/a.x-k2/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
A.X K2의 앱 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- LiveCodeBench v6 84.0(DeepSeek V4 Flash 89.4), SciCode 41.0(Kimi-K2.6 53.5), Terminal Bench v2.1 36.0(65.9).
- FP8 약 647 GiB, GPU 메모리 800 GiB 이상(B300 4장), 컨텍스트 262,144. SKT 포크 vLLM. Apache 2.0.

**앱 작업에서 따로 확인할 것**
- 모바일·데스크톱 빌드·서명 도구와의 호환, 긴 세션의 비용, 화면 입력 이해를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **긴 도구 사용 작업과 웹 탐색은 직접 평가한 뒤 맡긴다.** 모델 카드가 에이전트 성능이 중간 수준이고 웹 탐색 평가에서 상위 모델에 못 미친다고 밝혔다. [부분: 2차 해설]
- **어려운 코딩과 조사에 쓰지 않는다.** 독립 지수가 9로 같은 크기의 공개 모델 중 가장 낮은 축이다. 도구 호출 위주의 좁은 일로 제한한다. [확인: Artificial Analysis 모델 페이지]

## 4. 근거와 한계
- [Hugging Face A.X-K2](https://huggingface.co/skt/A.X-K2)
- [AsiaAI 트래커](https://asiaai.fyi/guides/south-korea-frontier-models-tracker/)
- 추가 확인(2026-11-19 웹 검색): [NYU RITS: A.X K2 해설](https://rits.shanghai.nyu.edu/ai/sk-telecom-opens-a-x-k2-688b-parameters-and-one-telling-benchmark)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: a-x-k2 모델 페이지](https://artificialanalysis.ai/models/a-x-k2)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 앱 작업을 직접 측정한 것이 아니다.
