# GLM-5.3 · 웹 — 조사 기록
> 제공자: Z.ai(Zhipu) · 모델 ID: API `glm-5.3`(표기 확인 필요), 가중치 저장소 `zai-org/GLM-5.3`(검색 결과의 표기) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 docs/README.md의 근거 수준)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/08-glm/glm-5.3/web.md`](../../../../md/08-glm/glm-5.3/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§1 분야 규칙, §2 이 모델의 분야 운용). 응답 계약과 작업 원칙은 전역 지침(AGENTS·CLAUDE·GEMINI.md)이 맡는다.
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 744B급 MoE(활성 약 40B), 컨텍스트 100만 토큰, 독립 평가 점수 60 또는 45(버전 충돌), 벤더 수치는 미확인, 접근 방식과 약관 정보 부족.

- **웹 UI 생성 품질의 독립 평가는 찾지 못했다.** [미확인] 유일한 직접 후기(MindStudio)는 리팩터링, 보안 감사, 창작 HTML 생성을 시험했고, 도커로 띄운 암호화폐 추적 앱에 실시간 접속자 수 기능을 처음부터 끝까지 올바르게 추가했다고 한다. 스니펫에서 UI 디자인 판정 부분이 잘려 있어 디자인 품질은 확인하지 못했다. [부분: 개인 후기] 시각 마감은 스크린샷으로 직접 대조하고, 기존 UI 체계가 우선한다(§1.1).
- **다른 모델의 근거를 가져오지 않는다.** 검색에 나온 "디자인에서 코드로" 비교 페이지들은 GLM-5V-Turbo라는 별도 모델에 대한 것이다. 이 모델의 React·Vue·Tailwind 출력 능력을 GLM-5.3에 옮기지 않는다. [부분]
- **디자인-코드 벤치마크의 한계를 안다.** 한 평자는 Design2Code류 점수가 픽셀 유사도를 재지 유지보수성이나 실사용성을 재지 않는다고 지적했다. 점수가 있어도 우리 코드베이스의 컴포넌트 규약, 접근성, 상태 관리와 맞는지는 별도로 확인한다. [부분]
- **집계 사이트의 코딩 점수는 인용하지 않는다.** BenchLM에 GLM-5.3의 SWE-bench(Vals) 95.4%가 올라 있으나 같은 사이트의 SWE-bench Verified·SWE Multilingual은 "곧 공개" 상태이고, 다른 변형과 혼동될 수 있는 수치다. [부분: 집계 사이트]
- **접근 방식을 확인한다.** 출시 초기에 구독(GLM Coding Plan, ZCode) 우선이고 토큰 과금 API는 단계적으로 열렸다는 서술이 있다. 현재 어떤 경로로 호출 가능한지 공식 문서로 확인하고, 구독 전용 경로의 약관이 자동화 사용을 허용하는지 본다. [부분/미확인]
- **보안·접근성 판단을 맡기지 않는다.** 인가, 입력 검증, 비밀 노출, 접근성 "충족" 여부는 도구 출력과 §1.1 기준으로 사람이 점검한다. API·CSS·브라우저 지원은 공식 문서와 린터·컴파일러 출력으로 확인한다.
- **완료 보고는 도구 출력으로 확인한다.** 도구 호출 오류율과 환각률의 독립 측정이 없다. [미확인] 린터·타입체크·테스트 출력과 `git diff`를 직접 읽는다.
- **미공개 소스를 API로 보내기 전에 약관을 확인한다.** 데이터 처리 위치·보관·학습 사용 조건을 찾지 못했다. [미확인] 확인 전에는 비밀·고객 데이터가 담긴 코드를 보내지 않는다(전역 지침).
- **자체 호스팅은 대규모 장비가 필요하다.** 가중치가 공개돼도 744B급이라 웹 개발 보조용 로컬 실행은 현실적이지 않다. [추정]
- **시간·토큰 상한을 둔다.** 같은 급에서 가장 느린 편이고 출력이 매우 길다. [확인: Artificial Analysis 모델 페이지]
- **공개 가중치지만 상업 이용에 제한이 있다.** 라이선스 원문을 확인한다. [확인: Artificial Analysis 모델 페이지]
- **웹 앱 확장은 비용 효율이 좋다.** Opus 5.5와 비슷한 결과를 약 9분의 1 비용으로 냈다. [확인: Vals 평가]
- **제3자 추론 서비스에서 요청 간 KV 캐시 노출 사고가 보고됐다.** 미공개 코드와 비밀을 호스팅 서비스에 보내기 전에 사고 공지와 격리 방식을 확인한다. [부분: 제목만 확인]
- **`medium`이 비용 대비 가장 낫다.** `max`는 정확도가 약 5%p 오르는데 비용이 두 배다. [부분: HN 단일 측정 증언]

## 4. 근거와 한계
- 직접 후기: [MindStudio: GLM-5.3 hands-on review](https://www.mindstudio.ai/blog/glm-5-3-hands-on-review) (스니펫만) [부분: 개인 후기]
- 다른 모델(GLM-5V-Turbo) 페이지: [shiporskip: GLM-5V-Turbo 비교](https://shiporskip.io/compare/glm-5v-turbo-zhipu-ai-multimodal-design-to-code-vision-vs-vercel-v0-3-full-stack-app-generation-database-provisioning) [부분: 마케팅성, 다른 모델]
- 집계 코딩 점수: [BenchLM: GLM-5 대 GLM-5.3](https://benchlm.ai/md/compare/glm-5-vs-glm-5-3.md) [부분: 집계 사이트]
- 추가 확인(2026-11-19 웹 검색): [Artificial Analysis: glm-5-3 모델 페이지](https://artificialanalysis.ai/models/glm-5-3)
- 추가 확인(2026-11-19 웹 검색): [Vals AI: Vibe Code Bench 1-100 v1.1 (2026-11-17)](https://www.vals.ai/benchmarks/vcb-1-100-v1-1)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Cloudflare: GLM-5.3 Workers AI 요청 간 KV 캐시 노출(제목만 확인)](https://blog.cloudflare.com/kv-cache-exposure-remediation/)
- 추가 확인(2026-11-19 해외 커뮤니티·포럼): [Hacker News: GLM 5.3 Flash 한 달 사용기 스레드](https://news.ycombinator.com/item?id=49934620)
- 한계: 웹 UI 품질에 대한 독립 평가와 공식 자료를 읽지 못했다.
