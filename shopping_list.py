import json
from util import *

JSON_PATH = "json/shopping_list.json"

def addItemToList(name: str, shop: str, priority: int, bought: bool, ideal_price: float,quantity: int):
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    list = {
        "priority": priority,
        "shop": shop,
        "bought": bought,
        "ideal_price": ideal_price,
        "quantity": quantity
    }

    data[name] = list

    with open(JSON_PATH,'w') as w:
        json.dump(data, w, indent=4)

def readItemsData(name: str):
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    if (name not in data):
        print("No data found for " + name)
        return {}
    
    return data[name]

def printShoppingList():
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    for item in data:
        printItem(item)

def printItem(item: str):
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    if (item not in data):
        print(item + " not found in data.")
        return

    print(item + ": ")
    print("     Shop: " + data[item]["shop"])
    print("     Amount: " + str(data[item]["quantity"]))
    print("     Ideal Price: " + str(data[item]["ideal_price"]))
    print("     Priority: " + str(data[item]["priority"]))
    print("     Bought: " + str(data[item]["bought"]))

def getUserInputForNewItemAndAdd():
    name = input("Name: ")
    shop = input("Shop: ")
    quantity = int(input("Amount: "))
    ideal_price = float(input("Ideal Price: "))
    priority = int(input("Priority: "))
    bought = convertYNtoBoolean(input("Bought: "))
    
    addItemToList(name,shop,priority,bought,ideal_price,quantity)

    print("Successfully added: " + name)

def removeItem(item: str):
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    if (item not in data):
        return # No problem as its not there 
    
    data.pop(item)

    with open(JSON_PATH,'w') as w:
        json.dump(data, w, indent=4)


def updateItem(item: str):
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    if (item not in data):
        print(item + " not found in data.")
        return

    VALID_CHOICES = [d for d in data[item]]
    s = choicesToPrettyString(VALID_CHOICES)

    print(s)
    choice = input().lower()
    if (choice not in VALID_CHOICES):
        print("Invalid choice, choose " + s)

    new_val = input("New value: ")

    # This works for now
    if (choice == "bought"):
        new_val = convertYNtoBoolean(new_val)
    elif (choice == "priority" or choice == "quantity"):
        new_val = int(new_val)
    elif (choice == "ideal_price"):
        new_val = float(new_val)

    data[item][choice] = new_val
    with open(JSON_PATH,'w') as w:
        json.dump(data, w, indent=4)

def getEstimatedItemCost(item: str):
    with open(JSON_PATH,'r') as f:
        data = json.load(f)

    if (item not in data):
        print(item + " not found in data.")
        return
    
    amount = data[item]["quantity"]
    price = data[item]["ideal_price"]

    return amount * price


def askWhatNextAndRun():
    VALID_CHOICES = ["add","remove","list","check","update","cost"]
    s = choicesToPrettyString(VALID_CHOICES)

    print(s)
    choice = input().lower()

    if (choice not in VALID_CHOICES):
        print("Invalid choice, choose " + s)

    if (choice == "add"):
        getUserInputForNewItemAndAdd()
        return
    elif (choice == "remove"):
        item = input("Item: ") # These repeated input() stuff could just be its own method
        removeItem(item)
        return
    elif (choice == "list"):
        printShoppingList()
        return
    elif (choice == "check"):
        item = input("Item: ")
        printItem(item)
        return
    elif (choice == "update"):
        item = input("Item: ")
        updateItem(item)
        return        
    elif (choice == "cost"):
        item = input("Item: ")
        print("The estimated price for " + item + " is " + str(getEstimatedItemCost(item)))
        return



def main():
    while True:
        askWhatNextAndRun()
        

if __name__ == "__main__":
    main()