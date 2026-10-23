# Error Log: Cloud CI Failure Detection PoC

## [ERR-001] ModuleNotFoundError: No module named 'app'
- **발생 일시**: 2026-10-23 23:05:07
- **발생 환경**: macOS zsh, pytest 8.3.5 실행 시
- **오류 내용**:
  ```text
  ImportError while importing test module 'tests/test_calculator.py'.
  tests/test_calculator.py:2: in <module>
      from app.calculator import calculate_total
  E   ModuleNotFoundError: No module named 'app'
  ```
- **원인 분석**:
  단독 `pytest` 바이너리 실행 시 현재 루트 디렉터리가 Python의 `sys.path`에 포함되지 않아 하위 패키지인 `app`을 최상위 모듈로 인식하지 못함.
- **해결 방법**:
  1. `pyproject.toml`을 생성하고 `[tool.pytest.ini_options]` 섹션에 `pythonpath = ["."]` 지정.
  2. 실행 시 `python -m pytest -v` 방식을 병행하여 모듈 검색 경로를 현재 위치로 보장함.
- **재검증 결과**:
  `pytest -v` 및 `python -m pytest -v` 실행 시 4개 테스트 모두 정상 탐색 및 통과(PASSED).

## [ERR-002] AssertionError: Intentional Bug Injection in calculate_total
- **발생 일시**: 2026-10-23 23:07:31
- **발생 환경**: macOS zsh, pytest 8.3.5 실행 시
- **오류 내용**:
  ```text
  FAILED tests/test_calculator.py::test_normal_order - assert 10003 == 30000
  FAILED tests/test_calculator.py::test_single_item - assert 5001 == 5000
  2 failed, 2 passed in 0.14s (Exit Code: 1)
  ```
- **원인 분석**:
  `app/calculator.py`에서 곱셈 연산자(`*`)를 덧셈 연산자(`+`)로 의도적으로 변경하여 주문 총액 계산 로직 파괴.
- **해결 계획**:
  CI 파이프라인에서 실패(Failure, Exit Code 1) 감지 여부를 확인한 후, `return price * quantity`로 원복 예정.

