# Mistral Large 4 · 앱 — 조사 기록
> 제공자: Mistral AI · 모델 ID: `mistral-large-4-0`(문서 링크 표기, 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/12-mistral/mistral-large-4/app.md`](../../../../md/12-mistral/mistral-large-4/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
Mistral Large 4 전용 앱 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 컨텍스트 1M, 입력 $0.70 / 출력 $2.10. `high`에서 첫 토큰까지 70.5초, 지수 한 작업 20.0분, 출력 1.07억 토큰. 반복 코딩 루프에는 느리다.
- 독립 지수 26(`high`), `medium` 23. `high`가 3점 높지만 시간이 48% 더 든다(계산). 코딩 전용 점수는 찾지 못했다. [확인: 읽은 값 / 추정]
- 함수 호출·구조화 출력·배치·에이전트 기능이 있다. [확인: Mistral 문서]

**앱 작업에서 따로 확인할 것**
- 모바일·데스크톱 빌드·서명 도구와의 호환, 긴 세션의 비용, 화면 입력 이해를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 앱 작업 성능으로 읽지 않는다. [추정]
- **완료 보고를 파일과 테스트 출력으로 확인한다.** 에이전트가 확신에 찬 마무리 요약을 내놓고도 파일이 깨졌거나 만들어지지 않은 경우가 코딩 시험에서 지적됐다. 요약이 아니라 산출물 파일의 존재와 내용, 테스트·빌드 출력을 읽는다. [부분: 시험 글의 일반 서술]
- **어려운 설계·보안 판단은 상위 모델로 교차한다.** 빠른 코딩 모델이지 최상위 모델은 아니라는 평가가 있다. 시각적이고 자기완결적인 작은 구현에서 결과가 좋았다. [부분: 단일 리뷰]
- **접근 제어 결함 점검에는 실행 중인 앱에 붙여 쓸 수 있다.** 한 시험에서 IDOR를 빠르게 찾고 원인을 맞게 설명했다. 지적마다 사람이 재현해서 확인한다. [부분: 단일 시험]
- **`high` 이상으로 쓴다.** `medium`은 코딩 에이전트 지수가 11점 낮다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]
- **시간 상한을 둔다.** 작업당 비용은 낮지만 한 작업이 50분 가까이 걸린다. [부분: 2차 글이 옮긴 코딩 에이전트 지수]

## 4. 근거와 한계
- [Artificial Analysis: Mistral Large 4](https://artificialanalysis.ai/models/mistral-large-4)
- [Mistral docs: Mistral Large 4](https://docs.mistral.ai/models/mistral-large-4-0)
- 추가 확인(2026-11-19 웹 검색): [MindStudio: Mistral Large 4 코딩 시험](https://www.mindstudio.ai/blog/mistral-large-4-coding-test/)
- 추가 확인(2026-11-19 웹 검색): [Stack Archive: Mistral Large 4 오픈 웨이트 리뷰](https://stack-archive.com/blog/mistral-large-4-le-chonk-open-weights-coding-benchmarks-2026)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis Coding Agent Index v2.1 표(2차 정리)](https://freakyjolly.com/coding-agent-index-v2-1-explained/)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 앱 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
