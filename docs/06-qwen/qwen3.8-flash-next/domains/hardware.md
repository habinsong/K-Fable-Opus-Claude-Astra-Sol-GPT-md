# Qwen3.8-Flash-Next · 하드웨어 — 조사 기록
> 제공자: Alibaba(Qwen) · 모델 ID: `Qwen/Qwen3.8-Flash-Next` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/06-qwen/qwen3.8-flash-next/hardware.md`](../../../../md/06-qwen/qwen3.8-flash-next/hardware.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/hardware.md`](../../../_common/domain-rules/hardware.md)

## 2. 이 모델의 하드웨어 작업 운용
Qwen3.8-Flash-Next의 하드웨어 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- GPQA-Diamond 91.7, HLE 35.9, IFBench 81.3, MathVision(CI) 95.7, RealWorldQA 88.5.
- 총 약 180B(본체 125B + N-gram 51B + MTP 4B), 4비트 약 90~120 GB, 컨텍스트 262,144. qwen-community-1.0.

**하드웨어 작업에서 따로 확인할 것**
- 데이터시트·회로도 입력의 정확도, HDL 시뮬레이션 루프, 수치·단위 환각 빈도를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **사실 질문의 오답 비율이 중간 수준이다.** 사실·수치·인용은 출처 원문으로 확인한다. 사실 질문 기준 오답 비율이 46.8%다. [부분: 독립 측정을 옮긴 집계 페이지]

## 4. 근거와 한계
- [Hugging Face Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- [Qwen 블로그](https://qwen.ai/blog?id=qwen3.8-flash-next)
- [Akash 분석](https://akash.network/the-bid/qwen3-8-flash-next-architecture-gpu-requirements/)
- 추가 확인(2026-11-19 웹 검색): [BenchLM: AA-Omniscience 환각률(2026-11-19, Artificial Analysis 수치를 옮긴 미러)](https://benchlm.ai/benchmarks/omnisciencehallucinationrate)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 하드웨어 작업을 직접 측정한 것이 아니다.
