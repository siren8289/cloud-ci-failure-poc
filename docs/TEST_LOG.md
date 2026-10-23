# Test Log: Cloud CI Failure Detection PoC

## [TEST-001] 로컬 단위 테스트 1차 검증 (정상 코드)
- **일시**: 2026-10-23 23:05:25
- **명령어**: `/Users/jeong-yelim/.gemini/antigravity/scratch/cloud-ci-failure-poc/.venv/bin/python -m pytest -v`
- **테스트 결과 요약**: 4 Passed, 0 Failed (Exit Code: 0)
- **상세 결과**:
  - `tests/test_calculator.py::test_normal_order`: PASSED (10,000 * 3 == 30,000)
  - `tests/test_calculator.py::test_single_item`: PASSED (5,000 * 1 == 5,000)
  - `tests/test_calculator.py::test_negative_price`: PASSED (음수 가격 ValueError 발생 확인)
  - `tests/test_calculator.py::test_invalid_quantity`: PASSED (0 수량 ValueError 발생 확인)

## [TEST-002] 단위 테스트 2차 검증 (의도적 오류 주입 실험)
- **일시**: 2026-10-23 23:07:31
- **명령어**: `/Users/jeong-yelim/.gemini/antigravity/scratch/cloud-ci-failure-poc/.venv/bin/python -m pytest -v`
- **테스트 결과 요약**: 2 Failed, 2 Passed (Exit Code: 1)
- **상세 결과**:
  - `tests/test_calculator.py::test_normal_order`: FAILED (assert 10003 == 30000)
  - `tests/test_calculator.py::test_single_item`: FAILED (assert 5001 == 5000)
  - `tests/test_calculator.py::test_negative_price`: PASSED
  - `tests/test_calculator.py::test_invalid_quantity`: PASSED
- **목적 달성**: 계산식 버그가 단위 테스트에 의해 정상적으로 적발됨 확인.

## [TEST-003] 단위 테스트 3차 검증 (오류 복구 및 회귀 방지)
- **일시**: 2026-10-23 23:10:05
- **명령어**: `/Users/jeong-yelim/.gemini/antigravity/scratch/cloud-ci-failure-poc/.venv/bin/python -m pytest -v`
- **테스트 결과 요약**: 4 Passed, 0 Failed (Exit Code: 0)
- **상세 결과**:
  - `tests/test_calculator.py::test_normal_order`: PASSED (30,000 정상 산출)
  - `tests/test_calculator.py::test_single_item`: PASSED (5,000 정상 산출)
  - `tests/test_calculator.py::test_negative_price`: PASSED (ValueError)
  - `tests/test_calculator.py::test_invalid_quantity`: PASSED (ValueError)


