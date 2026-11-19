# Motif 3 · 앱 — 조사 기록
> 제공자: Motif Technologies · 모델 ID: `Motif-Technologies/Motif-3` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/21-motif/motif-3/app.md`](../../../../md/21-motif/motif-3/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
Motif 3의 앱 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- SWE-Bench Verified 76.2(Qwen-3.7 max 80.4), Terminal-Bench 2.1 74.9(비교 최상위권), SciCode 40.6(53.5).
- 총 314B, 262,144 컨텍스트, vLLM Motif 포크, NVFP4 체크포인트 별도. MIT.

**앱 작업에서 따로 확인할 것**
- 모바일·데스크톱 빌드·서명 도구와의 호환, 긴 세션의 비용, 화면 입력 이해를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **출력 토큰이 많이 든다.** 지수 평가에서 같은 급 중앙값보다 훨씬 많은 출력을 만들었다. 토큰 예산을 넉넉히 잡는다. [부분]
- **공개 여부와 라이선스는 공식 모델 카드로 확인한다.** 출처마다 달라서 상업 이용이나 미공개 코드 전송 전에 원문을 읽는다. [미확인: 출처 충돌]

## 4. 근거와 한계
- [Hugging Face Motif-3](https://huggingface.co/Motif-Technologies/Motif-3)
- [OrcaRouter Motif 3](https://www.orcarouter.ai/blog/motif-3-base-release)
- [AsiaAI 트래커](https://asiaai.fyi/guides/south-korea-frontier-models-tracker/)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: Motif 3 Beta](https://artificialanalysis.ai/ja/models/motif-0714)
- 추가 확인(2026-11-19 웹 검색): [Hugging Face: Motif 3](https://huggingface.co/Motif-Technologies/Motif-3)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 앱 작업을 직접 측정한 것이 아니다.
