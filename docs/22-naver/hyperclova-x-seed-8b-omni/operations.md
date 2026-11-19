# HyperCLOVA X SEED 8B Omni — 운용
> 제공자: Naver Cloud · 모델 ID: `naver-hyperclovax/HyperCLOVAX-SEED-Omni-8B` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/22-naver/hyperclova-x-seed-8b-omni/AGENTS.md`](../../../md/22-naver/hyperclova-x-seed-8b-omni/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.2 API·배포·로컬 실행
- **하드웨어 서술이 모순이다.** 요구 사항 A100 80GB 4장, 구성 표는 비전 인코더 약 8GB + 오디오 인코더 약 4GB(공유) + LLM 약 16GB + 비전 디코더 약 16GB + 오디오 디코더 약 4GB(공유)로 총 3장 약 48GB. 다운로드 약 16GB, 로딩 약 5분. 이미지·오디오 출력에는 S3 호환 저장소가 필요하다. [확인: 모순 그대로]
- OmniServe(OpenAI 호환 `/b/v1`, 포트 8000)가 정식 경로다. vLLM·SGLang 스니펫은 일반 템플릿이라 옴니 지원을 보여 주지 않는다. Transformers는 `trust_remote_code=True`. 양자화 모델 1개. 카드의 오디오 입력 예시는 URL 문자열을 base64로 넣어 그대로는 작동하지 않을 수 있다. [확인]

#### 2.3 행동 특성과 지침 문서를 쓰는 법
- 오디오 입출력이 핵심 기능이지만 카드 예시가 불완전하다. 오디오 기능은 직접 시험한 뒤 쓴다. [확인: 카드 서술 / 추정]
