def choicesToPrettyString(list: list):
    message = "("
    for choice in list:
        message = message + " | " + choice 
    message = message + " | )"
    return message

def convertYNtoBoolean(input: str):
    input = input.lower()

    if (input == "y"):
        return True
    elif (input == "n"):
        return False
    
    print("Invalid Y/N input, returning False")
    return False