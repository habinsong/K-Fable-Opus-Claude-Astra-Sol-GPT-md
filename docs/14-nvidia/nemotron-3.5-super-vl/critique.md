# Nemotron 3.5 Super VL — 비판적 평가·쓸 때와 쓰지 않을 때
> 제공자: NVIDIA · 모델 ID: `nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16`(Hugging Face), `nvidia/nemotron-3.5-super-vl`(OpenRouter) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/14-nvidia/nemotron-3.5-super-vl/general.md`](../../../md/14-nvidia/nemotron-3.5-super-vl/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.4 비판적 평가 (모델 카드는 벤더 수치, 독립은 지수 한 개)
- **독립 지수 26.** Artificial Analysis는 미국 오픈 가중치 모델 중 최상위이고 이전 Nemotron 3 Super(13)의 두 배, 출력 토큰은 약 60% 적다고 적었다. Nemotron 3 Ultra에는 못 미친다. 같은 사이트의 다른 모델은 Mistral Large 4 26, Qwen4-Max 43, Fable 5.2 65다. [부분: X 게시글을 전한 검색 요약]
- **모델 카드 벤치마크(BF16, NVIDIA 보고):** GPQA-Diamond 89.52, HLE(텍스트) 31.79, LiveCodeBench v6 88.22, SWE-bench Verified 71.10, SWE-bench Pro 51.78, Terminal-Bench 2.1 60.67, BrowseComp 78, tau2-bench retail/airline/telecom 69.24/76.50/73.19, AA-LCR 68.62, IFBench 70.86, MMLongBench-Doc 62.82, CharXiv 추론 80.82, OSWorld-Verified 51.14. 일부는 NeMo Gym 표준 하네스가 아니라 내부 스캐폴딩이나 공개 구현으로 돌렸다. [확인: 읽은 값, 벤더 보고]
- **약한 항목.** Video-MME v2 32.85, OCRBench v2 중국어 59.15, AA-Omniscience 4.03(환각 가능성). 비디오 이해는 약하다. [확인: 읽은 값]
- **VentureBeat 제목은 Opus 5와 GPT-6.1 Sol을 이겼다고 하나 "특화 과제 후학습" 조건이다.** 일반 능력 비교가 아니다. 이 문서는 그 비교를 검증하지 못했다. [부분]
- **속도 주장(최대 5배, 10,000 코딩 과제 4배 빠름, Dynamo로 사용자 8배)은 NVIDIA 자체 주장이다.** [부분, 벤더 주장]

#### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 서버급 GPU가 있는 환경의 문서·이미지·화면 이해(에이전트 작업), 후학습 데이터를 가진 특화 과제, 오픈 데이터·레시피가 필요한 연구.
- 쓰지 않는다: 개인 장비 실행(Bolt 계열 대상), 한국어 윤문, 비디오 이해 중심 작업.

## 재확인 (2026-11-19, 웹 검색, 사용자·후기 글)
- Artificial Analysis 지능 지수 26.5로 40B~150B 오픈 가중치 67개 중 1위라는 보도. 개인 사용자 후기는 찾지 못했다. 이전 모델 Nemotron 3 Super를 DGX Spark로 쓴 개발자 포럼 글은 Qwen3.5-122B 대비 뚜렷한 이점을 찾기 어렵고 비전이 없다고 했다. 120B 모델은 노트북 작업 부하가 아니다. [부분] ([The Neuron](https://www.theneuron.ai/news/nvidia-nemotron-3-5-bolt-super-vl-review/), [NVIDIA 포럼](https://forums.developer.nvidia.com/t/nvidia-nemotron-3-super-120b-a12b-nvfp4/363175?page=2))
