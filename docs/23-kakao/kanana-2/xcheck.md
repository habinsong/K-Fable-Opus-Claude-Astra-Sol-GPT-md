# Kanana-2 (30B-A3B) — 교차 확인
> 제공자: Kakao · 모델 ID: `kakaocorp/kanana-2-30b-a3b-instruct`(기반 `-base`, 추론 `-thinking`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/23-kakao/kanana-2/general.md`](../../../md/23-kakao/kanana-2/general.md)

`overview.md`의 사양을 다른 출처로 다시 맞춰 본 기록이다. 2026-11-19에 공식 페이지를 직접 읽고 웹 검색으로 맞췄다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 파라미터 | 30B / 3B | [확인] 모델 카드 + 트래커 일치 | HF, 트래커 | 트래커 발표문은 32B |
| 컨텍스트 | 32,768 (YaRN 128K) | [확인] 모델 카드 | HF | 트래커 32,768 |
| 공개 시기 | 2025-12 또는 2026-01 | [충돌] | 트래커, 모델 카드 컬렉션 | 컬렉션 갱신 "5월 20일" |
| 라이선스 | Kanana License | [확인] 모델 카드 | HF | 조항 미확인 |

## 아직 못 올린 것
- 공개일, 라이선스 조항, 메모리 요구량, 2026-07 소형 모델 사양.

## 출처
- [Hugging Face kanana-2-30b-a3b-instruct](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct)
- [AsiaAI 트래커](https://asiaai.fyi/guides/south-korea-frontier-models-tracker/)
