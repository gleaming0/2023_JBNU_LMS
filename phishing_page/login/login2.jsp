
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ko" xml:lang="ko">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=Edge"/>
<title>전북대학교 스마트학습관리시스템</title>
<link rel="StyleSheet" href="/jscss/pure.css" type="text/css" title="style" />
<script src="/jscss/jquery-1.10.2.js"></script>
<script type="text/javascript" >
<!--
function readcookie() {
   var yourname = document.cookie
   var f = document.loginform;
   f.idsave.checked = false;
   if(yourname.length > 0) {
	   var ca = document.cookie.split(';');
	   for(var i=0; i<ca.length;i++){
		   	var yourname = ca[i];
      		if(yourname.indexOf("username=") != -1) {
        		yourname=yourname.substring(yourname.indexOf("username=")+9,  yourname.length);
         		if(yourname.length > 0) {
          			f.login.value= yourname;
           			f.idsave.checked = true;
         		}
      		}
      	}
   }
}

function check_login_form() {
	var f = document.loginform;
	var loginsave = document.getElementById("loginsave");
	if(f.login.value == ""){
		alert("아이디를 입력해주세요.");
		f.login.focus();
		return;
	}

	var id = f.login.value;
    /*if(!/^[a-zA-Z0-9@._\-]+$/.test(id))
    {
        alert('아이디는 알파벳, 숫자, 문자(@ . - _)만 가능합니다.');
        f.login.focus();
        return;
    }*/

    if(id.length > 40)
    {
        alert('아이디는 최대 40글자까지 입력해주세요.');
        f.login.focus();
        return;
    }

	saveID();

	if(f.passwd.value == ""){
		alert("비밀번호를 입력해주세요.");
		f.passwd.focus();
		return;
	}

	/*
	if(f.passwd.value.length < 8)
    {
        alert('비밀번호는 최소 8글자입니다.');
        f.passwd.focus();
        return;
    }

	if(!/^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,24}$/.test(f.passwd.value))
    {
        alert('비밀번호는 대/소문자, 숫자, 특수문자의 조합으로 최소 8자 이상입니다.');
        f.passwd.focus();
        return;
    }*/

	if(loginsave.checked == true)
		loginsave.value = 1;

	var string = $("form[name=loginform]").serialize();

	$.ajax({
		type:"POST",
		url:"/login/authLoginProc.jsp",
		data: string,
		success: function(text){
	        cb_login(text);
	    }
	});
}

function cb_login(req) {
	if(req.indexOf("newuser") >= 0) {
		location.href="/login/serviceRule.jsp";
	}else if(req.indexOf("moduser") >= 0) {
		location.href="/login/memEdit.jsp";
	}else if(req.indexOf("success") >= 0) {
		if(req.indexOf("mypage") >= 0) location.href="/mypage/";
		else if(req.indexOf("group") >= 0) location.href="/mypage/group/";
		else {
			if(req.replace("success","").length > 0)
				location.href="/mypage/group/index.jsp";
			else
				location.href="/mypage/group/";
		}
	}else{
		alert(req);
		document.loginform.login.focus();
		document.loginform.passwd.value = "";
	}
}

function saveID() {
  var f = document.loginform;
  var idsave = document.getElementById("idsave");
  if (idsave.checked == true) {
	  makecookieId(f.login.value);
  }
  else
	   UnSaveID();
}

function UnSaveID() {
	  var todayDate = new Date();
	  todayDate.setDate(todayDate.getDate() + 365);

	  var cookies = document.cookie.split("; ");
	  var tmpCookie = "username=;";
	  for(var i = 0; i < cookies.length; i++){
		  if(cookies.indexOf("username=") != -1) continue;
		  tmpCookie += cookies[i].split("=")[0] + "=" + cookies[i].split("=")[1] + ";"
	  }
	  document.cookie= tmpCookie + "expires="+ todayDate.toGMTString()+";path=/";
}

function makecookieId(id) {
	  var todayDate = new Date();
	  todayDate.setDate(todayDate.getDate() + 365);

	  var cookies = document.cookie.split("; ");
	  var tmpCookie = "username="+id + ";";
	  for(var i = 0; i < cookies.length; i++){
		  if(cookies.indexOf("username=") != -1) continue;
	      tmpCookie += cookies[i].split("=")[0] + "=" + cookies[i].split("=")[1] + ";"
	  }
	  document.cookie= tmpCookie + "expires=" + todayDate.toGMTString()+";path=/";
}

function keepingLogin() {
	var lk = document.getElementById("loginsave");
	if(lk.checked == true) {
		if(!confirm("자동 로그인 기능을 사용하시겠습니까?\n단, 공공장소(PC방, 학교 등)에서 이용시 개인정보가 유출될 수 있으니 주의하시길 바랍니다.\n로그인 상태를 한 달간 유지하시려면 [확인] 버튼을, 취소를 원하시면\n[취소] 버튼을 클릭해주세요.")){
			lk.checked = false;
		}
		return;
	}
}
//-->
</script>
<style type="text/css">
	#check input{ vertical-align:-2px; }
</style>
</head>
<body onload="readcookie();">
<center>
<form class="pure-form" name="loginform" method="post" action="javascript:check_login_form();">
	<fieldset class="pure-group">
		<div style="margin-top:50px;"><a href="/"><img src="/img/logo2.gif" alt="logo Image" /></a></div>
	</fieldset>
	<fieldset class="pure-group">
		<div style="font-size:10pt;">전북대 포털 ID(학번 또는 사번) 로 로그인 하시면<br/>전북대학교 스마트학습관리시스템 서비스를 이용하실 수 있습니다.</div>
		<div class="loginText"  style="line-height:160%;font-size:10pt;padding:10px; 0">
					<span style="color:#5d3880"><b>교수님께서는 재직 중인 개인 사번으로 로그인해주십시오</b></span>
		</div>
	</fieldset>
    <fieldset class="pure-group">
        <input type="text" class="pure-input-1-3" placeholder="학번 or 사번" tabindex=1 name="login" id="id" />
        	<label for="id" style="font-size:0;">아이디</label>
     </fieldset>
    <fieldset class="pure-group">
        <input type="password" name="passwd" class="pure-input-1-3"  placeholder="비밀번호"  tabindex=2 id="passwd" autocomplete="off" />
        	<label for="passwd" style="font-size:0;">비밀번호</label>
    </fieldset>
    <button type="submit" class="pure-button pure-input-1-3 notice">로그인</button>
    <fieldset>
	    <label style="font-size:10pt;" id="check">
	    	<input type="checkbox" name="idsave" id="idsave" value="1"/>아이디 저장
			<input type="checkbox" name="loginsave" id="loginsave" value="0" onclick="javascript:keepingLogin();" />로그인 상태 유지
		</label>
	</fieldset>
	<div class="pure-menu pure-menu-open pure-menu-horizontal" style="font-size:10pt;">
	    <ul>
			<li><a href="https://oasis.jbnu.ac.kr/com/Search_Pwd.do" target="_blank" >아이디 / 비밀번호 찾기</a></li>
<li><a href="javascript:alert('회원가입을 하실 필요가 없습니다.\n전북대학교 오아시스 로그인 정보로 이용해주세요.');">회원가입</a></li></ul>
	</div>
</form>
</center>
</body>
</html>