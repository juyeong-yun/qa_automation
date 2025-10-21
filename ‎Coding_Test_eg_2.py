"""
Selenium을 활용한 웹 애플리케이션 테스트
Selenium WebDriver를 이용하여 사용자 로그인, 데이터 입력, 
제출 후 결과까지 자동화하세요.

평가포인트 :
  - 웹 요소 식별 능력 : Xpath, CSS, Selector 등 활용
  - 코드 품질 : 가독성, 유지 보수성, 모듈화 수준
  - 동기화 처리 : 페이지 로딩 시간에 따른 대기 처리 능력
"""


"""
문제 설명
  - 로그인 페이지로 이동
  - 올바른 사용자명과 비밀번호 로그인
  - 로그인 성공 여부 확인 (예: 사용자 프로필 페이지로의 이동 확인)
  - 특정 데이터를 입력하고 저장
  - 저장된 데이터가 올바르게 표시되는지 확인

요구사항
  - 프로그래밍 언어는 Java 또는 파이썬 중 선택하세요.
  - 코드의 가독성과 유지보수성 고려하세요.
  - 필요한 경우 적절한 대기 시간(Explicit Wait)을 구현하세요.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 웹 드라이버 설정 (예: Chrome)
# Chrome 브라우저 드라이버를 사용하여 새로운 브라우저 창 열기
driver = webdriver.Chrome()

try :
  # 1. 로그인 페이지로 이동
  driver.get('https://example.com/login')
  
  # 2. 사용자명과 비밀번호 입력
  username = drivier.find_element(By.ID,'username')
  password = driver.find_element(By.ID, 'password')

  username.send_keys('testuser')
  password.send_keys('testpassword')

  # 3. 로그인 버튼 클릭
  login_button = driver.find_element(By.ID,'loginButton')
  login_button.click()

  # 4. 로그인 성공 여부 확인
  WebDriverWait(driver,10).until(
   EC.presence_of_element_located((By.ID,'profileLink')) 
  )

  printf("로그인 성공")

  # 5. 데이터 입력 페이지로 이동
  driver.get('https://example.com/data-entry')

  # 6. 데이터 입력 및 저장
  data_field = driver.find_element(By.ID, 'dataField')
  data_field.send_keys('자동화 테스트 데이터')

  save_button = driver.find_element(By.ID, 'saveButton')
  save_button.click()

  # 7. 저장된 데이터 확인
  # 특정 요소가 조건을 만족할 때까지 최대 10초까지 대기
  WebdriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
      (By.ID, 'dataDispplay'), '자동화 테스트 데이터')
    )
  # 동기화 처리
  # EC.text_to_be_present_in_element, EC.presence_of_element_located
  
  displayed_data = driver.find_element(By.ID, 'DisplayData').text
  assert displayed_data == '자동화 테스트 데이터'
  # assert 문 : 예상되는 결과와 실제 결과를 비교하여 테스트 성공 여부 판단
  print("데이터 저장 및 확인 성공")

expected Exception as e :
  print(f"테스트 중 오류 방생 : {e}")

finally:
  # 브라우저 닫기
  driver.quit()
  
