import requests
from bs4 import BeautifulSoup

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

    def extract_code_from_source(self, beautifulsoup_obj: BeautifulSoup):
        """
        Extract all code blocks from a Stack Overflow page HTML.
        
        Args:
            beautifulsoup_obj (BeautifulSoup): Parsed BeautifulSoup object of the page
            
        Returns:
            list: List of dictionaries containing code snippets and their languages
        """
        code_blocks = []
        
        # Method 1: Find all <pre><code> blocks
        pre_tags = beautifulsoup_obj.find_all('pre')
        for pre in pre_tags:
            code_tag = pre.find('code')
            if code_tag:
                code_text = code_tag.get_text().strip()
                
                # Detect language
                language = "unknown"
                if code_tag.get('class'):
                    for cls in code_tag.get('class'):
                        if cls.startswith('language-'):
                            language = cls.replace('language-', '')
                            break
                        elif cls.startswith('lang-'):
                            language = cls.replace('lang-', '')
                            break
                
                if language == "unknown" and code_tag.get('data-language'):
                    language = code_tag.get('data-language')
                
                if language == "unknown" and pre.get('class'):
                    for cls in pre.get('class'):
                        if cls.startswith('lang-'):
                            language = cls.replace('lang-', '')
                            break
                
                if code_text and len(code_text) > 0:
                    code_blocks.append({
                        'code': code_text,
                        'language': language,
                        'type': 'pre-code'
                    })
        
        # Method 2: Find code blocks in divs with s-code-block class
        code_divs = beautifulsoup_obj.find_all('div', class_='s-code-block')
        for div in code_divs:
            code_tag = div.find('code')
            if code_tag:
                code_text = code_tag.get_text().strip()
                
                language = "unknown"
                if div.get('data-language'):
                    language = div.get('data-language')
                elif div.get('class'):
                    for cls in div.get('class'):
                        if cls.startswith('language-'):
                            language = cls.replace('language-', '')
                            break
                
                if code_text and len(code_text) > 0:
                    already_exists = False
                    for existing in code_blocks:
                        if existing['code'] == code_text:
                            already_exists = True
                            break
                    
                    if not already_exists:
                        code_blocks.append({
                            'code': code_text,
                            'language': language,
                            'type': 's-code-block'
                        })
        
        return code_blocks

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
        self.training_count = 0
        self.last_query = None
    
    def get_params(self):
        return {
            'data_count': len(self.data),
            'training_count': self.training_count,
            'last_query': self.last_query,
            'has_data': bool(self.data)
        }
    
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
            self.training_count += 1
            self.last_query = data if data else None 

    def find(self, inp):
        for val in self.data:
            if inp.lower() in val.lower():
                return True
        return False

    def process(self, Input: str):
        result = {
            'stackoverflow_links': [],
            'stackoverflow_codes': [],
            'w3schools_links': [],
            'raw_response': ""
        }
        
        if not self.validInput(Input):
            result['raw_response'] = "Please enter a valid input."
            return result
        
        if not self.find(Input):
            stackoverflow_results = self.stackoverflow.search(Input)
            
            if stackoverflow_results:
                for idx, item in enumerate(stackoverflow_results[:5], 1):
                    link = item['link']
                    result['stackoverflow_links'].append({
                        'title': item.get('title', 'Untitled'),
                        'link': link
                    })
                    
                    try:
                        response = requests.get(link, timeout=10)
                        response.raise_for_status()
                        soup = BeautifulSoup(response.content, 'html.parser')
                        
                        code_blocks = self.stackoverflow.extract_code_from_source(soup)
                        
                        if code_blocks:
                            for code_block in code_blocks[:3]:
                                result['stackoverflow_codes'].append({
                                    'source_link': link,
                                    'code': code_block['code'],
                                    'language': code_block['language']
                                })
                    except Exception as e:
                        print(f"Error fetching page {link}: {e}")
            else:
                result['raw_response'] += "No Stack Overflow results found.\n\n"
            
            w3school_results = self.w3school.search(Input)
            if w3school_results:
                for item in w3school_results[:5]:
                    result['w3schools_links'].append({
                        'title': item['title'],
                        'link': item['link']
                    })
            else:
                result['raw_response'] += "No W3Schools results found.\n"
            
            formatted_response = self._format_response(result)
            result['raw_response'] = formatted_response
            
            self.train(formatted_response)
            return result
        else:
            for val in self.data:
                if Input.lower() in val.lower():
                    result['raw_response'] = val
                    return result
            return result
    
    def _format_response(self, result):
        formatted = ""
        
        if result['stackoverflow_links']:
            formatted += "Stack Overflow Results:\n"
            for idx, link in enumerate(result['stackoverflow_links'], 1):
                formatted += f"  {idx}. {link['title']}: {link['link']}\n"
            
            if result['stackoverflow_codes']:
                formatted += "\nCode Examples:\n"
                for idx, code in enumerate(result['stackoverflow_codes'], 1):
                    formatted += f"  Code {idx} (Language: {code['language']}):\n"
                    formatted += f"    {code['code'][:200]}...\n"
        
        if result['w3schools_links']:
            formatted += "\nW3Schools Tutorials:\n"
            for idx, link in enumerate(result['w3schools_links'], 1):
                formatted += f"  {idx}. {link['title']}: {link['link']}\n"
        
        return formatted.strip() or "No results found."