# A.X K2 · 웹 — 조사 기록
> 제공자: SK Telecom · 모델 ID: `skt/A.X-K2` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/19-sk-telecom/a.x-k2/web.md`](../../../../md/19-sk-telecom/a.x-k2/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
A.X K2의 웹 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- τ²-Bench Telecom 98.0(1위), τ³-Banking 13.0(22.9), BrowseComp(검색 10회 이내) 9.3(GLM-5.1 29.1). 카드가 에이전트 성능을 "보통"이라고 적었다.
- LiveCodeBench v6 84.0(DeepSeek V4 Flash 89.4), SciCode 41.0(Kimi-K2.6 53.5), Terminal Bench v2.1 36.0(65.9).

**웹 작업에서 따로 확인할 것**
- 프런트엔드 과제의 자기 검증 능력, 도구 호출 형식, 반복 작업 단가를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [Hugging Face A.X-K2](https://huggingface.co/skt/A.X-K2)
- [AsiaAI 트래커](https://asiaai.fyi/guides/south-korea-frontier-models-tracker/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 웹 작업을 직접 측정한 것이 아니다.
