# Block of code for automatic path setup: it makes possible
# to execute the script from any location as long as the
# input file(s) are in the same folder as the script.
import os
abpath = os.path.abspath(__file__)
script_path = os.path.dirname(abpath)
os.chdir(script_path)

# Importing libraries: json is needed to read the definitions from
# the definitions' file, get_close_matches is for strings comparison.
import json
from difflib import get_close_matches

# Loading the definitions:
data = json.load(open("definitions.json"))

# The core function: it looks for the input word in all cases,
# if the word is not wound it proposes the most similar one.
def translate(word):
    w1 = word.lower()
    w2 = word.title()
    w3 = word.upper()
    if w1 in data:
        return data[word]
    elif w2 in data:
        return data[w2.title()]
    elif w3 in data:
        return data[w3.upper()]    
    else:
        sim_word = get_close_matches(word, data.keys())[0]
        ans = input(f"The word doesn't exist. Did you mean {sim_word}? Type Y or N: ")
        if ans.lower() == "y":
            return data[sim_word]
        else:
            return "The word you typed does not exist."

# While loop to keep the script running unless '/exit' is typed. 
while True:
    wordd = input("Please type a word. To exit, type '/exit': ")
    if wordd == "/exit":
        print("The program will close. Goodbye!")
        break
    else:    
        output = translate(wordd)
        if type(output) == list:
            for item in output:
                print (item)
        else:
            print(output)