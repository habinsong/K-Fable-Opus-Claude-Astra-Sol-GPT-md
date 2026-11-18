# Qwen3.8-Flash-Next — 교차 확인
> 제공자: Alibaba(Qwen) · 모델 ID: `Qwen/Qwen3.8-Flash-Next` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/06-qwen/qwen3.8-flash-next/general.md`](../../../md/06-qwen/qwen3.8-flash-next/general.md)

`overview.md`의 사양을 다른 출처로 다시 맞춰 본 기록이다. 2026-11-19에 공식 페이지를 직접 읽고 웹 검색으로 맞췄다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 본체/활성 | 125B / 6B (+N-gram 51B, MTP 4B) | [확인] 모델 카드 + [부분] 2차 일치 | HF, 2차 | 합계는 176B 또는 180B |
| 컨텍스트 | 262,144 → 1M(YaRN) | [확인] 모델 카드 + 2차 | HF, 2차 |  |
| 라이선스 | qwen-community-1.0 | [확인] 모델 카드 + 2차 | HF, 2차 | 조항 미확인 |
| 공개일 | 2026-08-26 또는 08-24 | [충돌] | HF 컬렉션, OrcaRouter |  |
| SWE-bench Pro | 62.5 | [확인] 모델 카드 | HF | 벤더 하네스 |

## 아직 못 올린 것
- Qwen 블로그 본문, 라이선스 조항, 4비트 실측 메모리·속도.

## 출처
- [Hugging Face Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- [Qwen 블로그](https://qwen.ai/blog?id=qwen3.8-flash-next)
- [Akash 분석](https://akash.network/the-bid/qwen3-8-flash-next-architecture-gpu-requirements/)
