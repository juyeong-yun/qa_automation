/*
Appium으로 모바일 앱 자동화 테스트

제공된 모바일 앱의 특정 기능(예: 회원가입 프로세스)을 Appium을 사용하여 자동화하세요

평가 포인트
  - 모바일 플랫폼 이해도 : 안드로이드/iOS 차이점, UI 요소 식별
  - 자동화 스크립트 작성 능력 : 안정적인 테스트를 위한 코드 작성
  - 환경 설정 능력 : Appium 서버 설정, 에뮬레이터 또는 실제 디바이스 연결

문제 설명
주어진 안드로이드 앱의 회원가입 기능을 Appium을 사용하여 자동화 하세요
  - 앱 실행
  - 회원가입 페이지로 이동
  - 사용자 정보 입력 (이름, 이메일, 비밀번호 등)
  - 회원가입 완료 버튼
  - 회원가입 성공 메시지 확인

  요구사항 :
   - 프로그래밍 언어는 Java 또는 Python 중 선택하세요
   - 실제 디바이스나 에뮬레이터를 사용하여 테스트하세요
   - 안정적인 스크립트를 위해 필요한 대기시간을 구현하세요.
*/

import io.appium.java_client.MobileElement;
import io.appium.java_client.android.AndroidDrivwer;
import io.appium.java_client.remote.MobileCapabilityType;

import org.openqa.selenium.remote.DesiredCapabilities;
import java.net.URL;

public class AppiumTest{
  public static void main(String[] args){
    // 앱 ium 설정 :: 테스트 할 디바이스와 앱의 정보를 설정
    DesiredCapabilities caps = new DesiredCapabilities();
    caps.setCapability(MobileCapabilityType.PLATFORM_NAME, "Android");
    caps.setCapability(MobileCapabilityType.DEVICE_NAME, "emulator-5544");
    caps.setCapability(MobileCapabilityType.APP, "/path/to/app.apk");
    
    // 앱 패키지와 액티비티 설정
    caps.setCapability("appPackage", "com.example.app");
    caps.setCapability("appActivity", "com.example.app.MainActivity");

    try{
      AndroidDriver<MobileElement> driver = new AndroidDriver<>(
        new URL("http://127.0.../wd/hub"), caps
      );

      // 1. 회원가입 페이지로 이동
      MobileElement signUpButton = driver.findElementById("com.example.app:id/signUpButton");
      signUpButton.click();

      // 2. 사용자 정보 입력
      MobileElement nameField = driver.findElementById("com.example.app:id/nameField");
      MobileElement emailField = driver.findElementById("com.example.app:id/emailField");
      MobileElement passwordField = driver.findElementById("com.example.app:id/passwordField");

      nameField.sendKeys("테스트 사용자");
      emailField.sendKeys("testuser@example.com");
      passwordField.sendKeys("testpassword");

      // 3. 회원가입 완료 버튼 클릭
      MobileElement submitButton = driver.findElementById("com.example.app:id/submitButton");
      submitButton.click();

      // 4. 회원가입 성공 메시지 확인
      MobileElement successMassage = driver.findElementById("com.example.app:id/successMassage");
      if(successMassage.isDisplayed()){
        System.out.println("회원가입 성공");
      } else {
        System.out.println("회원가입 실패");
      }

      // 테스트 완료 후 앱 종료
      driver.quit();
    } catch(Exception e){
      e.printStackTrace();
    }
}
