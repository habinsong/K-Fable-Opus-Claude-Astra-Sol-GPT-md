# HyperCLOVA X SEED 8B Omni — 개요·사양·라이선스
> 제공자: Naver Cloud · 모델 ID: `naver-hyperclovax/HyperCLOVAX-SEED-Omni-8B` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/22-naver/hyperclova-x-seed-8b-omni/AGENTS.md`](../../../md/22-naver/hyperclova-x-seed-8b-omni/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 사양
- Naver Cloud가 2025-12-29 공개한 HyperCLOVA X 계열 최초의 any-to-any 옴니모달 모델이다. 기술 보고서 arXiv 2601.01792(2026-01-05). 라이선스는 "HyperCLOVA X SEED 8B Omni Model License Agreement". [확인: 카드 / 부분: arXiv 날짜]
- 8B 밀집(Hub는 F32 11B로 표기), 컨텍스트 32K, 지식 기준 2025-05. 입력 텍스트·이미지·비디오·오디오(음성), 출력 텍스트·이미지·오디오(음성)이고 비디오 생성은 없다. `skip_reasoning`이 기본 true, 온도 0.7. [확인]
- 평가 항목 이름: 텍스트(MMLU-Pro, GSM8K, KMMLU-Pro, HAERAE 1.0), 비전→텍스트(SEED-IMG, AI2D, K-MMBench), 텍스트→비전(GenEval, ImgEdit), 음성(LibriSpeech, Ksponspeech, FLEURS 영↔한). 점수는 이미지라 읽지 못했다. [확인: 이름 / 미확인: 점수]
