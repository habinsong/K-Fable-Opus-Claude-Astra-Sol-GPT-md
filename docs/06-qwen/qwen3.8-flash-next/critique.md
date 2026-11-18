# Qwen3.8-Flash-Next — 비판적 평가·쓸 때와 쓰지 않을 때
> 제공자: Alibaba(Qwen) · 모델 ID: `Qwen/Qwen3.8-Flash-Next` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/06-qwen/qwen3.8-flash-next/general.md`](../../../md/06-qwen/qwen3.8-flash-next/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.4 비판적 평가
- **같은 계열 27B 밀집 모델보다 코딩·에이전트가 확실히 높다.** DeepSWE 1.1 58.7(27B 42.2), SWE-bench Pro 62.5(61.7), SWE-bench Multilingual 81.0(73.8), JobBench 55.7(33.4), CoWorkBench 73.9(70.7), Agents' Last Exam 51.2 점수(42.9), Toolathlon 73.5(67.1). GPQA-Diamond 91.7(89.2), LiveCodeBench v6 91.9(90.3). [확인: 읽은 값, 벤더 보고]
- **DeepSeek-V4-Flash-0731·Claude Opus 4.6 Max와 비교한다.** SWE-bench Pro 62.5는 DeepSeek 56.0, Opus 4.6 53.4보다 높다. NL2Repo-Bench 48.1은 DeepSeek 54.2에 뒤지고 HLE 35.9는 Opus 4.6 40.0에 뒤진다. 비교 대상이 2026년 중반 모델이라 최신 폐쇄 모델(Fable 5.2, Opus 5.5)과는 비교되지 않았다. [확인: 읽은 값]
- **비전 평가에서 27B를 앞선다.** ClawEval-MM Pass@3 64.4(57.4), AndroidWorld 84.5(81.9), ERQA 72.3(65.5), RealWorldQA 88.5(85.9), MathVision(CI 포함) 95.7(94.6). OSWorld 2.0 Binary 19.4는 27B와 같다. [확인: 읽은 값]
- **총 180B라 27B처럼 개인 GPU 한 장에 올릴 수 없다.** 활성 6B라 추론은 빠르지만 메모리는 175B급이다. [확인 / 추정]
- **라이선스가 qwen-community-1.0이다.** 이 저장소의 `qwen3.8-27b`(Apache 2.0)와 다르다. 상업 이용 조건을 원문으로 확인해야 한다. [확인: 이름 / 미확인: 조항]

#### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 서버·고메모리 워크스테이션(약 100GB급 양자화)에서 코딩·에이전트 오픈 가중치를 쓰고 싶을 때, 이미지·비디오 입력이 필요할 때.
- 쓰지 않는다: 24GB급 개인 GPU(Qwen3.8-27B를 쓴다), 라이선스 조항 확인 전 상업 서비스.

## 재확인 (2026-11-19, 웹 검색, 사용자·후기 글)
- **r/LocalLLaMA 미러의 로컬 에이전트 코딩 시험(RTX PRO 6000, 10개 시험):** Flash-Next NVFP4가 535, 27B NVFP4가 700으로 27B가 앞섰다. 4×RTX 3090 사용자는 하위 에이전트에 일을 맡기는 에이전트 코딩에서 27B FP16이 Flash-Next INT4보다 낫고 Flash-Next는 속도가 중요한 대화용에 맞는다고 평했다. 카드의 SWE-bench Pro(62.5 대 61.7) 우위와 방향이 다르다. [부분: 단일 시험 / 충돌] ([prismix 미러](https://prismix.dev/news/b1a8a4391beb), [MindStudio](https://www.mindstudio.ai/blog/qwen-3-8-27b-vs-flash-next-local-agents))
- **메모리가 핵심 제약이다.** Unsloth 안내: RAM+VRAM 합계가 2비트 79GB, 3비트 90GB, 4비트 96~114GB. 24GB Mac에서는 안 되고 24GB GPU에서는 llama.cpp 전문가 오프로드로 시스템 RAM에 전문가를 올려야 한다. 이론 희소성이 실제 속도를 보장하지 않는다는 분석. 출시 메가스레드는 650개 이상 댓글. [부분] ([eesel.ai 리뷰](https://www.eesel.ai/blog/qwen38-flash-next-review), [MindStudio](https://www.mindstudio.ai/blog/qwen-3-8-27b-vs-flash-next-local-agents))
