import requests
import sys

sys.stdout = open('./output/login_3.txt', 'w', encoding='utf-8')

print("====================================\tlogin\t\t\t====================================")

login = "https://ieilms.jbnu.ac.kr/login/authLoginProc.jsp"

login_headers = {  
                'Host':'ieilms.jbnu.ac.kr',
                'Cookie':'_ga=GA1.3.1376819658.1681869464; _gid=GA1.3.1885052582.1685080953; AWSALB=2ygF4vfjRdmeDtZJZciiJUmQhTSeQWg0/NxJ+bEFYo0iPulY5xOmVx+09YmQRNRK++uEetGIpXgiBa4gMSTpmueC9tWBEjemWvs/HUBWTzOni/mPdnRqt62o1IIX; AWSALBCORS=2ygF4vfjRdmeDtZJZciiJUmQhTSeQWg0/NxJ+bEFYo0iPulY5xOmVx+09YmQRNRK++uEetGIpXgiBa4gMSTpmueC9tWBEjemWvs/HUBWTzOni/mPdnRqt62o1IIX; JSESSIONID=1234FD2F714C46FBB398600159AD32C1.i-12343da02702cd919;',
                'Content-Length':'37',
                'Sec-Ch-Ua':'"Not A(Brand";v="24", "Chromium";v="110"',
                'Accept':'*/*',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With':'XMLHttpRequest',
                'Sec-Ch-Ua-Mobile':'?0',
                'Sec-Ch-Ua-Platform':'"Linux"',
                'Upgrade-Insecure-Requests':'1',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36',
                'Origin':'https://ieilms.jbnu.ac.kr',
                'Sec-Fetch-Site':'same-origin',
                'Sec-Fetch-Mode':'navigate',
                'Sec-Fetch-Dest':'document',
                'Referer':'https://ieilms.jbnu.ac.kr/',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'en-US,en;q=0.9'
                }

r = requests.post(login, headers=login_headers, data = {'login':'~id~', 'passwd':'~passwd~'})

print(r.status_code)
print(r.text+"\n")


print("====================================\tmove to group\t====================================")

group = "https://ieilms.jbnu.ac.kr/mypage/group/"

my_headers = {  
                'Host':'ieilms.jbnu.ac.kr',
                'Cookie':'_ga=GA1.3.1376819658.1681869464; _gid=GA1.3.1885052582.1685080953; AWSALB=2ygF4vfjRdmeDtZJZciiJUmQhTSeQWg0/NxJ+bEFYo0iPulY5xOmVx+09YmQRNRK++uEetGIpXgiBa4gMSTpmueC9tWBEjemWvs/HUBWTzOni/mPdnRqt62o1IIX; AWSALBCORS=2ygF4vfjRdmeDtZJZciiJUmQhTSeQWg0/NxJ+bEFYo0iPulY5xOmVx+09YmQRNRK++uEetGIpXgiBa4gMSTpmueC9tWBEjemWvs/HUBWTzOni/mPdnRqt62o1IIX; JSESSIONID=1234FD2F714C46FBB398600159AD32C1.i-12343da02702cd919;',
                'Sec-Ch-Ua':'"Not A(Brand";v="24", "Chromium";v="110"',
                'Sec-Ch-Ua-Mobile':'?0',
                'Sec-Ch-Ua-Platform':'"Linux"',
                'Upgrade-Insecure-Requests':'1',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site':'same-origin',
                'Sec-Fetch-Mode':'navigate',
                'Sec-Fetch-Dest':'document',
                'Referer':'https://ieilms.jbnu.ac.kr/',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'en-US,en;q=0.9'
                }

response = requests.post(url=group, headers=my_headers)

print("====================================\tCookie\t\t====================================")
print(my_headers['Cookie'])
print("====================================\tResponse\t====================================")
print(response)
print(response.text)