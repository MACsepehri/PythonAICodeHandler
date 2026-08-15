from assets.model import TrainerModel

lang = input("Enter your language: ")
trainer_model = TrainerModel(lang)

while True:
    Input = input("Enter your question: ")
    trainer_model.process(Input)