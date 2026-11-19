# MiMo-V2.6-Flash — 비판적 평가·쓸 때와 쓰지 않을 때
> 제공자: Xiaomi · 모델 ID: `XiaomiMiMo/MiMo-V2.6-Flash`(RL 판 `-RL`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/26-xiaomi/mimo-v2.6-flash/AGENTS.md`](../../../md/26-xiaomi/mimo-v2.6-flash/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.4 비판적 평가
- **코딩·터미널 점수가 대형 폐쇄 모델에 근접한다(Xiaomi 시험).** Terminal Bench 2.1 87.6(Claude Opus 5 89.1), DeepSWE v1.1 67.9(Pro 71.9, Opus 5 74.0, GPT-5.6 Sol 73.0, Fable 5 70.0), AutomationBench 52.3(GPT-5.6 Sol 45.8, Opus 5 50.3보다 높음), Toolathlon-Verified 73.6(Pro 76.9, Opus 5 80.6). 활성 150억 모델이 Opus 5 점수의 98%(Terminal Bench), 92%(DeepSWE)다(계산). [확인: 읽은 값, 벤더 보고]
- **보안 공격 평가는 약하다.** ExploitGym 6.0(Opus 5 22.1), ExploitBench 25.3(70.0), SEC Bench Pro 47.5(GPT-5.6 Sol 79.1). CyberGym 95.1은 Pro(94.0)보다 높다. [확인: 읽은 값]
- **벤치마크가 모델 카드의 혼합 평가다.** 한 정리는 Xiaomi의 출시 표가 공개 평가와 내부 평가를 섞었다고 지적한다. DeepSWE v1.1은 같은 모델이 65.68(RL 대시보드 이전 스냅샷)과 67.9(최종)로 적혀 있어 어느 값을 인용하는지 밝혀야 한다. [확인 / 부분]
- **독립 지수는 Pro만 46(Artificial Analysis)이고 Flash 점수는 찾지 못했다.** [부분]
- **이 저장소의 Hugging Face 직접 열람이 막혔다.** 모든 사양은 정리 글(OrcaRouter)이 모델 카드를 옮긴 것이다. [부분]

#### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 서버급 GPU가 있는 환경에서 MIT 라이선스의 고성능 코딩·에이전트 오픈 모델이 필요할 때, 멀티모달(오디오 포함) 입력이 필요할 때.
- 쓰지 않는다: 개인 장비 로컬 실행(173 GB), 공격 보안 코드 생성, 카드 원문 확인 없이 쓰는 구축.

## 재확인 (2026-11-19, 웹 검색, 사용자·후기 글)
- **Flash 전용 사용자 후기가 없다.** 후기 집계 페이지가 "첫 후기를 남겨 달라"고 표시한다. Pro 후기는 "5분간 멈췄다"는 초기 보고가 있다. Flash 코딩 순위는 한 집계에서 422개 중 234위로 낮다. Xiaomi 자체 학습 기록은 코드 RL에서 온라인 그룹 채점이 없으면 에이전트 턴 수와 생성 길이가 급증했다고 밝혀 길고 토큰을 많이 쓰는 에이전트 실행의 위험을 시사한다. [부분] ([aireiter Pro 후기](https://aireiter.com/blog/mimo-v2-6-pro-review-tested), [benchlm](https://benchlm.ai/models/mimo-v2-6-flash), [VentureBeat](https://venturebeat.com/technology/better-than-deepseek-xiaomis-mimo-v2-6-pro-debuts-as-the-top-open-weights-model-in-the-world-alongside-cheaper-v2-6-flash))
