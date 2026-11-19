# Qwen3.8-Flash-Next · 펌웨어 — 조사 기록
> 제공자: Alibaba(Qwen) · 모델 ID: `Qwen/Qwen3.8-Flash-Next` · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/06-qwen/qwen3.8-flash-next/firmware.md`](../../../../md/06-qwen/qwen3.8-flash-next/firmware.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/firmware.md`](../../../_common/domain-rules/firmware.md)

## 2. 이 모델의 펌웨어 작업 운용
Qwen3.8-Flash-Next의 펌웨어 작업을 직접 측정한 자료는 찾지 못했다. [미확인] 아래는 이 분야와 가까운 항목의 수치다.

- SWE-bench Pro 62.5(27B 61.7, DeepSeek-V4-Flash 56.0), DeepSWE 1.1 58.7(42.2), SWE-bench Multilingual 81.0, NL2Repo 48.1, LiveCodeBench v6 91.9.
- GPQA-Diamond 91.7, HLE 35.9, IFBench 81.3, MathVision(CI) 95.7, RealWorldQA 88.5.

**펌웨어 작업에서 따로 확인할 것**
- 레지스터·타이밍 수치의 환각 빈도, 장치 쓰기 전 승인 규칙 준수, 크로스 컴파일 도구 호출를 같은 과제로 비교 모델과 직접 대조한다. [추정]
- **제작사 코딩 수치를 믿지 말고 같은 과제로 시험한다.** 한 외부 시험에서는 GLM 5.3 Flash보다 낮았다. [부분]
- **쓰는 하네스에서 도구 호출 성공률을 먼저 잰다.** 도구 호출 신뢰도를 개선한 갱신판이 나왔다는 글이 하나 있다. [부분: 단일 블로그]
- **시간·토큰 상한을 둔다.** 한 작업이 30분을 넘고 출력이 매우 길고 느리다. 독립 지수는 같은 급에서 높은 편이다. [확인: Artificial Analysis 모델 페이지]
- **96GB 맥에서 로컬로 쓸 만하다는 증언이 있다.** 코드가 외부로 나가지 않는 보조 용도로 쓴다. [부분: HN 단일 증언]

## 4. 근거와 한계
- [Hugging Face Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- [Qwen 블로그](https://qwen.ai/blog?id=qwen3.8-flash-next)
- [Akash 분석](https://akash.network/the-bid/qwen3-8-flash-next-architecture-gpu-requirements/)
- 추가 확인(2026-11-19 웹 검색): [MindStudio: Qwen 3.8 Flash Next](https://www.mindstudio.ai/blog/qwen-3-8-flash-next-benchmarks)
- 추가 확인(2026-11-19 웹 검색): [eesel: Qwen 3.8 Flash Next 리뷰](https://www.eesel.ai/blog/qwen38-flash-next-review)
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: qwen3-8-flash-next 모델 페이지](https://artificialanalysis.ai/models/qwen3-8-flash-next)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: Qwen4-Max 스레드](https://news.ycombinator.com/item?id=50513215)
- 한계: 위 수치는 일반 벤치마크와 제조사 발표이며 펌웨어 작업을 직접 측정한 것이 아니다.
