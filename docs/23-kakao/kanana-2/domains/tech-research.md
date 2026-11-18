# Kanana-2 (30B-A3B) · 기술 연구 — 조사 기록
> 제공자: Kakao · 모델 ID: `kakaocorp/kanana-2-30b-a3b-instruct`(기반 `-base`, 추론 `-thinking`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/23-kakao/kanana-2/tech-research.md`](../../../../md/23-kakao/kanana-2/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 연구 작업 운용
Kanana-2 (30B-A3B)의 기술 연구 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- 30B 총·3B 활성, BF16 가중치 약 62GB(계산). 컨텍스트 32,768, YaRN 128K. Kanana License.
- MMLU 80.80, KMMLU 67.32, HAERAE 75.57(Qwen 53.41), GPQA-Diamond 42.93, 추론 모델 AIME 2024 78.3.

**기술 연구 작업에서 따로 확인할 것**
- 벤치마크 해석, 가격·사양 수치 인용 정확도, 비교 결론의 근거 제시를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [Hugging Face kanana-2-30b-a3b-instruct](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct)
- [AsiaAI 트래커](https://asiaai.fyi/guides/south-korea-frontier-models-tracker/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 기술 연구 작업을 직접 측정한 것이 아니다.
