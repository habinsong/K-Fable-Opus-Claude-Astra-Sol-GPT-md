# ERNIE 5.5 Flash Preview — 개요·사양·라이선스
> 제공자: Baidu · 모델 ID: `ernie-5.5-flash-preview`(Qianfan, 2차 표기), `baidu/ernie-5.5-flash-preview:free`(OpenRouter) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/16-baidu/ernie-5.5-flash-preview/AGENTS.md`](../../../md/16-baidu/ernie-5.5-flash-preview/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 사양
- Baidu의 ERNIE 5.5 Flash Base 체크포인트에서 처음 후학습(post-training)한 모델이다. 2026-11-11 공개됐다. **후학습 중간 체크포인트**이고 정식 출시에서 개선하겠다고 Baidu가 밝혔다. 일부 능력이 아직 부족할 수 있다고 직접 적었다. [확인: 공식 페이지 직접 읽음]
- 총 2,800억 파라미터 MoE, 토큰당 활성 140억(활성 비율 5.0%, 계산), 컨텍스트 100만 토큰. 최대 출력은 페이지에 없다. 페이지는 한 사례에서 "텍스트 전용 모델"이라고 적었다. [확인]
- 접근: Baidu Qianfan API와 OpenRouter 무료 엔드포인트 `baidu/ernie-5.5-flash-preview:free`. Qianfan 모델 ID는 `ernie-5.5-flash-preview`라는 2차 서술이 있다(공식 페이지의 링크 식별자는 `am-abe18d298d70`). [확인: OpenRouter ID / 부분: Qianfan ID]
- **가격**(100만 토큰당): Qianfan 입력 $0.280 / 출력 $1.13이라는 2차 서술이 있고 공식 페이지에는 가격이 없다. OpenRouter 무료 엔드포인트는 $0이고 미리보기 기간 동안만이다. [부분]
- **가중치**: 공식 페이지는 "Apache 2.0으로 곧 오픈소스화"라고만 적었다. 2차 서술은 목표일을 2026-11-25로 적었다. 2026-11-12 기준 Hugging Face 저장소가 없었다는 보고가 있다. [확인: 계획 / 부분: 목표일 / 미확인: 공개]
