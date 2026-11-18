# Qwen3.8-27B — 비판적 평가·쓸 때와 쓰지 않을 때
> 제공자: Alibaba(Qwen) · 모델 ID: `Qwen/Qwen3.8-27B`(검색 결과의 Hugging Face 표기, 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/06-qwen/qwen3.8-27b/general.md`](../../../md/06-qwen/qwen3.8-27b/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.5 비판적 평가
- 강점 후보: 24 GB급 GPU에서 4비트로 도는 비전 언어 모델, 긴 컨텍스트, Apache 2.0이라는 서술(미확인), 독립 평가 점수 `xhigh` 52. 약점 후보: 독립 후기 부재, 라이선스 근거가 소수 출처, 벤더 수치가 특정 하네스 의존, 출력 속도가 느림(`xhigh`), 벤치마크 버전 혼재.
- 막히면 `qwen3.6-27b`와 비교하거나 상위 모델 문서(`02-claude/opus-5.5`, `gpt-6.1-sol`, `gemini-4-argon`)의 모델로 올린다.

## 재확인 (2026-11-19, 웹 검색, 사용자·후기 글)
- **긍정 사례(개인 보고, SEO 정리 글이 인용):** RTX 5090 사용자가 대부분의 작업에서 Claude가 더 필요 없다고 썼다. 4비트 양자화 판이 DeepSWE 한 과제에서 98% 통과했다는 보고(좁은 시험). 16GB RTX 5060 Ti로 OpenCode를 통해 NestJS 앱을 두 시간 자율 구축했다는 보고. [부분] ([codersera](https://codersera.com/blog/qwen-3-8-27b-complete-guide-2026/amp/), [wccftech](https://wccftech.com/27b-quantized-llm-matches-frontier-ai-models-coding-benchmark-task/))
- **부정·회의 사례:** "에이전트 코딩에 쓸모없어 보인다", "그냥 그저 그렇다"는 제목의 Reddit 글 두 건이 있으나 미러에 본문이 없다. 기본 추론 노력(`xhigh`)이 소비자 하드웨어에서 느리고 행동 전에 생각 메시지를 여러 번 낸다는 평가. M5 Max 48GB에서 Q4 GGUF가 약 15~30 tok/s. 세계 지식·창작은 약하고 실행기 역할에 맞는다는 평. [부분] ([Pedal Assist Coding](https://pac.commonsware.com/archive/qwen-38-quality-sans-speed/), [developersdigest](https://www.developersdigest.tech/blog/qwen-3-8-27b-local-agentic-coding-2026), [prismix 미러](https://prismix.dev/news/cb47225a6c62))
- 독립 평가 한 곳은 8월 말 기준 반복 에이전트 시험이 아직 없다고 했다. 원본 Reddit 스레드는 열지 못했고 정리 글은 SEO 성격이 많다. [부분] ([smartscope](https://smartscope.blog/en/blog/qwen3-8-27b-code-arena-webdev-2026/))
