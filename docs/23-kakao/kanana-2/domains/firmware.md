# Kanana-2 (30B-A3B) · 펌웨어 — 조사 기록
> 제공자: Kakao · 모델 ID: `kakaocorp/kanana-2-30b-a3b-instruct`(기반 `-base`, 추론 `-thinking`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/23-kakao/kanana-2/firmware.md`](../../../../md/23-kakao/kanana-2/firmware.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/firmware.md`](../../../_common/domain-rules/firmware.md)

## 2. 이 모델의 펌웨어 작업 운용
Kanana-2 (30B-A3B)의 펌웨어 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- HumanEval+ 79.88(Qwen3-30B-A3B 86.59), MBPP+ 73.81, 추론 모델 LiveCodeBench 60.8(68.3).
- MMLU 80.80, KMMLU 67.32, HAERAE 75.57(Qwen 53.41), GPQA-Diamond 42.93, 추론 모델 AIME 2024 78.3.

**펌웨어 작업에서 따로 확인할 것**
- 레지스터·타이밍 수치의 환각 빈도, 장치 쓰기 전 승인 규칙 준수, 크로스 컴파일 도구 호출를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **작은 도구 호출 작업에 쓰고 어려운 코딩은 맡기지 않는다.** 활성 파라미터가 작은 MoE이고 도구 호출과 지시 따르기를 겨냥한 모델이다. [부분: 제작사 발표]

## 4. 근거와 한계
- [Hugging Face kanana-2-30b-a3b-instruct](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct)
- [AsiaAI 트래커](https://asiaai.fyi/guides/south-korea-frontier-models-tracker/)
- 추가 확인(2026-11-19 웹 검색): [Korea Times: Kanana-2](https://www.koreatimes.co.kr/amp/business/tech-science/20251219/kakao-open-sources-kanana-2-model-optimized-for-agentic-ai)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 펌웨어 작업을 직접 측정한 것이 아니다.
