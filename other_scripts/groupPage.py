import requests, sys, json
sys.stdout = open('./output/groupPage_7.txt', 'w', encoding='utf-8')

ieilms = "https://ieilms.jbnu.ac.kr/mypage/group/groupPage.jsp"
note = "로그아웃 후 바뀐 JSESSIONID 쿠키값으로 연결 시도"

my_headers = {  
                'Host':'ieilms.jbnu.ac.kr',
                'Cookie':'JSESSIONID=87AD4CFBD7D3A2C7A224B15EB62B6F57.i-0772391701db78309;',
                'Content-Length':'152',
                'Cache-Control':'max-age=0',
                'Sec-Ch-Ua':'"Not A(Brand";v="24", "Chromium";v="110"',
                'Sec-Ch-Ua-Mobile':'?0',
                'Sec-Ch-Ua-Platform':'"Linux"',
                'Upgrade-Insecure-Requests':'1',
                'Origin':'https://ieilms.jbnu.ac.kr',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site':'same-origin',
                'Sec-Fetch-Mode':'navigate',
                'Sec-Fetch-User':'?1',
                'Sec-Fetch-Dest':'document',
                'Referer':'https://ieilms.jbnu.ac.kr/mypage/group/index.jsp',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'en-US,en;q=0.9'
                }

my_params = {'group_id':'44475',
                'group_name':'2023-1%ED%95%99%EA%B8%B0+%EC%82%B0%ED%95%99%EC%8B%A4%EC%A0%84%EC%BA%A1%EC%8A%A4%ED%86%A4+2%281%EB%B6%84%EB%B0%98%29',
                'openTerm':'1'
                }

response = requests.post(url=ieilms, headers=my_headers, data=json.dumps(my_params))

print("* " + note + " *\n")
print("====================================\tCookie\t\t====================================")
print(my_headers['Cookie'])
print("====================================\tParameter\t====================================")
print(my_params)
print("====================================\tResponse\t====================================")
print(response)
print(response.text)