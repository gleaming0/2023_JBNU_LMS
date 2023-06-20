import requests, sys
sys.stdout = open('./output/ssrf_2.txt', 'w', encoding='utf-8')

# def theLoadComplete(response):
#     list_element = document.getElementById("dataList")
#     list_element.innerHTML = response.text

url = "https://ieilms.jbnu.ac.kr/mypage/data/dataList_Pubcate.jsp"
note = "'AI' 자료 검색 요청"

my_headers = {  
                'Host':'ieilms.jbnu.ac.kr',
                'Cookie':'JSESSIONID=E20967126E518C9A1D1CE899E979B1B9.i-0c156e517c7e97d65;',
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

params = {
    "data_cate_id": 0,
    "start": 1,
    "pub_ck": 2,
    "group_id": 43935,
    "text": "AI"
}



response = requests.post(url, headers=my_headers, data=params)

print("* " + note + " *\n")
print("====================================\tCookie\t\t====================================")
print(my_headers['Cookie'])
print("====================================\tParameter\t====================================")
print(params)
print("====================================\tResponse\t====================================")
print("HTTP 상태 코드:", response.status_code)
print(response.text)

# theLoadComplete(response)
