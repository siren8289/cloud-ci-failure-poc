# GitHub Actions CI Failure Detection PoC 검증 보고서

## 1. 검증 개요
- **저장소**: [siren8289/cloud-ci-failure-poc](https://github.com/siren8289/cloud-ci-failure-poc)
- **실행 환경**: macOS (Apple Silicon, 로컬) / Ubuntu 22.04 LTS (GitHub Actions Runner)
- **기술 스택**: Python 3.11, pytest 8.3.5, GitHub Actions, Git
- **비용**: 0원 (GitHub Actions Public Repository 무료 티어)

## 2. 검증 목표 및 완료 조건(DoD)
1. **정상 코드 배포**: 단위 테스트 4종 작성 및 푸시 시 GitHub Actions CI 초록색 통과(`success`) 확인
2. **오류 주입 실험**: 의도적 계산 오류 주입 시 pytest 실패(`Exit Code 1`) 및 CI 빨간색 중단(`failure`) 확인
3. **오류 복구 검증**: 정상 로직 복구 후 재푸시 시 CI 자동 복구(`success`) 확인
4. **증거 기록 확보**: 3단계 실행 히스토리 및 로그 파일 보관

## 3. 단계별 검증 결과 (Lifecycle)
| 실행 순서 (Run) | 커밋 해시 & 제목 | 로컬 pytest 결과 | GitHub Actions 상태 | 검증 결과 판정 |
| :---: | :---: | :---: | :---: | :---: |
| **Run 1** | `8968f08` feat: initialize cloud CI failure detection poc... | **4 Passed (0.01s)** | **Success (20초 소요)** | ✅ 정상 베이스라인 확보 |
| **Run 2** | `72fe617` test: inject calculation bug | **2 Failed, 2 Passed** | **Failure (19초 소요)** | ✅ 결함 감지 및 CI 중단 성공 |
| **Run 3** | `0d0439b` fix: restore correct calculation | **4 Passed (0.01s)** | **Success (21초 소요)** | ✅ 파이프라인 자동 복구 성공 |

## 4. GitHub Actions 실행 상세 로그 증거
```text
STATUS     CONCLUSION  RUN_NUMBER  TITLE                               COMMIT   HTML_URL
completed  success     3           fix: restore correct calculation    0d0439b  https://github.com/siren8289/cloud-ci-failure-poc/actions/runs/39967390522
completed  failure     2           test: inject calculation bug        72fe617  https://github.com/siren8289/cloud-ci-failure-poc/actions/runs/39967107489
completed  success     1           feat: initialize cloud CI failure... 8968f08  https://github.com/siren8289/cloud-ci-failure-poc/actions/runs/39966875600
```

## 5. 핵심 원리 및 엔지니어링 교훈
1. **Exit Code 기반의 파이프라인 제어**:
   - `pytest`는 모든 테스트 통과 시 종료 코드 `0`, 단 하나라도 실패 시 `1`을 운영체제에 반환합니다.
   - GitHub Actions Runner는 Step 실행 후 Exit Code가 0이 아니면 즉시 해당 Step과 Job을 `failure` 처리하고 후속 배포 작업을 자동 중단합니다.
2. **Fail Fast(빠른 실패 탐지)의 가치**:
   - 개발자가 결함 있는 코드를 푸시하자마자 19초 만에 클라우드 상에서 결함이 감지되었습니다.
   - 잘못된 코드가 main 브랜치에 머지되거나 프로덕션에 배포되는 것을 사전에 원천 차단합니다.
3. **추가 권장사항 (실무 적용 시)**:
   - 현재 설정은 CI 실패 시 알림을 주지만, 브랜치 머지를 강제로 막기 위해서는 GitHub Repository의 **Branch Protection Rules**에서 `Require status checks to pass before merging`을 활성화해야 합니다.
