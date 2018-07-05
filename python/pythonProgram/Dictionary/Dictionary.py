import json

data = json.load(open("data.json"))

def defination(word):
    word = word.lower()
    if word in data:
        print(data[word])
    else:
        print("Word doesnt exist in dictionary")
    decision = input("Do you want another word? (y/n): ")
    while(decision !="n"):
        word1 = input("Enter the word for the defination: ")
        word1 = word1.lower()
        if word1 in data:
            print(data[word1])
        else:
            print("Word doesnt exist in dictionary")
        decision = input("Do you want another word? (y/n): ")

word1 = input("Enter the word for the defination: ")
(defination(word1))
