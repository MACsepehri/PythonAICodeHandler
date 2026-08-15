import requests
from bs4 import BeautifulSoup

def GeeksForGeeks(Input, Language):
    try:
        query = f"{Language} {Input}"
        url = f"https://www.geeksforgeeks.org/?s={query.replace(' ', '+')}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        
        results = []
        articles = soup.find_all("article")
        
        for article in articles[:10]:
            title_tag = article.find("h2")
            if title_tag:
                link_tag = title_tag.find("a")
                if link_tag:
                    results.append({
                        'title': link_tag.text.strip(),
                        'url': link_tag.get('href')
                    })
        
        return (results, True) if results else (False, False)
        
    except requests.exceptions.ConnectionError:
        return "Please check your internet connection.\nTry again later."
    except requests.exceptions.Timeout:
        return "Request timed out.\nTry again later."
    except Exception as e:
        return f"An error occurred:\n{str(e)}"