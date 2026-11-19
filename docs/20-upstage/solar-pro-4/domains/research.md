# Solar Pro 4 · 연구 — 조사 기록
> 제공자: Upstage · 모델 ID: `solar-pro4-260806`(별칭 `solar-pro4`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/20-upstage/solar-pro-4/research.md`](../../../../md/20-upstage/solar-pro-4/research.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/research.md`](../../../_common/domain-rules/research.md)

## 2. 이 모델의 연구 작업 운용
Solar Pro 4의 연구 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- 지식 기준 2026-02. 지식 벤치마크 없음. 입출력 언어 영어·한국어·일본어.
- 컨텍스트 512K, 출력 128K. 장문 평가 없음.

**연구 작업에서 따로 확인할 것**
- 논문 인용의 실재 여부, 통계 수치 처리, 가설과 사실의 구분를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **어려운 일에 맡기지 않는다.** 독립 지수가 중앙값보다 낮고 출력이 매우 길며 한 작업이 70분을 넘는다. 시간·토큰 상한을 둔다. [확인: Artificial Analysis 모델 페이지]
- **사실 질문에서 모르면 기권하는 편이다.** 기권을 오류로 취급하지 말고, 그래도 인용과 수치는 원문으로 확인한다. 사실 질문 기준 오답 비율이 20.9%다. [부분: 독립 측정을 옮긴 집계 페이지]

## 4. 근거와 한계
- [Upstage Solar Pro 4](https://console.upstage.ai/docs/models/solar-pro-4)
- [Upstage 모델 이력](https://console.upstage.ai/docs/models/history)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: solar-pro-4 모델 페이지](https://artificialanalysis.ai/models/solar-pro-4)
- 추가 확인(2026-11-19 웹 검색): [BenchLM: AA-Omniscience 환각률(2026-11-19, Artificial Analysis 수치를 옮긴 미러)](https://benchlm.ai/benchmarks/omnisciencehallucinationrate)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 연구 작업을 직접 측정한 것이 아니다.
