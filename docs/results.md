# GitHub Actions CI Failure Detection PoC 검증 보고서

## 1. 검증 목표
코드 오류가 발생했을 때 GitHub Actions가 자동으로 이를 감지하고 CI 파이프라인을 실패(Failure) 처리하는 원리를 단계별로 실험하고 입증합니다.

## 2. 실험 절차 및 기대 결과
| 단계 | 작업 내용 | 로컬 pytest 결과 | GitHub Actions 상태 | 검증 목적 |
| :---: | :--- | :---: | :---: | :--- |
| **Run 1** | 정상 코드 Push | **4 Passed (Exit Code 0)** | **Success (초록색 체크)** | 정상 환경 베이스라인 확보 |
| **Run 2** | 연산 버그 주입 (`*` -> `+`) | **2 Failed (Exit Code 1)** | **Failure (빨간색 X)** | CI 오류 자동 감지 및 중단 확인 |
| **Run 3** | 버그 수정 및 복구 (`+` -> `*`) | **4 Passed (Exit Code 0)** | **Success (초록색 체크)** | CI 복구 및 파이프라인 정상화 확인 |

## 3. 검증 증거 로그
- 로컬 테스트 상세 로그: `docs/test-results.txt`
- CI 실행 히스토리: `docs/ci-run-history.txt` (GitHub Actions 실행 후 기록 예정)
- 오류 로그: `docs/ERROR_LOG.md`
