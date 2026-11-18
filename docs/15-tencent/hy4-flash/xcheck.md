# Tencent Hy4 Flash — 교차 확인
> 제공자: Tencent(Hunyuan) · 모델 ID: 미공개 [미확인] (보도자료 표기 `Hy4 flash`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/15-tencent/hy4-flash/general.md`](../../../md/15-tencent/hy4-flash/general.md)

`overview.md`의 사양을 다른 출처로 다시 맞춰 본 기록이다. 2026-11-19에 보도자료를 직접 읽고 웹 검색으로 맞췄다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 발표일 | 2026-11-16 또는 11-17 | [충돌] | 보도 다수(11-16), 보도자료 도시·날짜(11-17) | 시간대 차이일 수 있다 [추정] |
| 총/활성 파라미터 | 2,240억 / 120억 | [확인] 1차 + [부분] 2차 다수 | 보도자료, 검색 | 한 곳은 2,200억으로 적음 |
| Engram 파라미터 | 640억 | [확인] 1차 + [부분] 2차 | 보도자료, 검색 |  |
| 컨텍스트 | 1M | [확인] 1차 + [부분] 2차 | 보도자료, 검색 |  |
| 가격 | $0.070 / $0.281 / 캐시 $0.003 | [확인] 1차 + RMB 환산 일치 | 보도자료, 2차(RMB 0.5/2/0.02) | 출력은 환산에 따라 $0.28~0.30 |
| 디코딩 속도 | 150 tok/s 초과 | [확인] 벤더 서술 | 보도자료 | 독립 측정 없음 |
| 가중치 | 계획만 | [확인] 계획 + [충돌] 공개 여부 | 보도자료, 2차 | 11-18 HF 카드 서술은 미확인 |

## 아직 못 올린 것
- 숫자 벤치마크, 독립 평가, 공식 API 문서, 가중치 저장소.

## 출처
- [Tencent 보도자료](https://www.newswire.ca/news-releases/tencent-launches-hy4-flash-to-power-high-speed-cost-efficient-ai-deployment-for-everyday-workflows-804953901.html)
- [neurohive](https://neurohive.io/en/news/tencent-hy4-flash-open-weights/)
- [explainx](https://explainx.ai/blog/tencent-hy4-flash-224b-workbuddy-pricing-open-weights-planned-november-2026)
