import requests
from bs4 import BeautifulSoup
import urllib.parse

class Stackoverflow:
    def search(self, Input, max_results=10, sort="relevance"):
        url = f"https://api.stackexchange.com/2.3/search/advanced"
        params = {
            "order": "desc",
            "sort": sort,
            "q": Input,
            "site": "stackoverflow",
            "pagesize": min(max_results, 100),
        }
        
        try:
            req = requests.get(url, params=params, timeout=10)
            req.raise_for_status()
            
            data = req.json()
            
            if data.get("error"):
                print(f"API Error: {data['error']['message']}")
                return None
            
            if data.get("items"):
                return data["items"]
            else:
                print("No Stack Overflow results found")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
        except ValueError as e:
            print(f"Invalid JSON response: {e}")
            return None

class W3Schools:
    def __init__(self):
        self.tutorials = {
            "html": [
                {"title": "HTML Tutorial", "link": "https://www.w3schools.com/html/"},
                {"title": "HTML Div Tag", "link": "https://www.w3schools.com/tags/tag_div.asp"},
                {"title": "HTML Forms", "link": "https://www.w3schools.com/html/html_forms.asp"},
                {"title": "HTML Tables", "link": "https://www.w3schools.com/html/html_tables.asp"},
            ],
            "css": [
                {"title": "CSS Tutorial", "link": "https://www.w3schools.com/css/"},
                {"title": "CSS Flexbox", "link": "https://www.w3schools.com/css/css3_flexbox.asp"},
                {"title": "CSS Grid", "link": "https://www.w3schools.com/css/css_grid.asp"},
                {"title": "CSS Selectors", "link": "https://www.w3schools.com/css/css_selectors.asp"},
            ],
            "python": [
                {"title": "Python Tutorial", "link": "https://www.w3schools.com/python/"},
                {"title": "Python Lists", "link": "https://www.w3schools.com/python/python_lists.asp"},
                {"title": "Python Functions", "link": "https://www.w3schools.com/python/python_functions.asp"},
                {"title": "Python JSON", "link": "https://www.w3schools.com/python/python_json.asp"},
            ],
            "javascript": [
                {"title": "JavaScript Tutorial", "link": "https://www.w3schools.com/js/"},
                {"title": "JavaScript Functions", "link": "https://www.w3schools.com/js/js_functions.asp"},
                {"title": "JavaScript DOM", "link": "https://www.w3schools.com/js/js_htmldom.asp"},
            ],
            "sql": [
                {"title": "SQL Tutorial", "link": "https://www.w3schools.com/sql/"},
                {"title": "SQL SELECT", "link": "https://www.w3schools.com/sql/sql_select.asp"},
            ]
        }
    
    def search(self, Input):
        Input_lower = Input.lower()
        results = []
        added_links = set()
        
        for topic, tutorials in self.tutorials.items():
            if topic in Input_lower:
                for tut in tutorials:
                    if tut["link"] not in added_links:
                        results.append(tut)
                        added_links.add(tut["link"])
        
        if not results:
            results = self.tutorials.get("html", [])
        
        return results

class TrainerModel:
    def __init__(self):
        self.data = []
        self.stackoverflow = Stackoverflow()
        self.w3school = W3Schools()
    
    def validInput(self, Input: str):
        if Input == "":
            return False
        elif Input == " ":
            return False
        elif Input.replace(" ", "") == "":
            return False
        return True

    def train(self, data):
        if data not in self.data:
            self.data.append(data)

    def find(self, inp):
        for val in self.data:
            if inp.lower() in val.lower():
                return True
        return False

    def process(self, Input: str):
        result = ""
        if not self.validInput(Input):
            return "Please enter a valid input."
        
        if not self.find(Input):
            stackoverflow_results = self.stackoverflow.search(Input)
            if stackoverflow_results:
                for idx, item in enumerate(stackoverflow_results[:5], 1):
                    result += f"{item['link']}\n"
            else:
                result += "No Stack Overflow results found.\n\n"
            
            w3school_results = self.w3school.search(Input)
            if w3school_results:
                for idx, item in enumerate(w3school_results[:5], 1):
                    result += f"{item['link']}\n"
            else:
                result += "No W3Schools results found.\n"
            
            self.train(result)
            return result
        else:
            for val in self.data:
                if Input.lower() in val.lower():
                    return val
            return None