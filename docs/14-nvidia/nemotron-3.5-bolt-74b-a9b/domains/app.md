# Nemotron 3.5 Bolt 74B-A9B 24GB · 앱 — 조사 기록
> 제공자: NVIDIA · 모델 ID: `nvidia/Nemotron-3.5-Bolt-74B-A9B-24GB`(저장소 표기 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/14-nvidia/nemotron-3.5-bolt-74b-a9b/app.md`](../../../../md/14-nvidia/nemotron-3.5-bolt-74b-a9b/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
Nemotron 3.5 Bolt 74B-A9B 24GB의 앱 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- 속도: SPEED-Bench-Coding에서 83.99 TPS. 코딩 정확도 점수는 이미지라 읽지 못했다.
- 24GB, IQ2_XXS 2.0625비트 전문가 + NVFP4 Mamba + Q8_0 나머지. RTX Spark(128GB 시스템)에서 83.99 TPS. llama.cpp·vLLM.

**앱 작업에서 따로 확인할 것**
- 모바일·데스크톱 빌드·서명 도구와의 호환, 긴 세션의 비용, 화면 입력 이해를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [NVIDIA Research Bolt](https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Bolt-24GB/)
- [NVIDIA 블로그](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 앱 작업을 직접 측정한 것이 아니다.
