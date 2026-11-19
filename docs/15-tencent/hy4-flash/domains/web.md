# Tencent Hy4 Flash · 웹 — 조사 기록
> 제공자: Tencent(Hunyuan) · 모델 ID: 미공개 [미확인] (보도자료 표기 `Hy4 flash`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/15-tencent/hy4-flash/web.md`](../../../../md/15-tencent/hy4-flash/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
Tencent Hy4 Flash 전용 웹 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 컨텍스트 최대 1M, 총 2,240억(활성 120억), 디코딩 150 tok/s 초과(벤더). 입력 $0.07 / 출력 $0.281(100만 토큰당).
- 숫자 벤치마크가 없다. 슬라이드 편집 시험에서 Flash 74.0 대 Hy4 78.9(Tencent 시험). 코딩 능력은 직접 시험해야 한다. [부분]
- 작업당 출력 토큰 50% 감소(강화 학습)를 벤더가 주장한다. 짧은 출력이 장점이지만 코드 완결성은 별개다. [부분, 벤더 주장]

**웹 작업에서 따로 확인할 것**
- 프런트엔드 과제의 자기 검증 능력, 도구 호출 형식, 반복 작업 단가를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 웹 작업 성능으로 읽지 않는다. [추정]

## 4. 근거와 한계
- [Tencent 보도자료(newswire)](https://www.newswire.ca/news-releases/tencent-launches-hy4-flash-to-power-high-speed-cost-efficient-ai-deployment-for-everyday-workflows-804953901.html)
- [Hy4 Flash 정리(neurohive)](https://neurohive.io/en/news/tencent-hy4-flash-open-weights/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 웹 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
