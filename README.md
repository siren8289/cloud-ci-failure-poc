# CI Failure Detection PoC

GitHub Actions와 pytest를 연동하여 코드 오류 발생 시 CI 파이프라인의 실패 감지 및 복구 프로세스를 검증하는 프로젝트입니다.

## Tech Stack
- **Language**: Python 3.11
- **Testing Framework**: pytest 8.3.5
- **CI/CD Platform**: GitHub Actions
- **VCS**: Git / GitHub

## Local Test
```zsh
# 가상환경 활성화 후 테스트 실행
source .venv/bin/activate
python -m pytest -v
```

## Verification Lifecycle
1. **Pass**: 정상 비즈니스 로직 작성 및 CI 성공 (`Success`)
2. **Fail**: 연산 로직에 의도적 결함 주입 후 CI 실패 감지 (`Failure`)
3. **Recover**: 결함 수정 후 CI 파이프라인 자동 복구 (`Success`)

## Detailed Reports
- 아키텍처 및 원리: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- 개발 로그: [docs/DEV_LOG.md](docs/DEV_LOG.md)
- 에러 로그: [docs/ERROR_LOG.md](docs/ERROR_LOG.md)
- 테스트 로그: [docs/TEST_LOG.md](docs/TEST_LOG.md)
- 최종 검증 결과: [docs/results.md](docs/results.md)
