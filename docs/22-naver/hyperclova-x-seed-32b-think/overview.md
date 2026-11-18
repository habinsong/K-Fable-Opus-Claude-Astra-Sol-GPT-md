# HyperCLOVA X SEED 32B Think — 개요·사양·라이선스
> 제공자: Naver Cloud · 모델 ID: `naver-hyperclovax/HyperCLOVAX-SEED-Think-32B` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/22-naver/hyperclova-x-seed-32b-think/general.md`](../../../md/22-naver/hyperclova-x-seed-32b-think/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.1 위치와 사양
- Naver Cloud가 2025-12-29 공개한 오픈 가중치 비전-언어 추론 모델이다. 기술 보고서 arXiv 2601.03286(2026-01-03). 정부 사업은 2026-01-15에 탈락했다. 이전 모델은 SEED Think 14B. 라이선스는 "HyperCLOVA X SEED 32B Think Model License Agreement"이고 대기업·경쟁사 제한이 있다는 트래커 서술이 있다(조항은 카드에 없음). [확인: 모델 카드 / 부분: 제한 서술]
- 32B 밀집(Hub 표기 33B), BF16, 컨텍스트 128K, 지식 기준 2025-05. 입력 텍스트·이미지·비디오, 출력 텍스트. `<think>` 추론 모드와 다중 턴을 지원한다. [확인]
- 한국어 시험 이름(KoBalt, CLIcK, HAERAE 1.0), 비전(ChartVQA, TextVQA, K-MMBench, K-DTCBench), 에이전트(Tau²-Airline/Retail/Telecom)를 평가했다고 하지만 점수표가 이미지라 숫자를 읽지 못했다. [확인: 이름 / 미확인: 점수]
