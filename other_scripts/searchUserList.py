import requests, sys, json
sys.stdout = open('./output/mypage.txt', 'w', encoding='utf-8')

ieilms = "https://ieilms.jbnu.ac.kr/note/searchUserList.jsp"

my_headers = {  
                'Host':'ieilms.jbnu.ac.kr',
                'Cookie':'_ga=GA1.3.1394965306.1644477054; _gid=GA1.3.658249068.1681873236; username=; JSESSIONID=573BD0A44030A2A819CC85CC95E310B2.i-0c156e517c7e97d65; _gat=1; AWSALB=+pc9VIcMOqFkNkYx4tqQsxPY3LOngMN48xkQ9wotdjn/MwVm8wWSC8P4FSUqaF4rIc4zZlBtqC2fSgQm8Ar1bjH4XBczTZmupNDi9IXjpoG0Xnk4YwFDLox6ryGk; AWSALBCORS=+pc9VIcMOqFkNkYx4tqQsxPY3LOngMN48xkQ9wotdjn/MwVm8wWSC8P4FSUqaF4rIc4zZlBtqC2fSgQm8Ar1bjH4XBczTZmupNDi9IXjpoG0Xnk4YwFDLox6ryGk;',
                'Content-Length':'61',
                'Sec-Ch-Ua':'"Not A(Brand";v="24", "Chromium";v="110"',
                'Accept':'text/html, */*; q=0.01',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With':'XMLHttpRequest',
                'Sec-Ch-Ua-Mobile':'?0',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36',
                'Sec-Ch-Ua-Platform':'"Linux"',
                'Origin':'https://ieilms.jbnu.ac.kr',
                'Sec-Fetch-Site':'same-origin',
                'Sec-Fetch-Mode':'cors',
                'Sec-Fetch-Dest':'empty',
                'Referer':'https://ieilms.jbnu.ac.kr/note/sendNote2.jsp',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'en-US,en;q=0.9'
                }

my_cookies = {'JBNUHub_202012178_GROUP_ID':'0',
                'JSESSIONID':'573BD0A44030A2A819CC85CC95E310B2.i-0c156e517c7e97d65',
                '_ga':'GA1.3.1394965306.1644477054',
                '_gat':'1',
                '_gid':'GA1.3.658249068.1681873236',
                '_ga_QGX8XGKVMF':'GS1.1.1672696951.14.1.1672696997.0.0.0',
                'AWSALB':'+pc9VIcMOqFkNkYx4tqQsxPY3LOngMN48xkQ9wotdjn/MwVm8wWSC8P4FSUqaF4rIc4zZlBtqC2fSgQm8Ar1bjH4XBczTZmupNDi9IXjpoG0Xnk4YwFDLox6ryGk',
                'AWSALBCORS':'+pc9VIcMOqFkNkYx4tqQsxPY3LOngMN48xkQ9wotdjn/MwVm8wWSC8P4FSUqaF4rIc4zZlBtqC2fSgQm8Ar1bjH4XBczTZmupNDi9IXjpoG0Xnk4YwFDLox6ryGk',
                'bHideResizeNotice':'1',
                'username':''
                }

my_params = {'tcate_id':'1',
                'search_name':'%EA%B9%80%EC%95%84%EC%9D%80',
                'group_id':'0'
                }

response = requests.post(url=ieilms, headers=my_headers, cookies=my_cookies, data=json.dumps(my_params))
print(my_params)
print(response)
print(response.text)