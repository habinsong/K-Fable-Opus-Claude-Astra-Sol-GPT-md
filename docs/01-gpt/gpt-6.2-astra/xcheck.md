# GPT-6.2 Astra — 교차 확인
> 제공자: OpenAI · 모델 ID: `gpt-6.2-astra` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/01-gpt/gpt-6.2-astra/general.md`](../../../md/01-gpt/gpt-6.2-astra/general.md)

`overview.md`의 사양을 다른 출처로 다시 맞춰 본 기록이다. 2026-11-19에 공식 모델 페이지·가이드를 직접 읽고 웹 검색으로 맞췄다.

## 1차 출처에서 읽은 것
- 모델 페이지: ID, 컨텍스트, 최대 입력·출력, 컷오프 2026-05-18, 가격, 엔드포인트, 도구.
- Using GPT-6: 마이그레이션 절차, API 변경, Astra의 출력 성향, 레지던시.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 출시일 | 2026-11-17 | [확인] 공지 스레드 + [부분] 보도 | OpenAI 커뮤니티 공지, 보도 | 6.2 Sol과 같은 날 |
| 가격 (입력/출력) | $8 / $40 | [확인] 1차 + 공지 일치 | 모델 페이지, 공지 | 6 Astra의 $10/$50보다 낮음 |
| 캐시 입력 | $0.40 | [확인] 단일 1차 | 모델 페이지 |  |
| 컨텍스트 / 최대 출력 | 1.05M / 128K | [확인] 1차 | 모델 페이지 |  |
| 지식 컷오프 | 2026-05-18 | [확인] 단일 1차 | 모델 페이지 | 6.2 Sol은 2026-06-01 |
| 독립 지수 | 62 | [확인] 단일 지표 사이트 | Artificial Analysis | 같은 사이트의 Sol 페이지 비교 행 |

## 아직 못 올린 것
- 허용 effort 값과 기본값, 공지의 `xhigh`·`max` 표현이 가리키는 정확한 단계.
- 벤더 벤치마크의 원문 표(이미지).

## 출처
- [GPT-6.2 Astra 모델 페이지](https://developers.openai.com/api/docs/models/gpt-6.2-astra)
- [Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model)
- [OpenAI 커뮤니티 공지](https://community.openai.com/t/gpt-6-2-astra-and-sol-are-now-available/1417531)
- [Artificial Analysis: GPT-6.2 Sol](https://artificialanalysis.ai/models/gpt-6-2-sol)
