# Mistral Large 4 — 교차 확인
> 제공자: Mistral AI · 모델 ID: `mistral-large-4-0`(문서 링크 표기, 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/12-mistral/mistral-large-4/general.md`](../../../md/12-mistral/mistral-large-4/general.md)

`overview.md`의 사양을 다른 출처로 다시 맞춰 본 기록이다. 2026-11-19에 Mistral 문서와 Artificial Analysis 페이지를 직접 읽고 웹 검색으로 맞췄다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 출시일 | 10-06(미리보기) / 10-29 / 11-05 | [충돌] | 2차, Artificial Analysis, Mistral 문서 | 미리보기·가중치·정식의 구분 때문으로 보임 [추정] |
| 총/활성 파라미터 | 1.05조(또는 1.1조) / 520억 | [확인] 1차 두 곳 | Mistral 문서, Artificial Analysis | 총 파라미터 표기가 둘로 갈림 |
| 컨텍스트 | 1M | [확인] 1차 두 곳 | Mistral 문서, Artificial Analysis | 524K·512K 서술은 2차 |
| 가격 | $0.70 / $0.07(캐시) / $2.10 | [확인] 1차 두 곳 일치 | Mistral 문서, Artificial Analysis | 미리보기 $1.36/$4.18은 2차 |
| 라이선스 | Mistral Ecosystem Open-Weight License | [확인] 1차 두 곳 | 위 두 곳 | 조항은 미확인 |
| 독립 지수 | 26(`high`), 23(`medium`) | [확인] 단일 지표 사이트 | Artificial Analysis | 비교군 중앙값 23 |

## 아직 못 올린 것
- 라이선스 조항 원문, 정확한 API ID·최대 출력, Hugging Face 저장소.

## 출처
- [Mistral 문서](https://docs.mistral.ai/models/mistral-large-4-0)
- [Artificial Analysis](https://artificialanalysis.ai/models/mistral-large-4)
- [eesel.ai](https://www.eesel.ai/blog/mistral-large-4)
