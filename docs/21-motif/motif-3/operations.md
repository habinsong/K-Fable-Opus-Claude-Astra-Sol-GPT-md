# Motif 3 — 운용
> 제공자: Motif Technologies · 모델 ID: `Motif-Technologies/Motif-3` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/21-motif/motif-3/AGENTS.md`](../../../md/21-motif/motif-3/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.2 API·배포·로컬 실행
- 권장 서빙은 vLLM Motif 포크(v0.26.0 기반, Docker `ghcr.io/motiftechnologies/vllm:v0.26.0-motif3`)이고 도구·추론 파서는 `motif`다. H200 예시는 텐서 병렬 1·데이터 병렬 8·전문가 병렬, `--max-model-len 262144`, `--block-size 128`, `FLASH_ATTN_MLA` 백엔드. B200은 백엔드 지정 없음. 최소 VRAM은 카드에 없다. 추측 디코딩은 1토큰이 최적이다. [확인]
- Transformers는 `trust_remote_code=True`가 필요하다. 온라인 블록-FP8(`modelopt_blockfp8`)로 올릴 수 있다. [확인]

#### 2.3 행동 특성과 지침 문서를 쓰는 법
- 카드는 에이전트·도구 사용에 강하다고 소개하고 일부 지표에서 뒤진다고 직접 밝혔다. 문서에는 한계 절이 없다. [확인]
