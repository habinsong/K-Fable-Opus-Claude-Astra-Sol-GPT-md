# Nemotron 3.5 Super VL · 웹 리서치 — 조사 기록
> 제공자: NVIDIA · 모델 ID: `nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16`(Hugging Face), `nvidia/nemotron-3.5-super-vl`(OpenRouter) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/14-nvidia/nemotron-3.5-super-vl/web-research.md`](../../../../md/14-nvidia/nemotron-3.5-super-vl/web-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web-research.md`](../../../_common/domain-rules/web-research.md)

## 2. 이 모델의 웹 리서치 작업 운용
Nemotron 3.5 Super VL 전용 웹 리서치 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- GPQA-Diamond 89.52, HLE(텍스트) 31.79, BrowseComp 78, AA-LCR 68.62, IFBench 70.86. AA-Omniscience 4.03으로 환각 가능성이 있다. [확인: 읽은 값, 벤더 보고]
- 비전·문서: CharXiv 추론 80.82, MMLongBench-Doc 62.82, OCRBench v2 영어 68.12 / 중국어 59.15, Video-MME v2 32.85. 비디오 이해는 약하다.
- 독립 지수 26(미국 오픈 가중치 최상위). 이전 Nemotron 3 Super(13)의 두 배다. [부분: Artificial Analysis 게시글 요약]

**웹 리서치 작업에서 따로 확인할 것**
- 검색 도구의 인용 정확도, 출처 날조 빈도, 긴 조사에서의 일관성를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 웹 리서치 작업 성능으로 읽지 않는다. [추정]

## 4. 근거와 한계
- [Hugging Face: NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16)
- [NVIDIA 블로그: Nemotron 3.5 Super VL](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 웹 리서치 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
