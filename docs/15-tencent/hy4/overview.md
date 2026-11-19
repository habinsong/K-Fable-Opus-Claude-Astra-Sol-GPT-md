# Tencent Hy4 — 개요·사양·라이선스
> 제공자: Tencent(Hunyuan) · 모델 ID: `tencent/hy4`(OpenRouter 표기) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/15-tencent/hy4/AGENTS.md`](../../../md/15-tencent/hy4/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 사양
- Tencent Hunyuan의 플래그십이다. 미리보기(Hy4 Preview)는 2026-08-28, 전체 모델은 **2026-11-04**에 나왔다. 전체 모델에서 비전과 컴퓨터 사용(명령줄·GUI)이 새로 들어갔다. [부분: 2차 정리 한 곳(explainx)]
- 총 7,700억 파라미터의 MoE이고 활성은 미리보기 모델 카드 기준 490억이다(활성 비율 약 6.4%, 계산). 전체 모델의 활성 수는 확인하지 못했다. 컨텍스트 1M. [부분]
- **가격**(100만 토큰당): Tencent Cloud TokenHub 표준가 입력 RMB 6 / 출력 RMB 18 / 캐시 입력 RMB 0.3. 2026-12-31까지 50% 할인이라고 한다. OpenRouter의 Tencent Cloud 항목은 입력 $0.417 / 출력 $1.251로 RMB 3/9를 환율 약 7.19로 환산한 값과 맞는다(계산). [부분: 2차 / 확인: OpenRouter 읽은 값]
- 접근: Tencent Cloud TokenHub, OpenRouter(`tencent/hy4`), CodeBuddy, WorkBuddy. 미리보기 문서 기준으로 OpenAI Chat Completions, Responses, Anthropic Messages 형식을 지원한다고 한다. 사고(thinking) 모드가 기본이고 `reasoning_content` 필드가 있다. EU 지역 라우팅은 안 된다. [부분/확인]
- **가중치**: 미리보기는 Hugging Face에 Apache 2.0으로 공개됐다는 서술이 있다. 최종 모델의 가중치와 시스템 카드는 "예정"이고 확인되지 않았다. [부분/미확인]
