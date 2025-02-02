import requests
from bs4 import BeautifulSoup

def scrape_samsung_news():
    url = 'https://finance.yahoo.com/quote/005930.KS/news?p=005930.KS'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        news_items = soup.find_all('h3')
        
        if not news_items:
            print("No news items found. The page structure might have changed.")
            return
        
        print("Recent Samsung News Headlines:")
        for item in news_items:
            print(item.text.strip())
    
    except requests.RequestException as e:
        print(f"An error occurred while fetching the page: {e}")

scrape_samsung_news()
