# importing assets
from assets.stackoverflow import StackOverFlow
from assets.geeksforgeeks import GeeksForGeeks

language = input("Select your coding language: ")
question = input("Enter your question: ")

# web scrapping
stackoverflow = StackOverFlow(question, language)
geeksforgeeks = GeeksForGeeks(question, language)

# show result
def ShowResult():
    print("AI Results :")
    print("="*20)
    print("1. Stackover flow :")
    try:
        for stackoverflowData in stackoverflow:
            print(stackoverflowData["title"])
    except:
        print("Not found.")
    print("="*20)
    print("2. Geeks For Geeks :")
    if geeksforgeeks[1]:
        for geeksforgeeksData in geeksforgeeks:
            print(geeksforgeeksData["title"])
    else:
        print("Not found.")

ShowResult()