# K-EXAONE 2.5 · 앱 — 조사 기록
> 제공자: LG AI Research · 모델 ID: 미공개 [미확인] (API 문서 docs.exaone.ai에서 확인) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/18-lg/k-exaone-2.5/app.md`](../../../../md/18-lg/k-exaone-2.5/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
K-EXAONE 2.5의 앱 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- SWE-Bench Pro 59.2(LG 시험). 2.0의 SWE-bench Verified 68.2와 다른 지표다.
- API 무료 공개. 사양·컨텍스트·가중치는 미공개.

**앱 작업에서 따로 확인할 것**
- 모바일·데스크톱 빌드·서명 도구와의 호환, 긴 세션의 비용, 화면 입력 이해를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **코드 변경보다 도구 호출 위주 작업에 먼저 쓴다.** 도구 사용·자동화 지표는 크게 올랐지만 코딩 향상 폭은 그보다 작다고 보고된다. 코드 변경은 테스트와 `git diff`로 확인한다. [부분: 제작사 발표와 2차 보도]

## 4. 근거와 한계
- [Korea Times](https://www.koreatimes.co.kr/business/companies/20261109/lg-ai-research-opens-k-exaone-25-api-free-of-charge)
- [layer3labs](https://www.layer3labs.io/guides/k-exaone-2-5-explained)
- 추가 확인(2026-11-19 웹 검색): [Asiae: K-EXAONE 2.5 에이전트 성능 향상](https://view.asiae.co.kr/en/article/2026110908593029581)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 앱 작업을 직접 측정한 것이 아니다.
