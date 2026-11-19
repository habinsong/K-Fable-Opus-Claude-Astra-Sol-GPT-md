# Claude Fable 5.2 — 교차 확인
> 제공자: Anthropic · 모델 ID: `claude-fable-5-2` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/02-claude/fable-5.2/CLAUDE.md`](../../../md/02-claude/fable-5.2/CLAUDE.md)

`overview.md`의 사양을 다른 출처로 다시 맞춰 본 기록이다. 2026-11-19에 Anthropic의 공식 문서를 직접 읽고 웹 검색으로 맞췄다.

## 1차 출처에서 읽은 것
- Claude API 모델 개요 표와 모델 페이지: API ID, 가격, 컨텍스트, 최대 출력, 기본 effort, 지식 컷오프, 퇴역 약속일, 출시일.
- What's new 페이지: 파괴적 변경, 지원 기능, 가격, 가용성, 데이터 보관.
- Anthropic 제품 페이지: 출시일, Fast 모드 가격, 가용성, 벤더 벤치마크.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| API ID / 컨텍스트 / 최대 출력 | `claude-fable-5-2` / 1M / 128K | [확인] 1차 | Models overview, 모델 페이지, What's new | 세 곳 일치 |
| 가격 (입력/출력) | $8 / $40, 5분 캐시 쓰기 $10, 1시간 $16, 캐시 읽기 $0.20 | [확인] 1차 | 모델 페이지, What's new | 5.1의 $10/$50에서 인하 |
| 기본 effort / 추론 | `high` / 적응형(항상 켜짐) | [확인] 1차 | Models overview, 모델 페이지 |  |
| 지식 컷오프 / 퇴역 | 2026-06 / 2027-11-09 이전에는 퇴역하지 않음 | [확인] 1차 | Models overview |  |
| 출시일 | 2026-11-09 | [확인] 1차 + [부분] 2차 | 모델 페이지, Anthropic 제품 페이지, 보도 | 일치 |
| Fast 모드 | $16 / $80, 최대 2.5배 빠름 | [확인] What's new(가격) + [확인] 제품 페이지(배율) | 두 페이지 | 가격 일치, 배율은 제품 페이지에만 있음 |
| Mythos 5.2 | 제한 공개, 같은 사양·가격 | [확인] 1차 | Models overview, 모델 페이지 | 이 폴더의 대상이 아님 |
| FrontierCode 2.0 | 49.1% (5.1은 32.4%) | [부분] 2차 단일 계열 | 보도 | 하네스·effort가 보도마다 다를 수 있음 |

## 아직 못 올린 것
- 시스템 카드의 안전·평가 세부, Prompting 가이드와 migration guide의 본문.
- 벤더·2차 벤치마크의 원문 표.

## 출처
- [Claude 모델 개요](https://platform.claude.com/docs/en/models/overview)
- [Claude Fable 5.2 모델 페이지](https://platform.claude.com/docs/en/models/fable-5-2/overview)
- [What's new in Claude Fable 5.2](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2)
- [Claude Fable (Anthropic)](https://www.anthropic.com/claude/fable)
- [VentureBeat](https://venturebeat.com/technology/google-gemini-4-carbon-is-now-publicly-available-and-it-undercuts-claude-fable-5-2-and-opus-5-5-on-api-price)
