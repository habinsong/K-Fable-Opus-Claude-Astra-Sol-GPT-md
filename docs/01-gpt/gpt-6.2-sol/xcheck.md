# GPT-6.2 Sol — 교차 확인
> 제공자: OpenAI · 모델 ID: `gpt-6.2-sol` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/01-gpt/gpt-6.2-sol/AGENTS.md`](../../../md/01-gpt/gpt-6.2-sol/AGENTS.md)

`overview.md`의 사양을 다른 출처로 다시 맞춰 본 기록이다. 2026-11-19에 공식 모델 페이지·가이드를 직접 읽고 웹 검색으로 맞췄다.

## 1차 출처에서 읽은 것
- 모델 페이지: ID, 컨텍스트 1,050,000, 최대 입력 922,000, 최대 출력 128,000, 컷오프 2026-06-01, 가격, 엔드포인트, 도구, 속도 등급 배수, 요금 한도.
- Using GPT-6: 마이그레이션 절차, API 변경, 프롬프트 권고, 데이터 레지던시.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 출시일 | 2026-11-17 | [확인] 공지 스레드 + [부분] 2차 다수 | OpenAI 커뮤니티 공지, Artificial Analysis FAQ, 보도 | 일치 |
| 가격 (입력/출력) | $2 / $10 | [확인] 1차 + 공지·지표 사이트 일치 | 모델 페이지, 공지, Artificial Analysis | 6.1 Sol과 같음 |
| 캐시 입력 | $0.10 | [확인] 1차 | 모델 페이지 | AA는 캐시 할인 95%로 적어 일치 |
| 컨텍스트 / 최대 출력 | 1.05M / 128K | [확인] 1차 | 모델 페이지 | 보도는 1.05M 또는 1M으로 적음 |
| 지식 컷오프 | 2026-06-01 | [확인] 단일 1차 | 모델 페이지 | Astra는 2026-05-18 |
| effort 단계 전체·기본값 | 불명 | [미확인] | 모델 페이지, 가이드에 없음 | AA 측정표로 단계 존재만 확인 |

## 아직 못 올린 것
- 허용 effort 값과 기본값, Fast 속도 향상 정도, 요금 한도 표의 최신성.
- 한 보도의 "Artificial Analysis 57, 비용 20% 감소"는 앞 값만 지표 사이트와 일치한다.

## 출처
- [GPT-6.2 Sol 모델 페이지](https://developers.openai.com/api/docs/models/gpt-6.2-sol)
- [Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model)
- [OpenAI 커뮤니티 공지](https://community.openai.com/t/gpt-6-2-astra-and-sol-are-now-available/1417531)
- [Artificial Analysis: GPT-6.2 Sol](https://artificialanalysis.ai/models/gpt-6-2-sol)
