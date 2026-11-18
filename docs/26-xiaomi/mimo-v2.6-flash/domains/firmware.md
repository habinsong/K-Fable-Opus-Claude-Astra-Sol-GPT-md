# MiMo-V2.6-Flash · 펌웨어 — 조사 기록
> 제공자: Xiaomi · 모델 ID: `XiaomiMiMo/MiMo-V2.6-Flash`(RL 판 `-RL`) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/26-xiaomi/mimo-v2.6-flash/firmware.md`](../../../../md/26-xiaomi/mimo-v2.6-flash/firmware.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/firmware.md`](../../../_common/domain-rules/firmware.md)

## 2. 이 모델의 펌웨어 작업 운용
MiMo-V2.6-Flash의 펌웨어 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- DeepSWE v1.1 67.9(Opus 5 74.0), Terminal Bench 2.1 87.6(89.1), MiMo VisualCoding 71.5(Opus 5 70.0).
- 지식 벤치마크가 정리 글에 없다. 사이버: CyberGym 95.1, ExploitGym 6.0, ExploitBench 25.3, SEC Bench Pro 47.5.

**펌웨어 작업에서 따로 확인할 것**
- 레지스터·타이밍 수치의 환각 빈도, 장치 쓰기 전 승인 규칙 준수, 크로스 컴파일 도구 호출를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [OrcaRouter MiMo-V2.6-Flash](https://www.orcarouter.ai/blog/xiaomi-mimo-v2-6-flash-release)
- [Hugging Face MiMo-V2.6-Flash](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash)
- [DataNorth](https://datanorth.ai/news/xiaomi-releases-mimo-v2-6-pro-and-flash)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 펌웨어 작업을 직접 측정한 것이 아니다.
