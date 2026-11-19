# Muse Ember — 비판적 평가·쓸 때와 쓰지 않을 때
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-ember-1.0`(2차 보도 표기, 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/10-muse/muse-ember/AGENTS.md`](../../../md/10-muse/muse-ember/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.4 비판적 평가 (독립 지표는 직접 읽은 한 사이트)
- **독립 지수 36(`max`, 같은 비교군 38개 중 2위, 중앙값 22), `xhigh` 34.** 작업당 비용 $0.14(Muse Wonder $6.95)이고 점수는 Wonder(44)의 82%다(계산). 비용 대비 효율은 좋다. [확인: 읽은 값]
- **같은 가격대에서 앞선다는 것은 점수가 낮다는 뜻이기도 하다.** 지수 36은 Fable 5.2(65)·GPT-6.2 Sol(57)·Gemini 4 Hydrogen(51)보다 한참 낮다. 어려운 문제에는 맞지 않는다. [확인: 읽은 값 / 추정]
- **Meta의 비교(Haiku, Luna, DeepSeek V4.1 Flash, GLM 5.3 Flash)는 모두 Meta의 주장이고 점수가 없다.** 독립 측정은 위 한 사이트뿐이다. [부분]
- **출력 가격 정보가 초기 보도에 빠져 있었다.** 입력 $0.10만 알려졌다가 Artificial Analysis에서 출력 $0.50이 확인됐다. 가격 인용은 출력 단가까지 확인한다. [확인]
- **Muse 계열은 이 저장소에서 권장하지 않는다.** 한국어 출력 품질과 일반 평가가 낮다.

#### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 대량·저지연 하위 작업(파일 읽기, 분류·추출, 도구 호출 반복), 상위 모델이 쪼갠 국소 수정.
- 쓰지 않는다: 설계·계획·어려운 디버깅, 사실 정확성이 결과를 좌우하는 조사.

## 재확인 (2026-11-19, 웹 검색, 사용자·후기 글)
- Ember 전용 개발자 후기는 찾지 못했다. Ember를 쓰는 Muse Code는 베타이고 Claude Code·Codex와의 격차를 아직 못 줄였다는 평, Meta가 장시간 작업 성공 주장의 분모를 공개하지 않았다는 분석이 있다. 출시일이 11-09와 11-11로 갈린다. [부분] ([eesel.ai Muse Code 리뷰](https://www.eesel.ai/blog/meta-muse-code-review), [myclaw](https://myclaw.ai/blog/muse-ember-review), [nxcode](https://www.nxcode.io/resources/news/meta-muse-code-recoverable-coding-agent-2026))
