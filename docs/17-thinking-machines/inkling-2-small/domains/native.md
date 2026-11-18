# Inkling 2 Small · 네이티브 — 조사 기록
> 제공자: Thinking Machines Lab · 모델 ID: `inkling-2-small`(Cloudflare 표기) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/17-thinking-machines/inkling-2-small/native.md`](../../../../md/17-thinking-machines/inkling-2-small/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
Inkling 2 Small 전용 네이티브 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 총 5,940억(활성 170억), 컨텍스트 1M 평가, Apache 2.0 가중치(2026-11-12). NVFP4 체크포인트에 GPU 메모리 합계 500GB 이상.
- FrontierCode 2.0 25.4%(DeepSeek-V4.1-Flash 28.5), DeepSWE v1.1 72.1%(77.0), SWE-Atlas 61.9%(62.1), Terminal Bench Science v0.1 5.7%(12.9). 코딩은 DeepSeek V4.1 Flash에 대체로 뒤진다. [부분, 벤더 보고]
- 도구를 항상 최선으로 고르지 않는다(스킬이 많은 코드베이스). 슬래시를 과하게 쓴다. [확인: 블로그의 한계 절]

**네이티브 작업에서 따로 확인할 것**
- 메모리 안전·동시성 버그 진단 정확도, 디버거·새니타이저 출력의 해석를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 네이티브 작업 성능으로 읽지 않는다. [추정]

## 4. 근거와 한계
- [Thinking Machines: Introducing Inkling 2 Small](https://thinkingmachines.ai/news/inkling-2-small/)
- [Cloudflare Workers AI: inkling-2-small](https://developers.cloudflare.com/workers-ai/models/inkling-2-small/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 네이티브 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
