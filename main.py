from assets.model import TrainerModel

trainer_model = TrainerModel()

while True:
    Input = input("Enter your question: ")
    result = trainer_model.process(Input)
    print(result)