import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

def get_naver_news_content(news_url):
    """네이버 뉴스 URL에서 뉴스 본문을 가져옴"""
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(news_url, headers=headers)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        
        # 네이버 뉴스 본문이 있는 태그 탐색
        content = soup.select_one("#dic_area")  # 네이버 뉴스 본문 영역

        if content:
            return content.get_text(strip=True)
        else:
            return "본문을 찾을 수 없습니다."
    else:
        return "페이지 로드 실패"

# 예제 실행
news_url = "https://n.news.naver.com/mnews/article/001/0014345678"  # 실제 뉴스 URL 사용
news_content = get_naver_news_content(news_url)
print(news_content)


def search_naver_news(keyword, url=None):
    if url is None:
        url = f"https://search.naver.com/search.naver?where=news&query={keyword}&sm=tab_tmr&nso=so:r,p:all,a:all&sort=0"
        
    res = requests.get(url)
    ret = []
    if res.status_code == 200:
        html = res.text 
        
        soup = BeautifulSoup(html, 'html.parser')
        news_title = soup.select('.news_tit')
        
        ret = []
        for title in news_title:
            ret.append({title.text: title['href']})
        
        return ret
            
    else:
        return ret

# def search_naver_news(keyword, url=None):
#     if url:
#         url = f"https://search.naver.com/search.naver?where=news&query={keyword}&sm=tab_tmr&nso=so:r,p:all,a:all&sort=0"
        
#     res = requests.get(url)

#     if res.status_code == 200:
#         html = res.text 
        
#         soup = BeautifulSoup(html, 'html.parser')
#         news_title = soup.select('.news_tit')
        
#         for title in news_title:
#             print(title.text)
#             print(title['href'])
            
#             print()
            
#     else:
#         return None


if __name__ == '__main__':
    keyword = '삼성전자'
    
    naver_news = search_naver_news(keyword)
    
    