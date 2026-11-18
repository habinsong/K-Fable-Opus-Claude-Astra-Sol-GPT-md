# ERNIE 5.5 Flash Preview · 펌웨어 — 조사 기록
> 제공자: Baidu · 모델 ID: `ernie-5.5-flash-preview`(Qianfan, 2차 표기), `baidu/ernie-5.5-flash-preview:free`(OpenRouter) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/16-baidu/ernie-5.5-flash-preview/firmware.md`](../../../../md/16-baidu/ernie-5.5-flash-preview/firmware.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/firmware.md`](../../../_common/domain-rules/firmware.md)

## 2. 이 모델의 펌웨어 작업 운용
ERNIE 5.5 Flash Preview 전용 펌웨어 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 컨텍스트 100만, 총 2,800억(활성 140억). 후학습 중간 체크포인트이고 일부 능력이 부족할 수 있다고 Baidu가 밝혔다. 텍스트 전용.
- 시연 수치: 11시간 단일 코딩 작업, 모바일 미니 게임 약 100개(24개 공개), 코드 10,000줄 이상의 애니메이션. 성공률 자료는 없다. [부분, 벤더 시연]
- 벤치마크 점수는 이미지로만 제공돼 읽지 못했다. [미확인]

**펌웨어 작업에서 따로 확인할 것**
- 레지스터·타이밍 수치의 환각 빈도, 장치 쓰기 전 승인 규칙 준수, 크로스 컴파일 도구 호출를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 펌웨어 작업 성능으로 읽지 않는다. [추정]

## 4. 근거와 한계
- [Baidu: Introducing ERNIE 5.5 Flash Preview](https://ernie.baidu.com/release/ernie-5-5-flash-preview/)
- [pasqualepillitteri: ERNIE 5.5 Flash Preview](https://pasqualepillitteri.it/en/news/32984/baidu-releases-ernie-55-flash-preview-free-openrouter)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 펌웨어 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
