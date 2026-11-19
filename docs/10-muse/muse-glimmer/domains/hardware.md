# Muse Glimmer · 하드웨어 — 조사 기록
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-glimmer`(Meta 오픈 가중치 30B) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/10-muse/muse-glimmer/hardware.md`](../../../../md/10-muse/muse-glimmer/hardware.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/hardware.md`](../../../_common/domain-rules/hardware.md)

## 2. 이 모델의 하드웨어 작업 운용
Muse Glimmer의 하드웨어 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- AA 지수 35(`high`), MMMU-Pro 74%, AA-Omniscience Index -33, 환각률 82%, GPQA-Diamond 82.6(Raon 카드).
- BF16 약 60 GB, 4비트 약 18 GB, KV 캐시 128K에서 약 1.8 GB. 24GB용 K-Quant-17GB(정확도 -1%), 32GB용 K-Quant-Dynamic(-0.2%). Apache 2.0.

**하드웨어 작업에서 따로 확인할 것**
- 데이터시트·회로도 입력의 정확도, HDL 시뮬레이션 루프, 수치·단위 환각 빈도를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **모르는 사실을 모른다고 하지 않고 틀리게 답하는 경향이 강하다.** 사실·수치·인용은 출처 원문으로 확인하고 "모르면 모른다고 쓴다"를 지시에 넣는다. 사실 질문 기준 오답 비율이 83.6%다. [부분: 독립 측정을 옮긴 집계 페이지]

## 4. 근거와 한계
- [Artificial Analysis Muse Glimmer](https://artificialanalysis.ai/articles/muse-glimmer)
- [AI Weekly](https://aiweekly.co/alerts/meta-releases-muse-glimmer-a-30b-apache-20-agent-model)
- [VentureBeat](https://venturebeat.com/ai/meta-returns-to-open-source-with-muse-glimmer-an-apache-2-0-licensed-30b-parameter-ai-model-optimized-for-agents-available-now/)
- 추가 확인(2026-11-19 웹 검색): [BenchLM: AA-Omniscience 환각률(2026-11-19, Artificial Analysis 수치를 옮긴 미러)](https://benchlm.ai/benchmarks/omnisciencehallucinationrate)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 하드웨어 작업을 직접 측정한 것이 아니다.
