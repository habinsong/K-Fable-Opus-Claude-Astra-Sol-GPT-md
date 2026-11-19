# Nemotron 3.5 Super VL · 기술 연구 — 조사 기록
> 제공자: NVIDIA · 모델 ID: `nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16`(Hugging Face), `nvidia/nemotron-3.5-super-vl`(OpenRouter) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/14-nvidia/nemotron-3.5-super-vl/tech-research.md`](../../../../md/14-nvidia/nemotron-3.5-super-vl/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 연구 작업 운용
Nemotron 3.5 Super VL 전용 기술 연구 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- GPQA-Diamond 89.52, HLE(텍스트) 31.79, BrowseComp 78, AA-LCR 68.62, IFBench 70.86. AA-Omniscience 4.03으로 환각 가능성이 있다. [확인: 읽은 값, 벤더 보고]
- 비전·문서: CharXiv 추론 80.82, MMLongBench-Doc 62.82, OCRBench v2 영어 68.12 / 중국어 59.15, Video-MME v2 32.85. 비디오 이해는 약하다.
- 독립 지수 26(미국 오픈 가중치 최상위). 이전 Nemotron 3 Super(13)의 두 배다. [부분: Artificial Analysis 게시글 요약]

**기술 연구 작업에서 따로 확인할 것**
- 벤치마크 해석, 가격·사양 수치 인용 정확도, 비교 결론의 근거 제시를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 기술 연구 작업 성능으로 읽지 않는다. [추정]

## 4. 근거와 한계
- [Hugging Face: NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16)
- [NVIDIA 블로그: Nemotron 3.5 Super VL](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 기술 연구 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
