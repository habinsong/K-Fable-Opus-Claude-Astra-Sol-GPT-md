# Nemotron 3.5 Bolt 74B-A9B 24GB · 하드웨어 — 조사 기록
> 제공자: NVIDIA · 모델 ID: `nvidia/Nemotron-3.5-Bolt-74B-A9B-24GB`(저장소 표기 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/14-nvidia/nemotron-3.5-bolt-74b-a9b/hardware.md`](../../../../md/14-nvidia/nemotron-3.5-bolt-74b-a9b/hardware.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/hardware.md`](../../../_common/domain-rules/hardware.md)

## 2. 이 모델의 하드웨어 작업 운용
Nemotron 3.5 Bolt 74B-A9B 24GB의 하드웨어 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- 지식 점수 없음. 부모 모델 Nemotron 3.5 Super VL(120B/12B)의 GPQA-Diamond 89.52가 참고값이다.
- 24GB, IQ2_XXS 2.0625비트 전문가 + NVFP4 Mamba + Q8_0 나머지. RTX Spark(128GB 시스템)에서 83.99 TPS. llama.cpp·vLLM.

**하드웨어 작업에서 따로 확인할 것**
- 데이터시트·회로도 입력의 정확도, HDL 시뮬레이션 루프, 수치·단위 환각 빈도를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **압축본이라 값 회상을 믿지 않는다.** 24GB 구성은 2비트 양자화이고 제작사 표에서 BF16보다 점수가 낮았다. 레지스터·핀·정격 값은 문서에서만 가져오고 코드 변경은 테스트로 확인한다. [부분: 제작사 표]

## 4. 근거와 한계
- [NVIDIA Research Bolt](https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Bolt-24GB/)
- [NVIDIA 블로그](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/)
- 추가 확인(2026-11-19 웹 검색): [Magica: Nemotron 3.5 Bolt](https://magica.com/news/nvidia-nemotron-3-5-bolt-weights-local-ai-memory)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 하드웨어 작업을 직접 측정한 것이 아니다.
