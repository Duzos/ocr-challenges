import json
from util import *

JSON_PATH = "json/averages.json"

def addNumberToList(list: list,num: int):
    list.append(num)
    return list

# Alternative to these is to import statistics but thats no fun :(
def getMeanOfList(list: list):
    total = 0

    for num in list:
        total = total + num

    return total / len(list)
    

def getMedianOfList(list: list):
    list.sort()
    n = len(list)
    if n % 2 == 1:
        return list[n // 2]
    else:
        i = n // 2
        return (list[i - 1] + list[i]) / 2

def getModeofList(list: list):
    list.sort()
    mode = 0
    count = {}

    for num in list:
        if num in count:
            amount = count.get(num)
            new = {num: amount+1}
            count.update(new)
        else:
            new = {num: 1}
            count.update(new)

    highest = 0
    for num in count.keys():
        if count.get(num) > highest:
            highest = count.get(num)
            mode = num

    return mode

def askAddNum():
    print("Number:")
    return int(input())

def printAverages(list: list):
    print("List: " + str(list))
    print("Mean: " + str(getMeanOfList(list=list)))
    print("Mode: " + str(getModeofList(list=list)))
    print("Median: " + str(getMedianOfList(list=list)))

def askChoice():
    VALID_CHOICES = ["add","print","clear","load","settings","quit"]

    pretty = choicesToPrettyString(VALID_CHOICES)
    print(pretty)
    choice = input().lower()

    if ((choice in VALID_CHOICES) == False):
        return print("Invalid choice, choose " + pretty)
    
    return choice

def changeName(name: str):
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    if (("settings" in data) == False):
        data["settings"] = {}

    data["settings"]["name"] = name

    with open(JSON_PATH,'w') as w:
        json.dump(data, w, indent=4) 


def changeSavesSetting():
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    print("Do you want to save your list on quit? (y/n)")
    choice = input().lower()

    if (("settings" in data) == False):
        data["settings"] = {}

    if (choice == "y"):
        data["settings"]["saves"] = True
    else:
        data["settings"]["saves"] = False

    with open(JSON_PATH,'w') as w:
        json.dump(data, w, indent=4) 

def changeNameSetting():
    print("What do you want to save the list as?")
    choice = input().lower()

    changeName(choice)

def openSettings():
    VALID_CHOICES = ["saves","name"]
    pretty = choicesToPrettyString(VALID_CHOICES)

    print("What do you want to edit " + pretty )
    choice = input().lower()

    if (choice not in VALID_CHOICES):
        return print("Invalid choice, please use " + pretty)
    
    if (choice == "saves"):
        changeSavesSetting()
    elif (choice == "name"):
        changeNameSetting()

def doesSave():
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    if (("settings" in data) == False):
        data["settings"] = {}
        with open(JSON_PATH,'w') as w:
            json.dump(data, w, indent=4)    
        print("Error with data, please run saves setting!")
        return False
        
    if ("saves" not in data["settings"]):
        data["settings"]["saves"] = False
        with open(JSON_PATH,'w') as w:
            json.dump(data, w, indent=4)    
        print("Error with data, please run saves setting!")
        return False
    
    return data["settings"]["saves"]

def getListName():
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    if (("settings" in data) == False):
        data["settings"] = {}
        with open(JSON_PATH,'w') as w:
            json.dump(data, w, indent=4)    
        print("Error with data, please run name setting!")
        return "ERROR"
    
    if ("name" not in data["settings"]):
        data["settings"]["name"] = "ERROR"
        with open(JSON_PATH,'w') as w:
            json.dump(data, w, indent=4)    
        print("Error with data, please run name setting!")
        return "ERROR"

    return data["settings"]["name"]

def save(list: list):
    name = getListName()
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    data[name] = list

    with open(JSON_PATH,'w') as w:
        json.dump(data, w, indent=4)

def load():
    with open(JSON_PATH,'r') as f:
        data = json.load(f)
    name = getListName()

    if (name in data):
        print("List found! Would you like to load it? (y/n)")
        choice = input().lower()

        if (choice == "y"):
            return data[name]
    
    return []

def loadPrevious(name: str):
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    if (name in data):
        changeName(name)
        return data[name]
    
    changeName("error")

    print("ERROR: List not found! Resetting..")
    
    return []

def main():
    list = load()

    while True:
        choice = askChoice()

        if (choice == "add"):
            addNumberToList(list,askAddNum())
            continue
        elif (choice == "print"): 
            if (len(list) == 0):
                print("Empty list, cancelling print.")
                continue

            printAverages(list=list)
            continue
        elif (choice == "settings"):
            openSettings()
            continue
        elif (choice == "load"):
            print("What list would you like to load?")
            name = input().lower()

            list = loadPrevious(name)
            continue
        elif (choice == "clear"):
            list = []
            continue
        elif (choice == "quit"):
            if (doesSave()):
                save(list)
            exit()
            return

        print(list) # Should be unreachable

main()