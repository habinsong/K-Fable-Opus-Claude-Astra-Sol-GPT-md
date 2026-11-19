# Tencent Hy4 — 비판적 평가·쓸 때와 쓰지 않을 때
> 제공자: Tencent(Hunyuan) · 모델 ID: `tencent/hy4`(OpenRouter 표기) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/15-tencent/hy4/AGENTS.md`](../../../md/15-tencent/hy4/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.4 비판적 평가 (벤더 수치와 2차 정리, 독립 평가는 얕음)
- **Tencent 자체 12개 벤치마크.** 7개 모델을 Tencent가 자기 설정으로 돌렸고 Hy4는 대부분 3~4위다. FrontierCode 2.0 31.0(1위 Claude 46.4), Terminal Bench 4.0 44.4(1위 Kimi 66.8), OSWorld 2.1 78.9(1위 Claude 81.8), ProgramBench 30.0(1위 Claude Opus 5.5 56.5), Terminal Bench Science 19.8(1위 GPT 60.9), Hy-FrontierMath T5 13.0(GPT-6.1 Sol 97.5), Goal2Repo 23.2(Claude 74.0). Kimi K3.1 Pro와는 12개 중 6개씩 갈렸다. [부분, 벤더 주장]
- **독립 평가.** Artificial Analysis 지수 34.6(OpenRouter 목록 인용), CWE-Bench-AA 75.8% pass@1(120과제, 과제당 2시간 제한; DeepSeek V4.1 Flash 69.2%, Grok 4.7 68.3%). Collinear CWE-bench는 250과제에서 64.1%로 7위(Claude Code 하네스; Fable 5.2가 75.0%). 최종 모델에 대한 독립 종합 평가는 없다. [부분]
- **지수 34.6은 같은 사이트에서 읽은 Qwen4-Max 43, Muse Ember 36보다 낮다.** 큰 파라미터가 점수로 이어지지 않았다. 지수 버전이 같은지는 확인하지 못했다. [부분/추정]
- **"오픈"은 최종 모델에 대해 아직 확인되지 않았다.** 미리보기만 Apache 2.0이다. [부분]
- **출시 첫날 수요 폭주로 한도 부족과 속도 문제가 있었다.** [부분]

#### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 값싼 에이전트·컴퓨터 사용 실험, 보안 취약점 점검 보조, Tencent 생태계(WorkBuddy, CodeBuddy) 안에서의 작업.
- 쓰지 않는다: 큰 저장소 대규모 변경, 고난도 수학, 외부 전송이 금지된 코드·데이터, 한국어 윤문.

## 재확인 (2026-11-19, 웹 검색, 사용자·후기 글)
- 실사용 후기는 얕다. 한 실무 글(wavect)은 긴 컨텍스트·다단계 도구 사용·반복 저장소 검색이 병목이면 통제된 코딩 에이전트 시범은 할 만하지만 모든 상용 워크플로의 안전한 기본값은 아니라고 평했다(날짜가 11월 출시 보도와 맞지 않는 미리보기 기준 글). Tencent가 감사받은 독립 벤치마크를 공개하지 않았다는 보도, 수요 폭주로 추론 클러스터를 10배로 늘렸다는 서술이 있다. [부분] ([wavect](https://wavect.io/blog/tencent-hy4-preview-coding-agent-review/), [SCMP](https://www.scmp.com/tech/big-tech/article/3366068/tencents-hy4-model-gains-open-source-ai-rankings-after-ecosystem-driven-training))
