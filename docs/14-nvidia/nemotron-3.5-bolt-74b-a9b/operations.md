# Nemotron 3.5 Bolt 74B-A9B 24GB — 운용
> 제공자: NVIDIA · 모델 ID: `nvidia/Nemotron-3.5-Bolt-74B-A9B-24GB`(저장소 표기 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/14-nvidia/nemotron-3.5-bolt-74b-a9b/general.md`](../../../md/14-nvidia/nemotron-3.5-bolt-74b-a9b/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.2 API·배포·로컬 실행
- llama.cpp(GGUF)는 RTX Spark에서, vLLM은 DGX Spark에서 쓴다. 테스트 장비는 RTX Spark 노트북이다. 그 밖의 GPU(RTX 4090 24GB 등)에서의 실측은 찾지 못했다. [확인 / 미확인]
- **같은 하드웨어 비교(llama.cpp, NVIDIA 측정):** Bolt 83.99 TPS·AA-AgentPerf 재생 600.80초, Qwen3.6 35B-A3B(UD-Q4_K_M + MTP) 96.63 TPS·453.97초, Gemma 4 26B-A4B(UD-Q4_K_M + MTP) 100.56 TPS·480.68초, Qwen3.8 27B(UD-Q4_K_M + DFlash) 28.26 TPS·1,043.28초. 재생 시간의 우열 방향은 페이지에 없다(짧을수록 빠르다고 추정). [확인: 읽은 값 / 추정]

#### 2.3 행동 특성과 지침 문서를 쓰는 법
- 정확도는 NVIDIA 그림(이미지)으로만 있다. 숫자 점수가 페이지 본문에 없다. [확인: 부재]
