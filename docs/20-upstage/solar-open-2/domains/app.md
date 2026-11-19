# Solar Open 2 · 앱 — 조사 기록
> 제공자: Upstage · 모델 ID: `upstage/Solar-Open2-250B` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/20-upstage/solar-open-2/app.md`](../../../../md/20-upstage/solar-open-2/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
Solar Open 2의 앱 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- SWE-Bench Verified 70.4(DeepSeek-V4-Flash 73.8), LiveCodeBench v6 92.4, Terminal Bench Hard 28.3, ArtifactsBench 55.9.
- H200 4장 이상(권장 8장), vLLM Upstage 포크, 컨텍스트 1M. Upstage Solar License(표기 의무).

**앱 작업에서 따로 확인할 것**
- 모바일·데스크톱 빌드·서명 도구와의 호환, 긴 세션의 비용, 화면 입력 이해를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [Hugging Face Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)
- [Upstage 모델 이력](https://console.upstage.ai/docs/models/history)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 앱 작업을 직접 측정한 것이 아니다.
