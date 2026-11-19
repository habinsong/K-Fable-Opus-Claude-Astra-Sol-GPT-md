# Kanana-2 (30B-A3B) — 비판적 평가·쓸 때와 쓰지 않을 때
> 제공자: Kakao · 모델 ID: `kakaocorp/kanana-2-30b-a3b-instruct`(기반 `-base`, 추론 `-thinking`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/23-kakao/kanana-2/AGENTS.md`](../../../md/23-kakao/kanana-2/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.4 비판적 평가
- **지시 모델은 Qwen3-30B-A3B-Instruct-2507에 대부분 진다.** MMLU 80.80 대 87.13, GPQA-Diamond 42.93 대 54.55, MATH 86.26 대 90.96, HumanEval+ 79.88 대 86.59, BFCL-v3 Multi-Turn 35.38 대 38.77, Multi-Challenge 34.80 대 41.76. 앞선 항목: IFEval 84.47(82.62), IFBench 41.84(30.27), BFCL-v3 Live 74.30(73.93), HAERAE 75.57(53.41). KMMLU 67.32는 67.56과 사실상 같다. [확인: 읽은 값, 벤더 보고]
- **추론 모델도 같은 경향이다.** AIME 2024 78.3 대 91.0, GPQA-Diamond 61.3 대 70.6, LiveCodeBench 60.8 대 68.3, BFCL-v3 Multi-Turn 34.3 대 53.6. [확인: 읽은 값]
- **비교 대상이 2025년 7월 Qwen3-30B-A3B다.** 같은 시기(2026년 가을) 모델과의 비교가 없다. Qwen3.6-35B-A3B·Raon-1 mini·Gemma 4 26B-A4B와 비교한 자료도 없다. [확인: 부재]
- **사용량이 작다.** 최근 한 달 3,103회 다운로드, 좋아요 48. [확인: 읽은 값]

#### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 한국어 지시 수행·한국어 지식(HAERAE)이 중요한 소형 MoE 자체 호스팅, Kakao 생태계 연구.
- 쓰지 않는다: 영어 지식·코딩·수학·다중 턴 도구 호출 중심 작업, 같은 크기의 최신 모델이 필요한 경우.

## 재확인 (2026-11-19, 웹 검색, 사용자·후기 글)
- 독립된 사용자 후기를 찾지 못했다. 검색에 나온 것은 제조사 발표·출시 보도·판매 사이트 정리뿐이다. [확인: 부재] Kakao는 업데이트된 Kanana-2가 Qwen-30B-A3B-Instruct-2507보다 지시 수행·다중 턴 도구 호출·한국어에서 낫다고 밝혔으나 우리가 카드에서 읽은 표(Qwen에 대부분 짐)와 방향이 달라 보인다. 어느 시험 설정인지 확인이 필요하다. [부분: 벤더 주장 / 충돌] ([Kakao 보도](https://www.kakaocorp.com/page/detail/11904?lang=ENG), [Korea Times](https://www.koreatimes.co.kr/amp/business/tech-science/20260120/kakao-updates-kanana-2-releases-4-open-source-models))
- [BestLLMfor 카탈로그](https://bestllmfor.com/catalog/kanana-2-30b/): Q8_0 33GB, FP16 60GB, Q4_K_M 약 18GB VRAM(방법론 없는 추정). 한 한국어 블로그는 같은 이름의 Kanana-2 30B-A3B 계열이 여러 저장소에 나뉘어 있고 소형 1.3B·3B 모델과 헷갈리기 쉬우니 저장소 이름을 확인하라고 경고했다. [부분] ([braindetox](https://braindetox.kr/en/posts/kakao_kanana2_open_models_2026.html))
