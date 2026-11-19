# EXAONE 4.5 · 하드웨어 — 조사 기록
> 제공자: LG AI Research · 모델 ID: `LGAI-EXAONE/EXAONE-4.5-33B`(저장소 표기 확인 필요) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/18-lg/exaone-4.5/hardware.md`](../../../../md/18-lg/exaone-4.5/hardware.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/hardware.md`](../../../_common/domain-rules/hardware.md)

## 2. 이 모델의 하드웨어 작업 운용
EXAONE 4.5의 하드웨어 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- GPQA-Diamond 80.5, MMLU-Pro 83.3, AIME 2026 92.6, KMMLU-Pro 67.6, KoBALT 52.1.
- 33B 밀집. 256K 컨텍스트에 H200 1장 또는 A100-40GB 4장. Q4_K_M GGUF. 비상업 라이선스.

**하드웨어 작업에서 따로 확인할 것**
- 데이터시트·회로도 입력의 정확도, HDL 시뮬레이션 루프, 수치·단위 환각 빈도를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [GitHub EXAONE-4.5](https://github.com/LG-AI-EXAONE/EXAONE-4.5)
- [Taiwan News](https://www.taiwannews.com.tw/news/6337738)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 하드웨어 작업을 직접 측정한 것이 아니다.
