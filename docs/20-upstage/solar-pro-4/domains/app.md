# Solar Pro 4 · 앱 — 조사 기록
> 제공자: Upstage · 모델 ID: `solar-pro4-260806`(별칭 `solar-pro4`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/20-upstage/solar-pro-4/app.md`](../../../../md/20-upstage/solar-pro-4/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
Solar Pro 4의 앱 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- 코딩 점수 없음. 컨텍스트 512K, 최대 출력 128K, 도구 호출·구조화 출력 지원.
- 입력 $0.30 / 캐시 $0.06 / 출력 $1.20. 콘솔·플레이그라운드·온프레미스. API 입력은 학습에 쓰지 않는다.

**앱 작업에서 따로 확인할 것**
- 모바일·데스크톱 빌드·서명 도구와의 호환, 긴 세션의 비용, 화면 입력 이해를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **터미널·에이전트 작업은 같은 과제로 직접 시험한 뒤 맡긴다.** 점수 상승은 제작사 발표이고 코딩 순위는 출처마다 다르다. [부분]
- **어려운 일에 맡기지 않는다.** 독립 지수가 중앙값보다 낮고 출력이 매우 길며 한 작업이 70분을 넘는다. 시간·토큰 상한을 둔다. [확인: Artificial Analysis 모델 페이지]

## 4. 근거와 한계
- [Upstage Solar Pro 4](https://console.upstage.ai/docs/models/solar-pro-4)
- [Upstage 모델 이력](https://console.upstage.ai/docs/models/history)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: Solar Pro 4](https://artificialanalysis.ai/es/articles/upstage-solar-pro-4)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: solar-pro-4 모델 페이지](https://artificialanalysis.ai/models/solar-pro-4)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 앱 작업을 직접 측정한 것이 아니다.
