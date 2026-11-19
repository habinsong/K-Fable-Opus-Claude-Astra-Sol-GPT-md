# Kanana-2 (30B-A3B) — 운용
> 제공자: Kakao · 모델 ID: `kakaocorp/kanana-2-30b-a3b-instruct`(기반 `-base`, 추론 `-thinking`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/23-kakao/kanana-2/AGENTS.md`](../../../md/23-kakao/kanana-2/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.2 API·배포·로컬 실행
- Transformers 4.51.0 이상. vLLM은 `--enable-auto-tool-choice --tool-call-parser hermes`, SGLang은 `--tool-call-parser qwen`. 128K는 YaRN(factor 4.0)을 켜야 하고 짧은 글 성능이 떨어질 수 있어 필요할 때만 켠다. 카드 퀵스타트는 탐욕 디코딩이다. [확인]
- 메모리 요구량은 카드에 없다. BF16 31B 파라미터이면 가중치만 약 62GB다(파라미터 × 2바이트, 계산). 양자화 모델은 Hub에 1개다. [미확인 / 추정]

#### 2.3 행동 특성과 지침 문서를 쓰는 법
- 지시 모델에서 한국어 지식(HAERAE 75.57)·지시 수행(IFBench 41.84)이 Qwen3-30B-A3B(2507)보다 강하고 영어 지식·코딩은 약하다. 아래 비판 참조. [확인]
