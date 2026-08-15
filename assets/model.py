class TrainerModel:
    def __init__(self, lang):
        self.data = []
        self.lang = lang
    
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
            pass
        else:
            # me must return data from the history
            pass