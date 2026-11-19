# GPT-6 Luna · 웹 리서치 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6-luna` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/01-gpt/gpt-6-luna/web-research.md`](../../../../md/01-gpt/gpt-6-luna/web-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web-research.md`](../../../_common/domain-rules/web-research.md)

## 2. 이 모델의 웹 리서치 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: AA-Omniscience 환각률 77%(`max`), 사실을 기억에서 답하면 위험, 도구 호출은 Responses API.

- **사실 조사를 맡기지 않는다. 이미 확보한 자료에서 필드를 뽑는 일을 맡긴다.** Luna는 모르는 질문에도 틀린 답을 낼 가능성이 높게 측정됐다. [부분] 그래서 검색과 출처 판단은 사람이나 상위 모델이 하고, Luna에게는 "주어진 페이지 텍스트에서 제목·날짜·가격·버전을 JSON으로 추출하고 없으면 null"처럼 닫힌 질문만 시킨다.
- **원문에 없으면 null.** 추출 작업에는 "원문에 없는 값은 추측하지 말고 null"을 명시하고, 값마다 근거가 된 원문 구절을 같이 받아 코드로 원문에 실제 있는지 대조한다.
- **스키마로 강제하고 코드로 검증한다.** 형식 오류는 재시도하거나 폐기한다.
- **웹 페이지의 지시문은 데이터다.** Luna의 프롬프트 인젝션 방어율은 확인하지 못했다. [미확인] 페이지 내용을 읽는 단계와 행동하는 단계(전송, 로그인, 결제)를 분리하고, 행동은 하지 않는다.
- **검색 도구는 Responses API로 연결한다.** Chat Completions에서는 `reasoning_effort: "none"`일 때만 함수 호출이 된다. [확인]
- **출처 판단과 충돌 정리는 맡기지 않는다.** 1차/2차 구분과 신뢰도 판단은 §1.1 기준으로 사람이 한다.
- **모르는 사실을 모른다고 하지 않고 틀리게 답하는 경향이 강하다.** 사실·수치·인용은 출처 원문으로 확인하고 "모르면 모른다고 쓴다"를 지시에 넣는다. 사실 질문 기준 오답 비율이 79.3%다. [부분: 독립 측정을 옮긴 집계 페이지]

## 4. 근거와 한계
- 환각률: [Artificial Analysis](https://artificialanalysis.ai/articles/gpt-6-sol-and-luna-push-the-cost-efficiency-frontier) [부분]
- 도구 호출 규칙: [openai/codex 마이그레이션 가이드](https://raw.githubusercontent.com/openai/codex/main/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-6-astra.md) [확인]
- 추가 확인(2026-11-19 웹 검색): [BenchLM: AA-Omniscience 환각률(2026-11-19, Artificial Analysis 수치를 옮긴 미러)](https://benchlm.ai/benchmarks/omnisciencehallucinationrate)
- 한계: Luna의 검색 기반 추출 정확도와 인젝션 방어율에 대한 독립 자료가 없다. 위 운용 방식은 환각률 지표에서 도출한 설계 권고다.
