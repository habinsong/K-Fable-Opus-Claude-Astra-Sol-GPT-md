# MAI Code 2 Flash · 앱 — 조사 기록
> 제공자: Microsoft AI · 모델 ID: 미공개 [미확인] (GitHub Copilot 모델 이름 `MAI Code 2 Flash`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/13-microsoft/mai-code-2-flash/app.md`](../../../../md/13-microsoft/mai-code-2-flash/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
MAI Code 2 Flash 전용 앱 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 입력 $0.05 / 출력 $0.25(프로모션), 정가 $0.10 / $0.50(100만 토큰당). 컨텍스트·파라미터·속도는 미확인.
- Microsoft 보고: DeepSWE 1.1 59.9, Terminal-Bench 2.1 78.3, SWE-Atlas 44.8, 평균 61.0(GPT-6 Luna 55.1, Haiku 5.5 53.9). [부분, 벤더 주장]
- 작업당 평균 비용 $0.052(프로모션). 정가가 되면 약 $0.104로 Luna($0.080)보다 비싸진다(계산).

**앱 작업에서 따로 확인할 것**
- 모바일·데스크톱 빌드·서명 도구와의 호환, 긴 세션의 비용, 화면 입력 이해를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 앱 작업 성능으로 읽지 않는다. [추정]
- **아주 긴 자율 작업과 기초 과학 연구에는 맡기지 않는다.** 제작사가 이 모델이 그 용도로 조정되지 않았다고 밝혔다. 그런 일은 상위 모델로 하고 이 모델은 다중 파일 변경과 디버깅 범위로 쓴다. [부분: 제작사 발표]
- **제작사 평균 수치로 도입을 정하지 않는다.** 같은 과제와 같은 하네스로 직접 비교한 뒤 정한다. [부분: 제작사 수치뿐]
- **일상 작업용이다.** 어려운 디버깅과 다중 파일 변경은 MAI Code 2로 올린다. [부분: 제작사 포지셔닝]

## 4. 근거와 한계
- [InfoWorld: MAI Code 2 보도](https://www.infoworld.com/article/4250152/microsoft-launches-mai-code-2-models-to-challenge-openai-and-anthropic-in-ai-coding.html)
- [Unite.AI: MAI Code 2 출시](https://www.unite.ai/microsoft-ai-releases-mai-code-2-and-mai-code-2-flash-for-enterprises/)
- 추가 확인(2026-11-19 웹 검색): [Microsoft AI: MAI Code 2와 Code 2 Flash](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/)
- 추가 확인(2026-11-19 웹 검색): [Techzine: MAI Code 2](https://www.techzine.eu/news/devops/145878/microsoft-mai-code-2-generates-code-at-a-fraction-of-the-price/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 앱 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
