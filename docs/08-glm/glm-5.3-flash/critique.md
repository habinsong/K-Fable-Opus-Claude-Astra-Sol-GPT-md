# GLM-5.3-Flash — 비판적 평가·쓸 때와 쓰지 않을 때
> 제공자: Z.ai(Zhipu) · 모델 ID: API `glm-5.3-flash`(빠른 서빙 변형 `glm-5.3-flashx`가 별도 존재, 표기 확인 필요), 가중치 저장소 `zai-org/GLM-5.3-Flash`(검색 결과의 표기) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/08-glm/glm-5.3-flash/AGENTS.md`](../../../md/08-glm/glm-5.3-flash/AGENTS.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

#### 2.5 비판적 평가
- 강점 후보: 낮은 가격, 무료 등급, MIT 라이선스, 100만 토큰 컨텍스트, 멀티모달 입력. 약점 후보: 독립 근거가 얕고 가격·입력 방식·출시일이 출처마다 다르며, 재업로드 가중치가 퍼져 있고, 무료 등급은 한도가 불안정하다.
- 쓰는 용도: 비용 민감한 분류·추출·코드 초안, 이미지 이해가 필요한 보조(검증 전제). 쓰지 않는 용도: 출처 없는 사실 조회, 규제 데이터(약관 확인 전), 임의 재업로드 가중치 사용.
- 막히면 플래그십(`glm-5.3` 문서)이나 `02-claude/opus-5.5`, `gpt-6.1-sol`, `gemini-4-argon` 문서의 모델로 올린다.

## 재확인 (2026-11-19, 웹 검색, 사용자·후기 글)
- **로컬 속도 보고는 하드웨어에 따라 크게 갈린다(대부분 MindStudio 한 저자·단일 구성).** 듀얼 Xeon + RTX 3060 2장에서 약 50~60 tok/s(전용 런타임), GPU 5장 llama.cpp 1비트(약 93GB)에서 짧은 작업 33~34 tok/s이고 10만 토큰 넘게 생성하면 14~15 tok/s로 떨어짐, DGX Spark 1대 UD-Q2_K_XL 17.9 tok/s, B200 MTP 적용으로 58.6에서 86.5 tok/s(컨텍스트 4,096), CPU만 쓰면 한 자릿수. [부분: 개인 보고] ([MindStudio Project Maya](https://www.mindstudio.ai/blog/glm-5-3-local-review-project-maya), [MindStudio 멀티 GPU](https://www.mindstudio.ai/blog/glm-5-3-flash-hands-on-multi-gpu-test/), [ai-muninn DGX Spark](https://ai-muninn.com/en/blog/glm53-flash-one-dgx-spark))
- Unsloth는 3비트 UD-IQ3_XXS가 128GB 기기에 들어간다고 안내한다. 메인라인 llama.cpp 지원은 서술이 엇갈려 PR·포크가 필요하다는 쪽이 많다. 출시 48시간 동안 신뢰할 만한 커뮤니티 tok/s 수치가 없었다는 글도 있다. [부분 / 충돌] ([Unsloth](https://unsloth.ai/docs/models/glm-5.3-flash))
