# HyperCLOVA X SEED 32B Think — 비판적 평가·쓸 때와 쓰지 않을 때
> 제공자: Naver Cloud · 모델 ID: `naver-hyperclovax/HyperCLOVAX-SEED-Think-32B` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/22-naver/hyperclova-x-seed-32b-think/general.md`](../../../md/22-naver/hyperclova-x-seed-32b-think/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.4 비판적 평가
- **점수가 이미지뿐이라 정량 비교가 불가능하다.** 같은 시기 K-EXAONE 2.0·A.X K2·Solar Open 2는 카드에 숫자 표를 싣는다. 이 모델은 비교 대상 모델명도 읽지 못했다. [확인: 부재]
- **정부 사업에서 가장 먼저 떨어진 팀 중 하나다**(2026-01-15). 같은 해 후속 SEED 계열은 4B(국방용 경량)로 갔다. [확인 / 부분]
- **다운로드가 적다.** 최근 한 달 6,897회, 좋아요 408(참고: Qwen3.8-27B는 월 약 689만 회). 커뮤니티 활동이 작아 도구·양자화 생태계가 얕다. [확인: 읽은 값]
- **128K 컨텍스트에 비디오 입력을 받지만 출력은 텍스트뿐이다.** [확인]

#### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 한국어 문화·맥락에 맞춘 비전-언어 추론을 국내 가중치로 시험할 때(라이선스 확인 후).
- 쓰지 않는다: 점수 근거가 필요한 선택, 상용 대규모 서비스(라이선스 제한), 도구 호출 에이전트.

## 재확인 (2026-11-19, 웹 검색, 사용자·후기 글)
- 독립된 사용자 후기를 찾지 못했다. 검색에 나온 것은 제조사 발표·출시 보도·판매 사이트 정리뿐이다. [확인: 부재]
- Artificial Analysis 지능 지수 17(같은 비교군 오픈 가중치 중앙값 9). Naver 블로그는 한국 문화·언어 지식에서 국내 텍스트 모델보다 약 10%p, 에이전트 도구 사용에서 다른 모델보다 15%p 높다고 밝혔다. KETI가 이 가중치로 만든 미세조정 판(HAECHI-32B)은 한국 문화유산 OCR·지식 시험에서 큰 향상을 보고했으나 제작자 자체 평가다. [부분: 벤더·제작자 주장] ([Artificial Analysis](https://artificialanalysis.ai/ko/models/hyperclova-x-seed-think-32b), [Naver 기술 블로그](https://clova.ai/en/tech-blog/hyperclova-x-omni-koreas-flagship-ai-on-the-road-to-omnimodality), [KETI HAECHI](https://huggingface.co/KETI-AIR/HyperCLOVA-X-KETI-HAECHI-32B))
