import time

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

# Copied from an old project, ignore the weirdo comments
# some neat little computing animations, dunno why i added them but i like them and they look cool so yeah. if you want to add them anywhere yourself just call the function.

# text - the text to show
# sleep_time - how long per dot/line appearing
# dot_amount - the amount of dots til its done
# spin_amount - the amount of times to spin 

def compute_dots(text: str = 'Computing',sleep_time: str = 1,dot_amount: int = 5):
    for x in range (0,dot_amount):  
        b = f"{text}" + "." * x
        print (b, end="\r")
        time.sleep(sleep_time)

def compute_line(text: str = 'Computing',sleep_time: str = 1,spin_amount: int = 1):
    line_choices = ['|','/','-','\\']
    while spin_amount != 0:
        for x in range (0,4):  
            current_line = line_choices[x]
            b = f'{text} {current_line}'
            print (b, end="\r")
            time.sleep(sleep_time)
        spin_amount = spin_amount - 1

# Splitter
import re

class Splitter():
    def __init__(self, filepath: str):
        self.path = filepath

    def split(self, text: str):
        split_lines = re.split('(?<=[.!?]) +',text)
        lines = ""

        for line in split_lines:
            lines = lines + "\n" + line
        
        return lines
    
    def rewrite(self):
        file = open(self.path, "r")
        lines = self.split(file.read())
        
        file = open(self.path, "w")
        file.write(lines)