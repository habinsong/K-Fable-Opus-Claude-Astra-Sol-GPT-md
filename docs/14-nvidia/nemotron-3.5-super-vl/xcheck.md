# Nemotron 3.5 Super VL — 교차 확인
> 제공자: NVIDIA · 모델 ID: `nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16`(Hugging Face), `nvidia/nemotron-3.5-super-vl`(OpenRouter) · 기준일: 2026-11-19 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/14-nvidia/nemotron-3.5-super-vl/general.md`](../../../md/14-nvidia/nemotron-3.5-super-vl/general.md)

`overview.md`의 사양을 다른 출처로 다시 맞춰 본 기록이다. 2026-11-19에 NVIDIA 블로그와 Hugging Face 모델 카드를 직접 읽고 웹 검색으로 맞췄다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 출시일 | 2026-10-15 | [확인] 1차 두 곳 | NVIDIA 블로그, 모델 카드 | 일치 |
| 총/활성 파라미터 | 120B / 12B | [확인] 1차(모델 카드) | 모델 카드 | 블로그는 120B만, 2차 한 곳은 124B |
| 컨텍스트 | 최대 1M | [확인] 1차(모델 카드) | 모델 카드 | 블로그에는 없음, 배포 레시피별로 작음 |
| 라이선스 | OpenMDW-1.1 | [확인] 1차(모델 카드) | 모델 카드 | 블로그에는 없음 |
| 입력 | 텍스트·이미지·비디오(2분) | [확인] 1차 | 모델 카드, 블로그(이미지·웹페이지·PDF) | 일치 |
| 독립 지수 | 26 | [부분] 단일 2차 | Artificial Analysis(X 인용) | 직접 읽지 못함 |
| 한국어 | 명시 없음 | [미확인] | 모델 카드 | 15개 언어 목록에 포함이라는 서술만 |

## 아직 못 올린 것
- 모델 카드 끝부분(약 1만 자), 비교 모델 표, 토큰 단가, 라이선스 원문.

## 출처
- [Hugging Face 모델 카드](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16)
- [NVIDIA 블로그](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/)
- [Artificial Analysis(X)](https://x.com/ArtificialAnlys/status/2110760441240752399)
