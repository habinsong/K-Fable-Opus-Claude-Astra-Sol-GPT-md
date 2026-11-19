# ERNIE 5.5 Flash Preview · 네이티브 — 조사 기록
> 제공자: Baidu · 모델 ID: `ernie-5.5-flash-preview`(Qianfan, 2차 표기), `baidu/ernie-5.5-flash-preview:free`(OpenRouter) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/16-baidu/ernie-5.5-flash-preview/native.md`](../../../../md/16-baidu/ernie-5.5-flash-preview/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
ERNIE 5.5 Flash Preview 전용 네이티브 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 컨텍스트 100만, 총 2,800억(활성 140억). 후학습 중간 체크포인트이고 일부 능력이 부족할 수 있다고 Baidu가 밝혔다. 텍스트 전용.
- 시연 수치: 11시간 단일 코딩 작업, 모바일 미니 게임 약 100개(24개 공개), 코드 10,000줄 이상의 애니메이션. 성공률 자료는 없다. [부분, 벤더 시연]
- 벤치마크 점수는 이미지로만 제공돼 읽지 못했다. [미확인]

**네이티브 작업에서 따로 확인할 것**
- 메모리 안전·동시성 버그 진단 정확도, 디버거·새니타이저 출력의 해석를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 네이티브 작업 성능으로 읽지 않는다. [추정]
- **후훈련이 끝나지 않은 중간 체크포인트다.** 최종판이 다르게 동작할 수 있으므로 갱신 전후에 같은 과제로 회귀 시험을 돌린다. [부분: 2차 설명]
- **긴 자율 실행의 시연을 근거로 삼지 않는다.** 길게 돌릴 때는 체크포인트와 중단 지점을 둔다. [부분: 제작사 시연]

## 4. 근거와 한계
- [Baidu: Introducing ERNIE 5.5 Flash Preview](https://ernie.baidu.com/release/ernie-5-5-flash-preview/)
- [pasqualepillitteri: ERNIE 5.5 Flash Preview](https://pasqualepillitteri.it/en/news/32984/baidu-releases-ernie-55-flash-preview-free-openrouter)
- 추가 확인(2026-11-19 웹 검색): [ai-tldr: ERNIE 5.5 Flash Preview](https://ai-tldr.dev/releases/baidu-ernie-5-5-flash-preview/)
- 추가 확인(2026-11-19 웹 검색): [AIreiter: ERNIE 5.5 Flash Preview API 리뷰](https://aireiter.com/blog/ernie-5-5-flash-preview-api-review)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 네이티브 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
