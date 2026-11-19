# EXAONE 4.5 · 웹 리서치 — 조사 기록
> 제공자: LG AI Research · 모델 ID: `LGAI-EXAONE/EXAONE-4.5-33B`(저장소 표기 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/18-lg/exaone-4.5/web-research.md`](../../../../md/18-lg/exaone-4.5/web-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web-research.md`](../../../_common/domain-rules/web-research.md)

## 2. 이 모델의 웹 리서치 작업 운용
EXAONE 4.5의 웹 리서치 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- τ2-Bench Retail 77.9 / Airline 56.5 / Telecom 73.0(Qwen3.5 27B 84.7 / 67.5 / 99.3).
- GPQA-Diamond 80.5, MMLU-Pro 83.3, AIME 2026 92.6, KMMLU-Pro 67.6, KoBALT 52.1.

**웹 리서치 작업에서 따로 확인할 것**
- 검색 도구의 인용 정확도, 출처 날조 빈도, 긴 조사에서의 일관성를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [GitHub EXAONE-4.5](https://github.com/LG-AI-EXAONE/EXAONE-4.5)
- [Taiwan News](https://www.taiwannews.com.tw/news/6337738)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 웹 리서치 작업을 직접 측정한 것이 아니다.
