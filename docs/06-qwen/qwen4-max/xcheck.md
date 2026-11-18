# Qwen4-Max — 교차 확인
> 제공자: Alibaba(Qwen) · 모델 ID: 미공개 [미확인] (보도자료 표기 `Qwen4-Max`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/06-qwen/qwen4-max/general.md`](../../../md/06-qwen/qwen4-max/general.md)

`overview.md`의 사양을 다른 출처로 다시 맞춰 본 기록이다. 2026-11-19에 Alibaba 보도자료와 Artificial Analysis 페이지를 직접 읽고 웹 검색으로 맞췄다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 출시일 | 2026-11-16 | [확인] 보도자료 + [부분] 2차 | Alibaba, Artificial Analysis FAQ | 일치 |
| 파라미터 | 2.4T, 활성 약 71B | [확인] 단일 1차 | Alibaba | Artificial Analysis는 비공개로 표기해 상충 |
| 컨텍스트 | 1M 또는 984K | [확인] 충돌 | Alibaba(1M), Artificial Analysis(984K) | 입력·추론 예약분 차이일 수 있다 [추정] |
| 가격 | $1.50 / $4.50, 캐시 적중 $0.075 | [확인] 1차(지표 사이트) + 보도자료(캐시) | Artificial Analysis, Alibaba | 둘의 단위는 서로 다른 항목이라 상충이 아니다 |
| 가중치 | 비공개 | [확인] 1차 + 지표 사이트 | Alibaba, Artificial Analysis | 소형은 예고만 |
| 독립 지수 | 43 | [확인] 단일 지표 사이트 | Artificial Analysis | 중앙값과 같다 |

## 아직 못 올린 것
- 공식 API 문서(모델 ID, reasoning 단계, 최대 출력, 한도), 벤더 벤치마크의 점수 표.

## 출처
- [Alibaba 보도자료](https://www.alibabacloud.com/press-room/alibaba-unveils-qwen4-max)
- [Artificial Analysis](https://artificialanalysis.ai/models/qwen4-max)
- [Constellation Research](https://www.constellationr.com/insights/news/alibaba-releases-qwen4-max)
