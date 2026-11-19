# Tencent Hy4 · 하드웨어 — 조사 기록
> 제공자: Tencent(Hunyuan) · 모델 ID: `tencent/hy4`(OpenRouter 표기) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/15-tencent/hy4/hardware.md`](../../../../md/15-tencent/hy4/hardware.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/hardware.md`](../../../_common/domain-rules/hardware.md)

## 2. 이 모델의 하드웨어 작업 운용
Tencent Hy4 전용 하드웨어 작업 측정은 찾지 못했다. [미확인] 아래는 이 분야와 관련된 이 모델의 수치와 운용 메모다. 모델 전체 사양은 상위 폴더의 [`overview.md`](../overview.md), 운용은 [`operations.md`](../operations.md)를 따른다.

- 컨텍스트 1M. 가격 RMB 6/18(100만 토큰당, 표준가). OpenRouter 약 63 tok/s, 첫 토큰 약 2.9초(3일 창).
- Tencent 자체 시험: FrontierCode 2.0 31.0(1위 46.4), Terminal Bench 4.0 44.4(1위 66.8), OSWorld 2.1 78.9(1위 81.8), Goal2Repo 23.2(Claude 74.0). 대형 저장소 작업이 약하다. [부분, 벤더 주장]
- 독립: CWE-Bench-AA 75.8%(120과제), Collinear CWE-bench 64.1%(250과제, 7위). [부분]

**하드웨어 작업에서 따로 확인할 것**
- 데이터시트·회로도 입력의 정확도, HDL 시뮬레이션 루프, 수치·단위 환각 빈도를 같은 과제로 비교 모델과 직접 대조한다. 이 문서의 수치를 하드웨어 작업 성능으로 읽지 않는다. [추정]

## 4. 근거와 한계
- [Tencent Hy4 정리(explainx)](https://explainx.ai/blog/tencent-hy4-official-release-770b-vision-computer-use-terminal-bench-44-4-weights-planned-2026)
- [OpenRouter: tencent/hy4](https://openrouter.ai/tencent/hy4)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 하드웨어 작업을 직접 측정한 것이 아니다. 분야 규칙은 모델과 무관한 공통 근거를 따른다.
