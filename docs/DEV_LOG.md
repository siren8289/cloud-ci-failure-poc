# Development Log: Cloud CI Failure Detection PoC

## [Phase 1] 2026-10-23 - 프로젝트 초기화 및 로컬 테스트 구축
- **작업 내용**:
  1. 프로젝트 디렉터리 구조 생성 (`app/`, `tests/`, `.github/workflows/`, `docs/`)
  2. Python 3.11 가상환경 `.venv` 구축 및 `pytest==8.3.5` 설치
  3. `app/calculator.py` 비즈니스 로직 작성: `calculate_total(price, quantity)`
  4. `tests/test_calculator.py` 단위 테스트 4개 작성 (정상 주문, 단일 품목, 음수 가격 검증, 0 이하 수량 검증)
  5. `pyproject.toml` 작성으로 모듈 import 경로(`pythonpath = ["."]`) 설정
  6. `.github/workflows/ci.yml` 워크플로 작성 (`ubuntu-latest`, Python 3.11, pytest)
- **실행 및 검증**:
  - 로컬 pytest 실행 완료: 4 passed in 0.01s (Exit Code: 0)
- **다음 작업**:
  - Git 초기화, 1차 정상 코드 커밋 및 GitHub 원격 저장소(`siren8289/cloud-ci-failure-poc`) Push
