# Tencent Hy4 · 웹 리서치 — 조사 기록
> 제공자: Tencent(Hunyuan) · 모델 ID: `tencent/hy4`(OpenRouter 표기) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/15-tencent/hy4/web-research.md`](../../../../md/15-tencent/hy4/web-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web-research.md`](../../../_common/domain-rules/web-research.md)

## 2. 이 모델의 웹 리서치 작업 운용
Tencent Hy4 전용 웹 리서치 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- Hy-BrowseComp 2.0 59.9(Tencent 시험에서 3위, 1위 GPT-6.1 Sol 61.7). 내부 검색 평가에서 환각률 15.76%에서 5.45%. [부분, 벤더 주장]
- Hy-FrontierMath T5 13.0(GPT-6.1 Sol 97.5)으로 고난도 수학은 약하다고 Tencent가 인정했다.
- 독립 지수 34.6(OpenRouter 목록 인용). 같은 사이트의 Qwen4-Max 43, Muse Ember 36보다 낮다. [부분]

**웹 리서치 작업에서 따로 확인할 것**
- 검색 도구의 인용 정확도, 출처 날조 빈도, 긴 조사에서의 일관성를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 웹 리서치 작업 성능으로 읽지 않는다. [추정]

## 4. 근거와 한계
- [Tencent Hy4 정리(explainx)](https://explainx.ai/blog/tencent-hy4-official-release-770b-vision-computer-use-terminal-bench-44-4-weights-planned-2026)
- [OpenRouter: tencent/hy4](https://openrouter.ai/tencent/hy4)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 웹 리서치 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
