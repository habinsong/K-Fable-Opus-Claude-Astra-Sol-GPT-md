# MiMo-V2.6-Flash · 연구 — 조사 기록
> 제공자: Xiaomi · 모델 ID: `XiaomiMiMo/MiMo-V2.6-Flash`(RL 판 `-RL`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/26-xiaomi/mimo-v2.6-flash/research.md`](../../../../md/26-xiaomi/mimo-v2.6-flash/research.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/research.md`](../../../_common/domain-rules/research.md)

## 2. 이 모델의 연구 작업 운용
MiMo-V2.6-Flash의 연구 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- 지식 벤치마크가 정리 글에 없다. 사이버: CyberGym 95.1, ExploitGym 6.0, ExploitBench 25.3, SEC Bench Pro 47.5.
- 컨텍스트 1M. 슬라이딩 윈도우 128토큰 39층 + 전역 9층 구조. 장문 평가 없음.

**연구 작업에서 따로 확인할 것**
- 논문 인용의 실재 여부, 통계 수치 처리, 가설과 사실의 구분를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **넓은 추론이 필요한 일은 상위 모델에 맡긴다.** 에이전트 과제에서는 Pro와 가깝지만 범용 추론은 Pro가 앞선다는 분석이 있다. [부분]
- **모르는 사실을 모른다고 하지 않고 틀리게 답하는 경향이 강하다.** 사실·수치·인용은 출처 원문으로 확인하고 "모르면 모른다고 쓴다"를 지시에 넣는다. 사실 질문 기준 오답 비율이 52.2%다. [부분: 독립 측정을 옮긴 집계 페이지]

## 4. 근거와 한계
- [OrcaRouter MiMo-V2.6-Flash](https://www.orcarouter.ai/blog/xiaomi-mimo-v2-6-flash-release)
- [Hugging Face MiMo-V2.6-Flash](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash)
- [DataNorth](https://datanorth.ai/news/xiaomi-releases-mimo-v2-6-pro-and-flash)
- 추가 확인(2026-11-19 웹 검색): [AIreiter: MiMo V2.6 Pro 리뷰](https://aireiter.com/blog/mimo-v2-6-pro-review-tested)
- 추가 확인(2026-11-19 웹 검색): [BenchLM: AA-Omniscience 환각률(2026-11-19, Artificial Analysis 수치를 옮긴 미러)](https://benchlm.ai/benchmarks/omnisciencehallucinationrate)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 연구 작업을 직접 측정한 것이 아니다.
