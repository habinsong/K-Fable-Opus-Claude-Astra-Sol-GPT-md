# Raon-1 mini (preview) · 웹 — 조사 기록
> 제공자: Krafton · 모델 ID: `KRAFTON/Raon-1-mini-preview` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/25-krafton/raon-1-mini/web.md`](../../../../md/25-krafton/raon-1-mini/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
Raon-1 mini (preview)의 웹 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- BrowseComp Plus 55.7(34.8 / 32.2), BFCL v4 59.8(64.7 / 65.8), AutomationBench 29.7(공개 분할).
- SWE-Verified 70.8(Qwen3.6-35B-A3B 63.2, Gemma 4 26B-A4B 61.6), LiveCodeBench v6 81.6, Terminal-Bench Lite 47.0(63.3 / 52.0), SciCode 38.7.

**웹 작업에서 따로 확인할 것**
- 프런트엔드 과제의 자기 검증 능력, 도구 호출 형식, 반복 작업 단가를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **프리뷰이고 활성 파라미터가 작다.** 어려운 코딩 변경은 상위 모델에 맡기고 정식판과 기술 보고서가 나온 뒤 다시 평가한다. [부분: 제작사 설명]

## 4. 근거와 한계
- [Raon-1-mini-preview README](https://github.com/krafton-ai/Raon-1-mini-preview/blob/main/README.md)
- [MoneyToday](https://www.mt.co.kr/en/tech/2026/10/21/2026102109562241281)
- 추가 확인(2026-11-19 웹 검색): [Hugging Face: Raon-1 mini Preview](https://huggingface.co/KRAFTON/Raon-1-mini-Preview)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 웹 작업을 직접 측정한 것이 아니다.
