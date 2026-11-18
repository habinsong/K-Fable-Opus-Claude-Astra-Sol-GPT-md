# Inkling 2 Small — 비판적 평가·쓸 때와 쓰지 않을 때
> 제공자: Thinking Machines Lab · 모델 ID: `inkling-2-small`(Cloudflare 표기) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/17-thinking-machines/inkling-2-small/general.md`](../../../md/17-thinking-machines/inkling-2-small/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.4 비판적 평가 (벤더 수치가 대부분, 독립 평가는 얕음)
- **벤더 벤치마크는 풍부하지만 비교 대상이 오픈 가중치 모델 위주다.** Artificial Analysis 지수 31(본문)·30.6(표). FrontierCode 2.0 25.4%(DeepSeek-V4.1-Flash 28.5, Kimi K3 17.3, GLM-5.3-Flash 17.6), DeepSWE v1.1 72.1%(DeepSeek 77.0, Kimi K3 68.5), SWE-Atlas v1.1 61.9%(DeepSeek 62.1), Vibe Code Bench v1.1 81.6%(DeepSeek 87.7), Terminal Bench Science v0.1 5.7%(DeepSeek 12.9), 비전은 MMMU Pro 81.6%·ScreenSpot Pro 83.8%·BabyVision 68.6%, 지식·추론은 HLE-Diamond 28.7%, ARC-AGI-2 81.7%(블로그 표기), BrowseComp 90.2%(압축 사용), AA-Omniscience 점수 16.1·비환각률 73.3%. [부분: 블로그 표를 요약 도구로 읽음, 벤더 보고]
- **코딩은 DeepSeek V4.1 Flash에 대체로 진다.** 한 리뷰는 터미널 벤치마크류에서 13.1% 대 33.8%로 졌다고 적었다. 블로그 표에서도 FrontierCode 2.0, DeepSWE, Vibe Code Bench, Terminal Bench Science에서 DeepSeek에 뒤진다. 비전·금융·정량 추론에서 앞선다는 것이 강점이다. [부분]
- **블로그 표 자체에 불일치가 있다.** 지수 31(본문) 대 30.6(표), DesignArena Website 1331(표) 대 1340(본문). 수치를 인용할 때 위치를 적는다. [확인: 읽은 값]
- **VentureBeat 표는 65B dense로 적었는데 다른 모든 출처와 맞지 않아 오류로 본다.** [부분]
- **이 저장소의 오픈 가중치 모델 평가는 그대로다.** 같은 크기대에서 DeepSeek V4.1 Flash에 코딩이 뒤지므로 코딩 기본 모델로 권장하지 않는다. [추정]

#### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 이미지·차트·문서 이해, 금융·정량 분석, 서버급 장비에서 Apache 2.0 가중치를 미세조정할 때.
- 쓰지 않는다: 터미널 코딩 에이전트의 기본 모델, 개인 장비 로컬 실행, 간결한 채팅.

## 재확인 (2026-11-19, 웹 검색, 사용자·후기 글)
- 상업적 이해가 있는 리뷰(eesel.ai, 에이전트 도구 회사) 한 편이 있다: 장시간 에이전트 작업에는 비용이 합리적이고 환각이 이전보다 줄었으나 0은 아니며 SWE-bench Verified는 Inkling-Small 80.2에서 82.2로 2점 상승에 그친다고 썼다. 이 수치는 우리가 읽은 공식 블로그 표(SWE-bench Pro v2 등)와 다른 지표다. 제목에 "여전히 비공개"라고 있어 가중치 공개(11-12) 이전에 쓴 것으로 보인다. SourceForge의 5점 후기는 1세대 모델에 대한 것이다. [부분] ([eesel.ai](https://www.eesel.ai/blog/inkling-2-small-review), [SourceForge](https://sourceforge.net/software/product/Inkling-Small/))
