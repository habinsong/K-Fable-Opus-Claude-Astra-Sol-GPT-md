# Claude Haiku 4.5 — 교차 확인
> 제공자: Anthropic · 모델 ID: `claude-haiku-4-5-20251001` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/02-claude/haiku-4.5/general.md`](../../../md/02-claude/haiku-4.5/general.md)

`overview.md`의 사양을 다른 출처로 다시 맞춰 본 기록이다. 2026-11-19에 Anthropic 공식 문서 두 페이지와 Artificial Analysis 두 페이지를 직접 읽었다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| API ID / 별칭 | `claude-haiku-4-5-20251001` / `claude-haiku-4-5` | [확인] 1차 | 모델 페이지, 상태 표 | 일치 |
| 출시일 | 2025-10-15 | [확인] 1차 + 지표 사이트 | 모델 페이지, Artificial Analysis | 일치 |
| 가격 (입력/출력) | $1 / $5 | [확인] 1차 + 지표 사이트 | 모델 페이지, Artificial Analysis | 일치 |
| 컨텍스트 / 최대 출력 | 200K / 64K | [확인] 1차 + 지표 사이트(컨텍스트) | 모델 페이지, Artificial Analysis | 최대 출력은 1차만 |
| 지식 컷오프 | Anthropic 2025-02(신뢰), 2025-07(학습) | [확인] 1차 | 모델 페이지 | 지표 사이트는 2025-07로 적음 |
| 상태 | 활성(레거시) 대 deprecated | [충돌] | Anthropic 상태 표, Artificial Analysis | 퇴역 공지는 어디에도 없다 |
| 퇴역 약속일 | 2026-10-15 이전에는 없음 | [확인] 1차 | 상태 표, 모델 페이지 | 날짜가 지났다 |
| 독립 지수 | 7(추론 변형) | [확인] 단일 지표 사이트 | Artificial Analysis |  |

## 아직 못 올린 것
- Haiku 4.5 시스템 카드, 퇴역 공지 여부의 최신 확인.

## 출처
- [Haiku 4.5 모델 페이지](https://platform.claude.com/docs/en/models/haiku-4-5/overview)
- [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- [Artificial Analysis: Haiku 4.5](https://artificialanalysis.ai/models/claude-4-5-haiku)
- [Artificial Analysis: Haiku 5.5](https://artificialanalysis.ai/models/claude-haiku-5-5)
