# Nemotron 3.5 Super VL · 웹 — 조사 기록
> 제공자: NVIDIA · 모델 ID: `nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16`(Hugging Face), `nvidia/nemotron-3.5-super-vl`(OpenRouter) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/14-nvidia/nemotron-3.5-super-vl/web.md`](../../../../md/14-nvidia/nemotron-3.5-super-vl/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
Nemotron 3.5 Super VL 전용 웹 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 120B 총, 12B 활성, 컨텍스트 최대 1M, 입력은 텍스트·이미지·비디오(2분). 배포는 H100 4장 또는 GB200 2장.
- NVIDIA 보고: LiveCodeBench v6 88.22, SWE-bench Verified 71.10, SWE-bench Pro 51.78, Terminal-Bench 2.1 60.67, OSWorld-Verified 51.14. 일부는 내부 스캐폴딩이다. [확인: 읽은 값, 벤더 보고]
- 라이선스 OpenMDW-1.1. 가중치·데이터셋·레시피를 공개한다. [확인]

**웹 작업에서 따로 확인할 것**
- 프런트엔드 과제의 자기 검증 능력, 도구 호출 형식, 반복 작업 단가를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 웹 작업 성능으로 읽지 않는다. [추정]
- **스크린샷과 도면 입력에 쓸 수 있지만 읽은 값은 원문과 대조한다.** 멀티모달 추론을 내세우는 모델이다. [부분: 제작사 블로그 요약]
- **어려운 코딩은 맡기지 않고 이미지 입력이 필요한 일에 쓴다.** 독립 지수가 14로 낮다. 출력이 길고 빠르다. [확인: Artificial Analysis 모델 페이지]

## 4. 근거와 한계
- [Hugging Face: NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16)
- [NVIDIA 블로그: Nemotron 3.5 Super VL](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/)
- 추가 확인(2026-11-19 웹 검색): [NVIDIA 개발자 블로그: Nemotron 3.5 Super VL](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: nemotron-3-5-super-vl 모델 페이지](https://artificialanalysis.ai/models/nemotron-3-5-super-vl)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 웹 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
