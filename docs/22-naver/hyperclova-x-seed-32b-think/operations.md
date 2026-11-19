# HyperCLOVA X SEED 32B Think — 운용
> 제공자: Naver Cloud · 모델 ID: `naver-hyperclovax/HyperCLOVAX-SEED-Think-32B` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/22-naver/hyperclova-x-seed-32b-think/AGENTS.md`](../../../md/22-naver/hyperclova-x-seed-32b-think/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.2 API·배포·로컬 실행
- **하드웨어 서술이 서로 모순이다.** 요구 사항에는 A100 80GB 4장, 구성 표에는 비전 인코더 GPU 1장(약 8GB) + LLM GPU 2장(약 60GB)으로 총 3장(약 68GB)이다. 다운로드 약 60GB, 로딩 약 5분. [확인: 모순 그대로]
- 기본 `thinking`은 꺼져 있고 `thinking_token_budget` 기본 500, 온도 0.7이다. OmniServe(OpenAI 호환, 포트 8000), vLLM, SGLang, Transformers로 서빙한다. 양자화 모델 6개가 Hub에 있다. [확인]
- 연락처는 모델 카드에 있다. 기술 보고서 인용은 "TBU"다. [확인]

#### 2.3 행동 특성과 지침 문서를 쓰는 법
- 추론을 켜려면 `thinking`을 명시하고 예산을 올려야 한다. 기본 500 토큰이면 추론이 짧게 끊긴다. [확인: 기본값 / 추정]
- 카드에 한계 절이 없다. [확인]
