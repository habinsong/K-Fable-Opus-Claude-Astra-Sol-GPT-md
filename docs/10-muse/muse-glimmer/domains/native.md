# Muse Glimmer · 네이티브 — 조사 기록
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-glimmer`(Meta 오픈 가중치 30B) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/10-muse/muse-glimmer/native.md`](../../../../md/10-muse/muse-glimmer/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
Muse Glimmer의 네이티브 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- Terminal-Bench v2.1 52%(Qwen3.6 27B 61%), SWE-Bench Verified 76.0(Meta) / 72.0(Raon 카드), Terminal-Bench Lite 70.7.
- BF16 약 60 GB, 4비트 약 18 GB, KV 캐시 128K에서 약 1.8 GB. 24GB용 K-Quant-17GB(정확도 -1%), 32GB용 K-Quant-Dynamic(-0.2%). Apache 2.0.

**네이티브 작업에서 따로 확인할 것**
- 메모리 안전·동시성 버그 진단 정확도, 디버거·새니타이저 출력의 해석를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **로컬 단일 GPU용 에이전트 모델이다.** 미공개 코드를 외부로 보내지 않아도 되지만 큰 변경은 테스트와 `git diff`로 확인하고 어려운 작업은 상위 모델에 맡긴다. [부분]
- **어려운 코딩과 조사에는 쓰지 않는다.** 독립 지수가 6으로 매우 낮다. 로컬에서 도는 보조 용도로 제한한다. [확인: Artificial Analysis 모델 페이지]

## 4. 근거와 한계
- [Artificial Analysis Muse Glimmer](https://artificialanalysis.ai/articles/muse-glimmer)
- [AI Weekly](https://aiweekly.co/alerts/meta-releases-muse-glimmer-a-30b-apache-20-agent-model)
- [VentureBeat](https://venturebeat.com/ai/meta-returns-to-open-source-with-muse-glimmer-an-apache-2-0-licensed-30b-parameter-ai-model-optimized-for-agents-available-now/)
- 추가 확인(2026-11-19 웹 검색): [DataCamp: Muse Glimmer](https://www.datacamp.com/blog/muse-glimmer)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: muse-glimmer 모델 페이지](https://artificialanalysis.ai/models/muse-glimmer)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 네이티브 작업을 직접 측정한 것이 아니다.
