# MiMo-V2.6-Flash · 앱 — 조사 기록
> 제공자: Xiaomi · 모델 ID: `XiaomiMiMo/MiMo-V2.6-Flash`(RL 판 `-RL`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/26-xiaomi/mimo-v2.6-flash/app.md`](../../../../md/26-xiaomi/mimo-v2.6-flash/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
MiMo-V2.6-Flash의 앱 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- DeepSWE v1.1 67.9(Opus 5 74.0), Terminal Bench 2.1 87.6(89.1), MiMo VisualCoding 71.5(Opus 5 70.0).
- FP8 172.9 GB, SGLang 텐서 병렬 16 + 데이터 병렬 2 또는 vLLM 텐서 병렬 8, 컨텍스트 1M. MIT.

**앱 작업에서 따로 확인할 것**
- 모바일·데스크톱 빌드·서명 도구와의 호환, 긴 세션의 비용, 화면 입력 이해를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [OrcaRouter MiMo-V2.6-Flash](https://www.orcarouter.ai/blog/xiaomi-mimo-v2-6-flash-release)
- [Hugging Face MiMo-V2.6-Flash](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash)
- [DataNorth](https://datanorth.ai/news/xiaomi-releases-mimo-v2-6-pro-and-flash)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 앱 작업을 직접 측정한 것이 아니다.
