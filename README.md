# 전북대학교 스마트학습관리시스템(LMS) 웹 취약점 점검

## 🔎 Scanning Port
+ `other_scripts/ponic.py (14p)`
+ 웹 서버에서 사용하는 DBMS를 추정하기 위해 선정해둔 DBMS의 기본 사용 포트가 열려있는지 스캔

## 👩🏻‍💻 LDAP Injection
+ `injection_code/Injection_LDAP.py (47p)`
+ 로그인 폼에 LDAP 쿼리문을 주입하여 로그인 우회가 일어나는지 점검

## ➕ Others..
### authLogin
+ `other_scripts/authLoginProc.py`
+ 로그인 인증 동작 확인

### searchUser
+ `other_scripts/serachUserList.py`
+ 쪽지 수신자에 대한 검색 결과 추출

### SSRF
+ `other_scripts/ssrf.py`
+ SSRF 취약점 점검을 위해 내부 동작 확인

### phishing page
+ `phishing_page/*`
+ 전북대학교 LMS 피싱 페이지 제작 후 사용자의 ID/PW 값 획득 시도
+ http://210.117.181.90:5080/JBNU_LMS.html
