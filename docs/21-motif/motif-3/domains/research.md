# Motif 3 · 연구 — 조사 기록
> 제공자: Motif Technologies · 모델 ID: `Motif-Technologies/Motif-3` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/21-motif/motif-3/research.md`](../../../../md/21-motif/motif-3/research.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/research.md`](../../../_common/domain-rules/research.md)

## 2. 이 모델의 연구 작업 운용
Motif 3의 연구 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- GPQA-Diamond 83.4(92.9), HLE 37.0, IMOAnswerBench 83.2, CritPt 6.6, OmniScience 정확도 30.1 / 비환각 71.6.
- AA-LCR 72.3(MiniMax-3 80.3), IFBench 78.2.

**연구 작업에서 따로 확인할 것**
- 논문 인용의 실재 여부, 통계 수치 처리, 가설과 사실의 구분를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **출력 토큰이 많이 든다.** 지수 평가에서 같은 급 중앙값보다 훨씬 많은 출력을 만들었다. 토큰 예산을 넉넉히 잡는다. [부분]

## 4. 근거와 한계
- [Hugging Face Motif-3](https://huggingface.co/Motif-Technologies/Motif-3)
- [OrcaRouter Motif 3](https://www.orcarouter.ai/blog/motif-3-base-release)
- [AsiaAI 트래커](https://asiaai.fyi/guides/south-korea-frontier-models-tracker/)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: Motif 3 Beta](https://artificialanalysis.ai/ja/models/motif-0714)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 연구 작업을 직접 측정한 것이 아니다.
