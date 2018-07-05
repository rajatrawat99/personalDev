import json

data = json.load(open("data.json"))

def secDef(word):
    word = word.lower()
    if word in data:
        print(data[word])
    else:
        print("Word doesnt exist in dictionary")
    decision = input("Do you want another word? (y/n): ")
    return decision

def defination(word):
    decision = secDef(word)
    while(decision !="n"):
        word1 = input("Enter the word for the defination: ")
        secDef(word)

word1 = input("Enter the word for the defination: ")
(defination(word1))
