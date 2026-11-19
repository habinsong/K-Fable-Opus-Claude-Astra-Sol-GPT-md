# EXAONE 4.5 · 네이티브 — 조사 기록
> 제공자: LG AI Research · 모델 ID: `LGAI-EXAONE/EXAONE-4.5-33B`(저장소 표기 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/18-lg/exaone-4.5/native.md`](../../../../md/18-lg/exaone-4.5/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
EXAONE 4.5의 네이티브 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- LiveCodeBench v6 81.4(Qwen3.5 27B 80.7), 코딩 에이전트 지표는 제시하지 않았다.
- 33B 밀집. 256K 컨텍스트에 H200 1장 또는 A100-40GB 4장. Q4_K_M GGUF. 비상업 라이선스.

**네이티브 작업에서 따로 확인할 것**
- 메모리 안전·동시성 버그 진단 정확도, 디버거·새니타이저 출력의 해석를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **에이전트형 코딩은 직접 시험한 뒤 맡긴다.** 함수 단위 생성 지표만 있고 저장소 단위 평가가 없다. [부분]
- **공개 가중치의 이용 범위가 연구·교육용이다.** 제품에 넣기 전에 라이선스 원문을 확인한다. [부분: 보도]

## 4. 근거와 한계
- [GitHub EXAONE-4.5](https://github.com/LG-AI-EXAONE/EXAONE-4.5)
- [Taiwan News](https://www.taiwannews.com.tw/news/6337738)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: EXAONE 4.5 33B](https://artificialanalysis.ai/zh/models/exaone-4-5-33b)
- 추가 확인(2026-11-19 웹 검색): [Korea Times: EXAONE 4.5](https://www.koreatimes.co.kr/amp/business/20260409/lg-unveils-multimodal-ai-model-that-outperforms-global-rivals)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 네이티브 작업을 직접 측정한 것이 아니다.
