# Solar Open 2 · 하드웨어 — 조사 기록
> 제공자: Upstage · 모델 ID: `upstage/Solar-Open2-250B` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/20-upstage/solar-open-2/hardware.md`](../../../../md/20-upstage/solar-open-2/hardware.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/hardware.md`](../../../_common/domain-rules/hardware.md)

## 2. 이 모델의 하드웨어 작업 운용
Solar Open 2의 하드웨어 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- MMLU-Pro 86.2, GPQA-Diamond 86.3, HLE 28.8, AIME2026 95.7, KMMLU-Pro 78.4, CLIcK 90.7, KorMedMCQA 93.0.
- H200 4장 이상(권장 8장), vLLM Upstage 포크, 컨텍스트 1M. Upstage Solar License(표기 의무).

**하드웨어 작업에서 따로 확인할 것**
- 데이터시트·회로도 입력의 정확도, HDL 시뮬레이션 루프, 수치·단위 환각 빈도를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [Hugging Face Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)
- [Upstage 모델 이력](https://console.upstage.ai/docs/models/history)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 하드웨어 작업을 직접 측정한 것이 아니다.
