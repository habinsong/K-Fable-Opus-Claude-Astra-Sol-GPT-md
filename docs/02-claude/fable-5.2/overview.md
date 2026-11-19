# Claude Fable 5.2 — 개요·사양·라이선스
> 제공자: Anthropic · 모델 ID: `claude-fable-5-2` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/02-claude/fable-5.2/CLAUDE.md`](../../../md/02-claude/fable-5.2/CLAUDE.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 사양
- Anthropic은 대부분의 워크로드를 Opus 5.5로 시작하고, 어려운 추론·장시간 에이전트 작업이거나 Opus 5.5의 높은 effort로도 평가 기준에 못 미칠 때 Fable 5.2를 쓰라고 안내한다. 2026-11-09 출시, API ID `claude-fable-5-2`. [확인]
- **Claude Mythos 5.2**는 같은 사양·가격의 모델로, Anthropic의 검증 프로그램(사이버 검증 프로그램 등)을 통과한 조직만 쓴다. 이 폴더의 대상이 아니다. 이전 세대와 같은 구조다. [확인]
- 가격은 입력 $8 / 출력 $40(100만 토큰당)으로 Fable 5.1($10/$50)보다 20% 낮다. 5분 캐시 쓰기 $10, 1시간 $16, 캐시 읽기 $0.20(입력가의 2.5%), 배치 $4/$20. Fast 모드(최대 2.5배 빠름)는 $16/$80이고 미국 내 추론 한정은 1.1배다. [확인: 모델 페이지·What's new / 부분: Fast 배율·1.1배(Anthropic 제품 페이지 서술)]
- 컨텍스트 1M, 최대 출력 128K, 지식 컷오프 2026-06. 응답 속도 등급은 "Moderate"로 Fable 5.1의 "Slower"보다 빨라졌다(Opus 5.5와 같은 등급). 퇴역은 2027-11-09 이전에는 없다. 기본 effort는 `high`, 단계는 `low`·`medium`·`high`·`xhigh`·`max`. 적응형 추론이 항상 켜져 있다. [확인]
- 가용성: Claude API, Amazon Bedrock(`bedrock-runtime` 엔드포인트), Google Cloud(Anthropic 관리·Google 관리), Microsoft Foundry, Claude Platform on AWS. 구독은 Pro·Max·Ultra·Team·Enterprise. [확인/부분]
- 30일 데이터 보관이 필수이고 명시적으로 승인받지 않으면 ZDR(보관 없음) 대상이 아니다. 사이버·생물 안전장치가 있어 걸린 요청은 거부되거나 덜 유능한 모델로 라우팅될 수 있다. 대체 모델은 Opus 4.8·Opus 5다. [확인]
