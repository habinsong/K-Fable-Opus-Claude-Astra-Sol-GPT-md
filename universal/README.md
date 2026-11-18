# universal

모델을 가리지 않고 쓰는 지침입니다. 모델별로 다듬은 [`md/`](../md/README.md)에 쓰는 모델이 없으면 여기서 고르세요.

## 전역 지침

`AGENTS.md`, `CLAUDE.md`, `GEMINI.md` 세 개이고 읽는 도구가 다릅니다.

| 파일 | 읽는 도구 | 다른 점 |
|---|---|---|
| `AGENTS.md` | Codex를 비롯한 여러 도구 | 기본형 |
| `CLAUDE.md` | Claude Code | 커밋 메시지에 Claude 표기와 `Co-Authored-By` 줄을 넣지 않는다는 항목이 더 있음 |
| `GEMINI.md` | Gemini CLI | 검색과 사실 규율, 읽기 규율 항목이 더 있음 |

프로젝트 루트에 넣으면 그 프로젝트에서만, `~/.codex`나 `~/.claude`, `~/.gemini`에 넣으면 모든 프로젝트에서 적용됩니다.

## 분야 문서

하나만 복사해도 공통 규칙이 들어 있습니다. 뭘 써야 할지 모르겠으면 `general.md`부터 쓰면 됩니다.

| 파일 | 쓰는 일 |
|---|---|
| `general.md` | 분야가 정해지지 않은 일반 개발과 분석 |
| `web.md` | 웹 프런트엔드, 백엔드 API, 풀스택 |
| `app.md` | iOS와 Android 앱, 크로스플랫폼 앱 |
| `native.md` | 데스크톱 프로그램, CLI, 드라이버 같은 컴파일하는 소프트웨어 |
| `hardware.md` | 회로와 PCB 설계, 부품 선정, FPGA용 HDL |
| `firmware.md` | MCU와 SoC 펌웨어, RTOS, 부트로더 |
| `web-research.md` | 최신 정보 조사, 사실 확인, 출처 수집 |
| `research.md` | 논문, 실험, 데이터 분석 |
| `tech-research.md` | 기술 선정, 도입 타당성, 특허와 라이선스 조사 |
| `ko-academic.md` | 논문, 초록, 기술 보고서 같은 한국어 학술 글의 윤문 |
| `ko-everyday.md` | 메신저, 이메일, 블로그 같은 한국어 일상 글의 윤문 |
| `ko-literary.md` | 소설, 수필, 칼럼 같은 한국어 문학 글의 윤문 |

다른 문서에도 포함되어 있는 공통 규칙입니다.

| 파일 | 내용 | 들어가는 곳 |
|---|---|---|
| `contract.md` | 복명복창, 5항목 보고, 한국어 존댓말 같은 공통 규칙과 작업 원칙 | 모든 분야 문서 |
| `ko-core.md` | 문장 흐름과 호흡, 번역투 같은 한국어 윤문의 공통 원리 | 한국어 윤문 문서 세 개 |
