# Raon-1 mini (preview) — 운용
> 제공자: Krafton · 모델 ID: `KRAFTON/Raon-1-mini-preview` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/25-krafton/raon-1-mini/general.md`](../../../md/25-krafton/raon-1-mini/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.2 API·배포·로컬 실행
- **RTX 5090(32GB) 한 장에서 NVFP4가 돈다.** vLLM 프로필은 최대 컨텍스트 32,768, 동시 시퀀스 8, GPU 메모리 0.85, KV 캐시 약 3 GiB, CUDA Toolkit 13 필요. Transformers는 32GB GPU에서 MXFP8 + CPU 오프로드. 첫 시작에 커널 컴파일로 약 10분이 걸린다. [확인]
- **DFlash2 추측 디코딩**: B300·vLLM 0.28.0·MXFP8에서 동시성 1일 때 최대 2.18배(GSM8K 296.3 → 646.3 tok/s), 동시성 8에서 1.38~1.65배, 32에서 1.56~1.71배, 수락 길이 3.24~4.76토큰. [확인: Krafton 측정]
- vLLM은 베타 포크가 필요하고 llama.cpp는 업스트림 병합 전 맞춤 브랜치가 필요하다. `trust_remote_code`와 원격 presence-penalty 구현이 필요하다. [확인]

#### 2.3 행동 특성과 지침 문서를 쓰는 법
- 추론 모드를 끄지 말라고 카드가 권한다. 이전 추론을 지우지 않는 설정(`truncate_history_thinking: false`)을 쓴다. [확인]
- 카드의 한계 서술: 프리뷰, 일부 비교 모델에 뒤진다, AutomationBench는 공개 분할만 사용, 텍스트 전용. [확인]
