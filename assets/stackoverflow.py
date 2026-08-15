import requests

def StackOverFlow(Input, Language):
    try:
        url = "https://api.stackexchange.com/2.3/search"
        
        params = {
            'order': 'desc',
            'sort': 'relevance',
            'tagged': Language,
            'intitle': Input,
            'site': 'stackoverflow',
            'pagesize': 10
        }
        
        response = requests.get(url, params=params, timeout=3)
        response.raise_for_status()
        
        data = response.json()
        
        if not data.get('items'):
            return f"No questions found for '{Input}' with tag '{Language}'"
        
        results = []
        for item in data['items']:
            results.append({
                'title': item['title'],
                'link': item['link'],
                'score': item['score'],
                'answer_count': item['answer_count']
            })
        
        return results
        
    except requests.exceptions.ConnectionError:
        return "Please check your internet connection.\nTry again later."
    except requests.exceptions.Timeout:
        return "Request timed out.\nTry again later."
    except Exception as e:
        return f"An error occurred:\n{str(e)}"