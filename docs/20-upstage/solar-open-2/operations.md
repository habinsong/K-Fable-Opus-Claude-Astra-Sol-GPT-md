# Solar Open 2 — 운용
> 제공자: Upstage · 모델 ID: `upstage/Solar-Open2-250B` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/20-upstage/solar-open-2/general.md`](../../../md/20-upstage/solar-open-2/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.2 API·배포·로컬 실행
- **최소 H200 4장, 권장 8장**(장당 141GB 이상, B200 가능). vLLM(v0.22.0, CUDA 12.9, Upstage 포크, Docker `upstage/vllm-solar-open2`)이 권장이고 SGLang·Transformers(Upstage 브랜치 `v5.14.1-solar-open2`)도 된다. `fla-core` 0.5.1 이상이 없으면 Transformers가 "훨씬 느린" PyTorch 경로로 떨어진다. [확인]
- 샘플링: 온도 1.0, top_p 1.0. `reasoning_effort="none"`은 최대 128K, `"high"`는 최대 256K 토큰이고 vLLM 설정은 추론을 131,072로 제한한다. `max_tokens`가 추론과 답을 함께 센다. [확인]
- 빈 답이 오면 추론 중 `max_new_tokens`에 걸린 것이다. 한도를 올린다. Nota AI가 INT4·NVFP4·INT4-GlobalPruned 양자화 판을 냈고 커뮤니티 양자화는 15개다. [확인]
- Claude Code는 vLLM의 Anthropic 호환 `/v1/messages`로, Hermes Agent는 OpenAI 호환 `/v1`로 연결하는 예시가 있다. 한 블로그는 카드의 서빙 명령이 그대로는 안 된다고 지적했다. [확인 / 부분]

#### 2.3 행동 특성과 지침 문서를 쓰는 법
- 추론 흔적이 길어 `max_tokens`가 작으면 답이 잘린다. 한국어 평가 3개(Ko-AIME'25, KBank-MMLU, Ko-GDPval)는 사내 평가라 독립 검증되지 않았다. [확인: 카드 서술]
