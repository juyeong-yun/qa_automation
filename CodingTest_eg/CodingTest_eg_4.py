"""
복잡한 테스트 시나리오 설계 및 구현
다중 사용자 환경에서 발생할 수 있는 경쟁 상태(race condition)를 테스트하기 위한 
시나리오를 설계하고 자동화 하세여.
  - 동일 데이터 레코드를 동시에 수정하려는 두 개의 프로세스를 시뮬레이션하세요.
  - 경쟁 상태로 인해 발생할 수 있는 문제를 식별하고, 이를 해결하는 방법을 제안하세요.

요구사항
  - 프로그래밍 언어는 자유입니다.
  - 스레드나 프로세스를 활용하여 동시성을 구현하세요
  - 테스트 결과를 분석하고 리포트를 작성하세요

문제 식별 및 해결방안
  - 락(lock) 매커니즘 도입 : 서버 측에서 데이터 수정 시 잠금처리를 통해 동시 수정 방지
  - 버전 관리 : 각 수정시도에 버전 번호를 부여하여 충돌감지
  - 원자적 연산 사용 : 데이터베이스 수준에서 원자적 연산을 이용하여 동시성 문제 헤결
"""

import threading
import requests


# 공유자원 URL
RESOURCE_URL = 'https://api.example.com/resource/1'
AUTH_TOKEN = 'Bearer your_auth_token'

# 수정할 데이터
update_data_1 = {'value' : 'Thread_A'}
update_data_2 = {'value' : 'Thread_B'}

# 헤더 설정
headers = {
  'Authorization' : AUTH_TOKEN,
  Content-Type : 'application/json'
}

def update_resource(data) :
  response = requests.put(RESOURCE_URL, json=data, headers=headers)
  print(f"Status Code : {response.status_code}, Response:{response,json()}")

#스레드 생성
# 파이썬의 스레드를 활용하여 동시 실행을 시뮬레이션
thread1 = threading.Thread(target=update_resource, args=(update_data_1))
thread2 = threading.Thread(target=update_resource, args=(update_data_2))

# 동시에 시작
thread1.start()
thread2.start()

# 스레드 종료 대기
thread1.join()
thread2.join()

# 최종데이터 확인
response= requests.get(RESOURCE_URL, headers = headers)
printf(f"Final Data :P{response.json()}")
