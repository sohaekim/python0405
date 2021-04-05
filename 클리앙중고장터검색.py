# coding:utf-8
# 웹 크롤링
from bs4 import BeautifulSoup
# 웹서버에 요청
import urllib.request
# 정규표현식
import re

# User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더)
# 웹봇(자동화된 프로그램)인척 ?
hdr = {
    'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

# 클리앙은 한 페이지가 30 * 10개 페이지 => 300
for n in range(0, 10):
    # 클리앙의 중고장터 주소
    data = 'https://www.clien.net/service/board/sold?&od=T31&po=' + \
        str(n)  # 정수를 문자열로
    # 웹브라우져 헤더 추가
    print(data)
    req = urllib.request.Request(data,
                                 headers=hdr)
    data = urllib.request.urlopen(req).read()
    # 공공사이트는 decode 사용 안함(커뮤니티는 사용)
    page = data.decode('utf-8', 'ignore')
    soup = BeautifulSoup(page, 'html.parser')


# <span class="subject_fixed" data-role="list-title-text">
# 아이폰11프로 256 스그 ios13.6.1 팝니다.</span>
# attrs 어트리뷰트들 딕셔너리{ 키:값}

    list = soup.findAll('span', attrs={'data-role': 'list-title-test'})

    for item in list:
        try:

            # print(item.text)

            if (re.search('아이폰', title)):
                print(title.strip())
            #         print('https://www.clien.net'  + item['href'])
        except:
            pass
