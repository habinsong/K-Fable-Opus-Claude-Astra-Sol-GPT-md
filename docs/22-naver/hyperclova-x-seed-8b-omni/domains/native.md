# HyperCLOVA X SEED 8B Omni · 네이티브 — 조사 기록
> 제공자: Naver Cloud · 모델 ID: `naver-hyperclovax/HyperCLOVAX-SEED-Omni-8B` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/22-naver/hyperclova-x-seed-8b-omni/native.md`](../../../../md/22-naver/hyperclova-x-seed-8b-omni/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
HyperCLOVA X SEED 8B Omni의 네이티브 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- 코딩 점수 없음. 컨텍스트 32K.
- 8B 밀집, 다운로드 약 16GB, A100 80GB 4장 또는 3장 약 48GB(서술 모순). OmniServe 필요.

**네이티브 작업에서 따로 확인할 것**
- 메모리 안전·동시성 버그 진단 정확도, 디버거·새니타이저 출력의 해석를 같은 과제로 비교 모델과 직접 대조한다. [추정]

## 4. 근거와 한계
- [Hugging Face HyperCLOVAX-SEED-Omni-8B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Omni-8B)
- [Naver Corp 보도자료](https://www.navercorp.com/en/media/pressReleasesDetail?seq=34256)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 네이티브 작업을 직접 측정한 것이 아니다.
