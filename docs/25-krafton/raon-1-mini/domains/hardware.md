# Raon-1 mini (preview) · 하드웨어 — 조사 기록
> 제공자: Krafton · 모델 ID: `KRAFTON/Raon-1-mini-preview` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/25-krafton/raon-1-mini/hardware.md`](../../../../md/25-krafton/raon-1-mini/hardware.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/hardware.md`](../../../_common/domain-rules/hardware.md)

## 2. 이 모델의 하드웨어 작업 운용
Raon-1 mini (preview)의 하드웨어 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- MMLU-Pro 76.5, GPQA-Diamond 84.3, AIME 2026 93.3, HMMT 84.1, IFBench 84.2, 한국어 대화(사내) 92.9, AA-Omniscience 3.5(비교 중 최고).
- RTX 5090 32GB에서 NVFP4, 컨텍스트 32,768 제한. KV 캐시 토큰당 약 8 KiB. DFlash2로 동시성 1에서 최대 2.18배.

**하드웨어 작업에서 따로 확인할 것**
- 데이터시트·회로도 입력의 정확도, HDL 시뮬레이션 루프, 수치·단위 환각 빈도를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [Raon-1-mini-preview README](https://github.com/krafton-ai/Raon-1-mini-preview/blob/main/README.md)
- [MoneyToday](https://www.mt.co.kr/en/tech/2026/10/21/2026102109562241281)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 하드웨어 작업을 직접 측정한 것이 아니다.
