/*
Postman을 활용한 API 테스트 스트립트 작성
특정 RESTful API 엔드포인트에 대한 테스트 시나리오를 작성하고,
Postman 또는 JMeter를 사용하여 이 시나리오를 자동화 하세요.
로그인, 데이터 생성, 수정, 삭제 등의 기능을 포함하면 좋습니다.

- 평가 포인트
  - API 이해도 : HTTP 메서드, 상태 코드, 인증 방식 등에 대한 이해
  - 자동화 능력 : 스크립트 작성 및 환경 설정 능력
  - 에러 처리 : 예외 상황에 대한 테스트 커버리지.
*/

/*
Step 1 : 로그인

Request : 
 - Method : POST
 - URL  : https://api.example.com/auth/login
 - Headers : Content-Type: application/json
 - Body : JSON 형식으로 사용자 자격 증명 전송
*/
{
  "username" : "testuser",
  "password" : "testpassword"
}

pm.test("Status code is 200", function(){
  pm.response.to.have.status(200);
});

// 액세스 토큰 저장
var jsonData = pm.responsse.json();
pm.environment.set("acccessToken", jsonData.acessToken);

/*
Step 2 : 데이터 생성

Request: 
  - Method : POST
 - URL  : https://api.example.com/posts
 - Headers : 
   - Content-Type: application/json
   - Authorization: Bearer{{accessToken}}
 - Body :
*/
{
  "title" : "테스트 게시글",
  "content" : "이것은 자동화 테스트로 생성된 게시글 입니다."
}

pm.test("Status code is 201", function(){
  pm.response.to.have.status(201);
});

var jsonDdata = pm.response.json();
pm.environment.set("postid", jsonData.id);

/*
Step 3 : 데이터 조회

Request: 
  - Method : GET
  - URL  : https://api.example.com/posts/{{postid}
  - Headers : 
   - Authorization: Bearer{{accessToken}}
 - Body :
*/
pm.test("Status code is 200", function(){
  pm.response.to.have.status(200);
});

pm.test("Correct post is returned", function(){
  var jsonData = pm.response.json();
  pm.expect(jsonData.id).to.eql(pm.environment.get("postid"));
});

/*
Step 4 : 데이터 수정

Request: 
  - Method : PUT
  - URL  : https://api.example.com/posts/{{postid}
  - Headers : 
   - Content-Type: application/json
   - Authorization: Bearer{{accessToken}}
  - Body :
*/
{
  "title" : "수정된 테스트 게시글",
  "content" : "이 게시글은 자동화 테스트로 수정되었습니다."
}
pm.test("Status code is 200", function(){
  pm.response.to.have.status(200);
});

/*
Step 5 : 데이터 삭제

Request: 
  - Method : DELETE
 - URL  : https://api.example.com/posts/{{postid}
 - Headers : 
   - Authorization: Bearer{{accessToken}}
 - Body :
*/
pm.test("Status code is 200", function(){
  pm.response.to.have.status(200);
});

/*
Step 6 : 로그아웃

Request: 
  - Method : POST
 - URL  : https://api.example.com/auth/logout
 - Headers : 
   - Content-Type: application/json
   - Authorization: Bearer{{accessToken}}
 - Body :
*/
pm.test("Status code is 200", function(){
  pm.response.to.have.status(200);
});

// 환경변수 초기화
pm.environment.unset("accessToken");
pm.environment.unset("postid");
