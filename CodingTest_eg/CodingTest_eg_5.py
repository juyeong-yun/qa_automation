"""
성능 테스트 시나리오 작성
JMeter를 이용하여 특정 서버에 대한 부하 테스트(load test)를 설계하고 실행하세요.
테스트 결과를 분석하고 개선 방안을 제시하세요.

평가포인트 :
  - 성능테스트 이해도 : TPS, 응답시간, 임계점 등 주요 지표 파악
  - 성능 분석 능력 : 그래프 및 로그를 통한 병목 지점 식별
  - 최적화 제안 : 서버 성능 향상을 위한 현실적인 제안

문제 설명 :
jMeter를 사용하여 https://api.example.com/login 엔드포인트에 대한 부하 테스트를 설계하고 실행하세요.
- 동시 사용자 100명을 시뮬레이션하여 10분동안 테스트를 진행하세요.
- TPS(Transaction Per Second), 평균 응답 시간, 에러 비율 등의 지표를 수집하세요.
- 테스트의 결과를 분석하고 서버의 병목 지점을 식별한 후, 개선 방안을 제시하세요.

예상답변 :
1. JMeter 테스트 계획 설정
- Thread Group 설정 :
  - Number of Thread(Users) : 100
  - Ramp-Up Period : 60초(사용자 부하를 서서히 증가)
  - Loop Count : 지속 시간을 설정하거나 Scheduler를 사용하여 10분동안 테스트

- HTTP Request 샘플러 추가:
  - Method : POST
  - URL : https://api.example.com/login
  - Body Data :
    username = testuser
    & password = testpassword

- HTTP Header Manager 추가 :
  - Content-Type : application/X-www-form-urlencoded

- Listeners 추가 :
  - Summary Report
  - Graph Results
  - Aggregate Report

2. 테스트 실행 및 결과 수집
테스트를 실행하고, 각 Listner를 통해 지표를 수집합니다.

3. 결과 분석
  -  TPS : 초당 처리된 트랜잭션 수를 확인합니다.
  - 평균 응답 시간 : 요청에 대한 평균 응답 시간을 확인합니다.
  - 에러 비율 : 실패한 요청의 비율을 확인합니다.
  - 그래프 분석 : 응답시간의 변동 추이를 확인합니다.
  - 예시결과 :

4. 병목 지점 식별
  - 응답 시간 증가 원인 : 동시 사용자가 많을 때 응답시간이 증가하는 패턴이 보입니다.
  - 에러 발생 원인 : 서버가 과부하되어 타임아웃이나 500번대 에러가 발생하고 있습니다.

5. 개선 방안 제시
  - 서버 스케일링 : 서버 인스턴스를 늘려 부하를 분산합니다.
  - 로드 밸런서 도입 : 로드 밸런서를 통해 트래픽을 균등 분산합니다.
  - DB 연결 최적화 : DB 커낵션 풀 크기를 조절하여 보다 효율적인 연결 관리.
  - 코드 최적화 : 로그인 로직에서 불필요한 연산이나 I/O를 최적화합니다.
  - 캐싱 전략 적용 : 인증 토큰 발급 시 캐싱을 도입하여 성능 향상
"""
