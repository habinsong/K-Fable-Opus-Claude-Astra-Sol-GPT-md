# EXAONE 4.5 — 비판적 평가·쓸 때와 쓰지 않을 때
> 제공자: LG AI Research · 모델 ID: `LGAI-EXAONE/EXAONE-4.5-33B`(저장소 표기 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/18-lg/exaone-4.5/AGENTS.md`](../../../md/18-lg/exaone-4.5/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.4 비판적 평가
- **같은 크기의 Qwen3.5 27B에 대부분 진다.** 비전: MMMU 78.7 대 82.3, MathVision 75.2 대 86.0, BabyVision 18.8 대 44.6, OmniDocBench v1.5 81.2 대 88.9. 언어: GPQA-Diamond 80.5 대 85.5, τ2-Bench Telecom 73.0 대 99.3, AA-LCR 50.6 대 67.3. 이긴 항목은 거의 없고 AIME 2026(92.6 대 90.8)과 LiveCodeBench v6 81.4(80.7)뿐이다. [확인: 읽은 값, 벤더 보고]
- **GPT-5 mini(high)와는 비슷하다.** MMMU 78.7 대 79.0, MMMU-Pro 68.6 대 67.3, AIME 2026 92.6 대 92.4. 반면 AA-LCR 50.6 대 68.0, KRETA 91.9 대 94.8로 장문·한국어 시각 평가는 뒤진다. [확인: 읽은 값]
- **한국어 지표가 강점이 아니다.** KMMMU 42.7, KMMLU-Pro 67.6, KoBALT 52.1이고 Qwen3.5 27B는 51.7 / 73.0 / 54.9다. [확인: 읽은 값]
- **비상업 라이선스 때문에 서비스에 쓰기 어렵다.** 같은 K-EXAONE 2.0(Apache 2.0)과 대비된다. [확인]

#### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 연구·학습 목적의 한국어·시각 비교 실험, 라이선스 조건이 맞는 비상업 환경.
- 쓰지 않는다: 상용 서비스(비상업 라이선스), 같은 크기에서 더 높은 점수가 필요한 시각·문서 작업(Qwen3.5 27B나 Qwen3.8-27B가 대체로 앞선다).

## 재확인 (2026-11-19, 웹 검색, 사용자·후기 글)
- 비상업 라이선스에 대한 불만 글이나 실사용 후기를 찾지 못했다. 한국어 블로그 리뷰는 기술 보고서(문서·OCR·차트·STEM·한국어 멀티모달, 한국어 학술 텍스트를 고해상도 이미지로 렌더링하는 text-to-vision 증강)를 소개하는 글이다. [확인: 부재]
- Artificial Analysis는 이 모델을 34.4B(비추론 판)로 적어 공식 카드의 33B와 다르다. 비추론 판이 별도로 있는 것으로 보인다. [부분: 검색 요약]
- 출처: [한국어 기술 보고서 리뷰](https://dimensionstp.github.io/study-concept/exaone_4_5/), [Artificial Analysis 비추론 판](https://artificialanalysis.ai/ko/models/exaone-4-5-33b-non-reasoning)
