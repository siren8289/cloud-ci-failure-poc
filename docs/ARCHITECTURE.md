# System Architecture: Cloud CI Failure Detection PoC

## 1. 전체 아키텍처 개요
본 프로젝트는 **GitHub Actions**와 **pytest**를 연계하여 개발자가 코드를 푸시할 때마다 클라우드 Runner 환경에서 자동으로 빌드 및 단위 테스트를 수행하고, 오류가 발생했을 때 파이프라인이 즉각 실패(`Exit Code != 0`) 처리되는 CI 메커니즘을 검증합니다.

```mermaid
flowchart TD
    subgraph Local_Dev["로컬 개발 환경 (macOS)"]
        DEV["개발자 (Developer)"] -->|1. 코드 작성/수정| CODE["app/calculator.py"]
        DEV -->|2. 단위 테스트 작성| TEST["tests/test_calculator.py"]
        DEV -->|3. 로컬 사전 검증| LOCAL_PYTEST["pytest -v"]
        DEV -->|4. Git Commit & Push| GIT_PUSH["git push origin main"]
    end

    subgraph GitHub_Cloud["GitHub 클라우드 플랫폼"]
        REPO["원격 저장소 (siren8289/cloud-ci-failure-poc)"]
        GHA["GitHub Actions 오케스트레이터"]
        
        GIT_PUSH -->|Webhook Trigger| REPO
        REPO -->|push 이벤트 감지| GHA
    end

    subgraph Cloud_Runner["GitHub 호스팅 Runner (Ubuntu-latest)"]
        RUNNER["Ubuntu 가상머신 인스턴스"]
        STEP1["Step 1: actions/checkout@v4"]
        STEP2["Step 2: actions/setup-python@v5 (Python 3.11)"]
        STEP3["Step 3: pip install -r requirements.txt"]
        STEP4["Step 4: python -m pytest -v"]
        
        GHA -->|Job 스케줄링| RUNNER
        RUNNER --> STEP1 --> STEP2 --> STEP3 --> STEP4
    end

    subgraph Decision["판정 및 피드백 (Exit Code)"]
        STEP4 -->|모든 테스트 Pass (Exit Code 0)| PASS["CI Success (녹색 체크 ✅)"]
        STEP4 -->|단 1개라도 Fail (Exit Code 1)| FAIL["CI Failure (빨간색 X ❌)"]
        FAIL -.->|머지 차단 및 알림| DEV
    end

    classDef pass fill:#2ea44f,stroke:#22863a,color:#ffffff
    classDef fail fill:#cb2431,stroke:#b31d28,color:#ffffff
    class PASS pass
    class FAIL fail
```

## 2. 컴포넌트 역할 명세
| 컴포넌트 | 파일 경로 | 주요 역할 |
| :--- | :--- | :--- |
| **비즈니스 로직** | `app/calculator.py` | 주문 금액 계산(`calculate_total`), 음수 가격 및 0 이하 수량 예외 처리(`ValueError`) |
| **단위 테스트** | `tests/test_calculator.py` | 정상 계산, 단일 상품 계산, 음수 가격 예외, 잘못된 수량 예외에 대한 자동화 테스트 |
| **CI 파이프라인** | `.github/workflows/ci.yml` | `main` 브랜치 Push/PR 발생 시 Ubuntu 환경에서 Python 설치 및 pytest 자동 실행 |
| **환경 설정** | `requirements.txt`, `pyproject.toml` | 의존성 고정(`pytest==8.3.5`) 및 pytest 모듈 경로(`pythonpath = ["."]`) 정의 |
