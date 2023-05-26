import requests, sys, json
sys.stdout = open('./output/index_3.txt', 'w', encoding='utf-8')

ieilms = "https://ieilms.jbnu.ac.kr/mypage/group/index.jsp"
note = "대인이 JSESSIONID 쿠키값"

my_headers = {  
                'Host':'ieilms.jbnu.ac.kr',
                'Cookie':'JSESSIONID=E9ACCAD03666C4E503F24739216CDF80.i-09353da02702cd919;',
                'Cache-Control':'max-age=0',
                'Sec-Ch-Ua':'"Not A(Brand";v="24", "Chromium";v="110"',
                'Sec-Ch-Ua-Mobile':'?0',
                'Sec-Ch-Ua-Platform':'"Linux"',
                'Upgrade-Insecure-Requests':'1',
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


response = requests.post(url=ieilms, headers=my_headers)

print("* " + note + " *\n")
print("====================================\tCookie\t\t====================================")
print(my_headers['Cookie'])
print("====================================\tResponse\t====================================")
print(response)
print(response.text)