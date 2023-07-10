from util import *
import json
import random

JSON_PATH = "json/quiz_maker.json"

def getNextQuestionMakerNumber():
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    if "questions" not in data:
        data["questions"] = {}
        with open(JSON_PATH,'w') as w:
            json.dump(data, w, indent=4)
        return 0
    
    c = 0

    for question in data["questions"]:
        if (str(c) in data["questions"]):
            c = c + 1
            continue
        else:
            break
    
    return c

def addQuestion(question: str, answer: str):
    num = getNextQuestionMakerNumber()

    with open(JSON_PATH,'r') as f:
        data = json.load(f)
    
    list = {
        "question": question,
        "answer": answer
    }

    if "questions" not in data:
        data["questions"] = {}
        with open(JSON_PATH,'w') as w:
            json.dump(data, w, indent=4)
        print("Error, rerun this command!")
        return


    data["questions"][num] = list

    with open(JSON_PATH,'w') as w:
        json.dump(data, w, indent=4)

def getInputsForNewQuestion():
    q = input("Question: ")
    a = input("Answer: ")
    addQuestion(q,a)

def printQuestion(id: int):
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    if "questions" not in data:
        data["questions"] = {}
        with open(JSON_PATH,'w') as w:
            json.dump(data, w, indent=4)
        print("Error, rerun this command!")
        return


    if (id not in data["questions"]):
        print(id + " not found in data.")
        return

    print(data["questions"][id]["question"] + " - " + data["questions"][id]["answer"])

def listQuiz():
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    if "questions" not in data:
        data["questions"] = {}
        with open(JSON_PATH,'w') as w:
            json.dump(data, w, indent=4)
        print("Error, rerun this command!")
        return

    for question in data["questions"]:
        printQuestion(question)

def quizAsList(): # not to be confused with above method
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    if "questions" not in data:
        data["questions"] = {}
        with open(JSON_PATH,'w') as w:
            json.dump(data, w, indent=4)
        print("Error, questions not in data")
        return

    return [q for q in data["questions"]]

def clearQuiz():
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    data["questions"] = {}

    with open(JSON_PATH,'w') as w:
        json.dump(data, w, indent=4)

def makeQuiz():
    VALID_CHOICES = ["add","list","clear","done"]
    s = choicesToPrettyString(VALID_CHOICES)
    choice = ""

    while choice != "done":
        print(s)
        choice = input().lower()
        if (choice not in VALID_CHOICES):
            print("Invalid choice, pick " + s)
            continue

        if (choice == "add"):
            getInputsForNewQuestion()
            continue
        elif (choice == "list"):
            listQuiz()
            continue
        elif (choice == "clear"):
            clearQuiz()
            continue

    print("Quiz made! Rerun this program in play mode.")

# Playing the quiz

def askQuestion(id: int):
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    if "questions" not in data:
        data["questions"] = {}
        with open(JSON_PATH,'w') as w:
            json.dump(data, w, indent=4)
        print("Error, questions not in data")
        return


    if (id not in data["questions"]):
        print(id + " not found in data.")
        return

    question = data["questions"][id]["question"]
    answer = data["questions"][id]["answer"]

    print(question)
    player = input().lower()

    if (player == answer.lower()):
        print("Correct!")
        return True
    
    print("Wrong, the correct answer is \n" + answer)
    return False

def playQuiz():
    score = 0

    for id in quizAsList():
        result = askQuestion(id)

        if (result):
            score = score + 1

    print("Congratulations, your score is " + str(score))
    input()

def main():
    print(choicesToPrettyString(["play","create"]))
    choice = input().lower()
    while True:
        if (choice not in ["play","create"]):
            return print("Invalid choice, use" + choicesToPrettyString(["play","create"]))
        
        if (choice == "create"):
            print("Starting Quiz Maker!")
            makeQuiz()
            return
        elif (choice == "play"):
            print("Starting the Quiz!")
            playQuiz()
            return
        
if __name__ == "__main__":
    main()
