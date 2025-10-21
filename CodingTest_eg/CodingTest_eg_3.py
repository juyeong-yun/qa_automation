"""
CodingTest_eg_3.java와 동일 문제 > 파이썬으로 작성

문제 설명
주어진 안드로이드 앱의 회원가입 기능을 Appium을 사용하여 자동화 하세요
  - 앱 실행
  - 회원가입 페이지로 이동
  - 사용자 정보 입력 (이름, 이메일, 비밀번호 등)
  - 회원가입 완료 버튼
  - 회원가입 성공 메시지 확인  
"""
from appium import webdriver
from appium.wbdriver.common.mobility from MobileBy
from selenium.webdriver.support.ui import WebdriverWait
from selenium.webdriver.support import expected_conditions as EC

# Appium 설정
# caps :: 디바이스와 앱의 설정 정보를 담는 딕셔너리
caps = {}
caps['platformName'] = 'Android' # 테스트 할 플랫폼 
caps['deviceName'] = 'emulator5554' # 테스트 할 디바이스명(에뮬레이터나 실제 디바이스 이름 사용)
caps['app'] = '/path/to/app.apk' # 테스트할 앱의APK 파일 경로 지정

# 앱 패키지와 액티비티 설정
caps['appPakage'] = 'com.example.app'
caps['appActivity'] = 'com.example.app.MainActivity'

try:
  # 드라이버 생성
  driver = webdriver.Remote('http://127.0.../wd/hub', caps)

  # 1. 회원가입 페이지로 이동
  sign_up_button = driver.find_element(MobileBy.ID, 'com.example.app:id/signUpButton')
  sign_up_button.click()

  /*
  # 동적 대기 처리 가능
  # 회원가입 버튼이 클릭 가능할 때까지 최대 10초 대기
  sign_up_button = WebdriverWait(driver,10).until(
    EC.element_to_be_clickable(MobileBy.ID,'com.example.app:id/signUpButton)
  )
  */

  # 2. 사용자 정보 입력
  name_field = driver.find_element(MobileBy.ID, 'com.example.app:id/name_field')
  email_field = driver.find_element(MobileBy.ID, 'com.example.app:id/email_field')
  password_field = driver.find_element(MobileBy.ID, 'com.example.app:id/password_field')

  name_field.send_keys('테스트 사용자')
  email_field.send_keys('testuser@example.com')
  password_field.send_keys('testpassword')

  # 3. 회원가입 완료 버튼 클릭
  submit_button = driver.find_element(MobileBy.ID, 'com.example.app:id/submitButton')
  submit_button.click();

  # 4. 회원가입 성공 메시지
  success_massage = driver.find_element(MobileBy.ID, 'com.example.app:id/sucessMassage')

  if success_massage.is_displayed() :
    print('회원가입 성공')
  else :
    print('회원가입 실패')

  # 테스트 완료 후 앱 종료
  driver.quit()

except Exception as e :
  print(e)
  driver.save_screenshot('error.png') 
  # 테스트 중 에러 발생 시 화면을 캡쳐하여 저장하면 디버깅 시 도움이 된다.
