# Qwen3.8-27B — 개요·사양·라이선스
> 제공자: Alibaba(Qwen) · 모델 ID: `Qwen/Qwen3.8-27B`(검색 결과의 Hugging Face 표기, 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/06-qwen/qwen3.8-27b/general.md`](../../../md/06-qwen/qwen3.8-27b/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 사양
- 2026-08-14 Qwen 조직이 Hugging Face에 공개한 **밀집 27B 비전 언어 모델**이다. 네이티브 컨텍스트 262,144 토큰(YaRN으로 약 100만까지 확장), 스택의 4분의 3에 선형 어텐션을 써서 긴 컨텍스트 비용을 줄였다는 서술이 있다. 입력은 이미지를 포함한다. [부분]
- **라이선스는 Apache 2.0이라는 서술이 두 곳(저장소가 표준 Apache License 2.0을 싣는다는 서술 포함)에 있다.** 반면 출시 전후의 다른 글은 Apache 2.0이 확실하지 않고 과거 일부 Qwen 릴리즈가 월간 활성 사용자 1억 명 임계값이 있는 "Tongyi Qianwen" 라이선스를 썼다고 지적했다. 같은 세대의 2.4T 체크포인트는 자체 라이선스다. 근거가 소수 출처라 저장소의 LICENSE 원문으로 확인하기 전에는 단정하지 않는다(§1.5). [부분, 충돌]
- **추론이 기본으로 켜져 있어 샘플링을 다시 조정해야 한다**는 서빙 안내가 있다(`vllm serve Qwen/Qwen3.8-27B --max-model-len 262144` 예시). 추론/비추론 전환 방법과 기본 샘플링 값은 모델 카드로 확인한다. [부분/미확인]
- **메모리**: BF16 가중치가 약 55.6 GB(가중치만, 긴 컨텍스트의 KV 캐시는 별도), 4비트 양자화하면 24 GB GPU(RTX 3090·4090)에 들어간다는 서술이 있다. 모든 정밀도에서 Blackwell 한 장에 들어간다는 서술도 있어 일치하지 않는다. 대상 기기에서 컨텍스트 길이별로 실측한다. [부분, 충돌]

## 재확인 (2026-11-19, Hugging Face 모델 카드 직접 읽기)
- [Qwen/Qwen3.8-27B 모델 카드](https://huggingface.co/Qwen/Qwen3.8-27B): 27B 밀집(Hub 표기 28B), 비전 인코더 포함. 64층 = 16 × [Gated DeltaNet → FFN] 3번 + [Gated Attention → FFN] 1번, 은닉 5,120, FFN 17,408, 어휘 248,320. Gated DeltaNet V 48 / QK 16 헤드(차원 128), Gated Attention 질의 24 / KV 4(차원 256). 컨텍스트 262,144 → 1M(YaRN). Apache 2.0. 이미지·비디오 입력(시간 단위 비디오). [확인]
- 벤더 벤치마크(Qwen 하네스): Terminal Bench 2.1 73.0(Claude Opus 4.6 Max 78.2), SWE-bench Pro 61.7(Opus 4.6 53.4), NL2Repo 42.3(47.6), DeepSWE 1.1 42.2, GPQA-Diamond 89.2(91.3), HLE 30.8(40.0), LiveCodeBench v6 90.3, IFBench 79.5(62.5), OSWorld-Verified 84.3(Opus 4.6 72.7), WebArena-Verified 64.8, AndroidWorld 81.9, BabyVision(CI) 85.6(12.6), CharXiv RQ(CI) 90.2. 직전 Qwen3.6-27B 대비 Terminal Bench 63.4에서 73.0(+9.6), SWE-bench Pro 53.5에서 61.7(+8.2), DeepSWE 13.3에서 42.2(3.2배)(계산). [확인: 읽은 값, 벤더 보고]
- 추론 노력 `xhigh`(기본) / `medium` / `low`, 최대 출력 추론 262,144·최종 응답 131,072 권장. 샘플링: 추론 모드 온도 1.0, top_p 0.95, top_k 20, presence 0.0; 비추론 모드 0.7 / 0.80 / 20 / 1.5. 최근 한 달 다운로드 약 689만 회, Hub 양자화 모델 1,860개. 카드에 하드웨어 요구량은 없다. [확인]
- 가중치 메모리(파라미터 × 바이트, 계산): BF16 약 54GB, 8비트 약 27GB, 4비트 약 14~17GB(2차 가이드 값과 일치). NVIDIA 측정(RTX Spark, llama.cpp, UD-Q4_K_M + DFlash)은 28.26 TPS, AA-AgentPerf 재생 1,043.28초로 Qwen3.6 35B-A3B(96.63 TPS)·Gemma 4 26B-A4B(100.56 TPS)보다 느리다. [확인 / 추정]
- 독립 지수가 서로 다르다: 한 리뷰는 Artificial Analysis v4.1 52.0, 다른 리뷰(10월 15일 확인)는 34로 적었다. 어느 쪽인지 확인하지 못했다. [충돌]
