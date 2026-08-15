import requests

class Stackoverflow:
    def search(self, Input, max_results=10, sort="relevance"):
        url = f"https://api.stackexchange.com/2.3/search/advanced"
        params = {
            'order': 'desc',
            'sort': sort,
            'q': Input,
            'site': 'stackoverflow',
            'pagesize': min(max_results, 100),
        }
        
        try:
            req = requests.get(url, params=params, timeout=10)
            req.raise_for_status()
            
            data = req.json()
            
            if data.get('error'):
                print(f"API Error: {data['error']['message']}")
                return None
            
            print(f"Quota remaining: {data.get('quota_remaining', 'Unknown')}")
            
            if data.get('items'):
                return data['items']
            else:
                print("No results found")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
        except ValueError as e:
            print(f"Invalid JSON response: {e}")
            return None

class W3School:
    def search(self, Input):
        pass

class TrainerModel:
    def __init__(self):
        self.data = []
        self.stackoverflow = Stackoverflow()
    
    def validInput(self, Input: str):
        if Input == "": return False
        elif Input == " ": return False
        elif Input.replace(" ", "") == "": return False
        return True

    def train(self, data):
        if not data in self.data:
            self.data.append(data)

    def find(self, value):
        if not value in self.data:
            return False
        return True

    def process(self, Input: str):
        isValidInput = self.validInput(Input)
        if not isValidInput:
            return "Please enter a valid input."
        find = self.find(Input)
        if not find:
            # we must train ai the new data
            stackoverflow_results = self.stackoverflow.search(Input)
            result = ""
            for data in stackoverflow_results:
                result += data["link"]+"\n"

            return result
        else:
            # me must return data from the history
            pass