# K-EXAONE 2.0 · 펌웨어 — 조사 기록
> 제공자: LG AI Research · 모델 ID: `LGAI-EXAONE/K-EXAONE-2.0-750B-A37B` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/18-lg/k-exaone-2.0/firmware.md`](../../../../md/18-lg/k-exaone-2.0/firmware.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/firmware.md`](../../../_common/domain-rules/firmware.md)

## 2. 이 모델의 펌웨어 작업 운용
K-EXAONE 2.0의 펌웨어 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- SWE-bench Verified 68.2, Terminal-Bench 2.1 43.8, SciCode 37.4, τ3-Banking 14.2, Claw-Eval 77.7. 비교 4개 모델 중 코딩 항목에서 대체로 하위다.
- MMLU-Pro 83.5, GPQA-Diamond 82.2, HLE 18.3, AIME 2026 92.3, IMO Answer 78.6, PolyMath 71.3, MMMLU 86.6.

**펌웨어 작업에서 따로 확인할 것**
- 레지스터·타이밍 수치의 환각 빈도, 장치 쓰기 전 승인 규칙 준수, 크로스 컴파일 도구 호출를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [Hugging Face K-EXAONE-2.0](https://huggingface.co/LGAI-EXAONE/K-EXAONE-2.0-750B-A37B)
- [AsiaAI 트래커](https://asiaai.fyi/guides/south-korea-frontier-models-tracker/)
- [LG AI Research 보도](https://www.lgresearch.ai/news/view?seq=678)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 펌웨어 작업을 직접 측정한 것이 아니다.
