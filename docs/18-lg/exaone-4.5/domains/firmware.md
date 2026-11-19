# EXAONE 4.5 · 펌웨어 — 조사 기록
> 제공자: LG AI Research · 모델 ID: `LGAI-EXAONE/EXAONE-4.5-33B`(저장소 표기 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/18-lg/exaone-4.5/firmware.md`](../../../../md/18-lg/exaone-4.5/firmware.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/firmware.md`](../../../_common/domain-rules/firmware.md)

## 2. 이 모델의 펌웨어 작업 운용
EXAONE 4.5의 펌웨어 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- LiveCodeBench v6 81.4(Qwen3.5 27B 80.7), 코딩 에이전트 지표는 제시하지 않았다.
- GPQA-Diamond 80.5, MMLU-Pro 83.3, AIME 2026 92.6, KMMLU-Pro 67.6, KoBALT 52.1.

**펌웨어 작업에서 따로 확인할 것**
- 레지스터·타이밍 수치의 환각 빈도, 장치 쓰기 전 승인 규칙 준수, 크로스 컴파일 도구 호출를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **에이전트형 코딩은 직접 시험한 뒤 맡긴다.** 함수 단위 생성 지표만 있고 저장소 단위 평가가 없다. [부분]
- **공개 가중치의 이용 범위가 연구·교육용이다.** 제품에 넣기 전에 라이선스 원문을 확인한다. [부분: 보도]

## 4. 근거와 한계
- [GitHub EXAONE-4.5](https://github.com/LG-AI-EXAONE/EXAONE-4.5)
- [Taiwan News](https://www.taiwannews.com.tw/news/6337738)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: EXAONE 4.5 33B](https://artificialanalysis.ai/zh/models/exaone-4-5-33b)
- 추가 확인(2026-11-19 웹 검색): [Korea Times: EXAONE 4.5](https://www.koreatimes.co.kr/amp/business/20260409/lg-unveils-multimodal-ai-model-that-outperforms-global-rivals)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 펌웨어 작업을 직접 측정한 것이 아니다.
