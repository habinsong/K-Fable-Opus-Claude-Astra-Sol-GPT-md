# Inkling 2 Small — 교차 확인
> 제공자: Thinking Machines Lab · 모델 ID: `inkling-2-small`(Cloudflare 표기) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/17-thinking-machines/inkling-2-small/general.md`](../../../md/17-thinking-machines/inkling-2-small/general.md)

`overview.md`의 사양을 다른 출처로 다시 맞춰 본 기록이다. 2026-11-19에 공식 블로그를 직접 읽고 웹 검색으로 맞췄다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 출시일 | 2026-11-05(블로그), 가중치 11-12 | [확인] 1차 + [부분] 2차 다수 | 블로그, 검색 | 일치 |
| 총/활성 파라미터 | 5,940억 / 170억 | [확인] 1차 + [부분] 2차 다수 | 블로그, 검색 | Cloudflare만 활성 180억 |
| 라이선스 | Apache 2.0 | [확인] 1차 + [부분] 2차 | 블로그("다음 주 안전 시험 뒤") + 검색 | 저장소 LICENSE 원문 미확인 |
| 컨텍스트 | 1M(평가 궤적), 1,048,576(Cloudflare) | [확인] + [부분] | 블로그, Cloudflare | 일치 |
| 가격 | $0.30 / $1.00 | [부분] 단일 제공자 | Cloudflare(스니펫) | 공식 블로그에는 없음 |
| 독립 지수 | 31 또는 30.6 | [확인] 블로그 내부 불일치 | 블로그 본문·표 | Artificial Analysis 페이지는 직접 읽지 못함 |
| 구조(dense 여부) | MoE | [확인] 1차 | 블로그 | VentureBeat 표의 65B dense는 오류로 봄 |

## 아직 못 올린 것
- 모델 카드와 저장소 LICENSE 원문, 공식 토큰 단가, 기본 effort.

## 출처
- [Thinking Machines 블로그](https://thinkingmachines.ai/news/inkling-2-small/)
- [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/models/inkling-2-small/)
- [MindStudio](https://www.mindstudio.ai/blog/inkling-2-small-thinking-machines)
