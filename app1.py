import json
from difflib import get_close_matches

data = json.load(open("app1.json"))

def means(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff = 0.8)) > 0:
        yn = input("Did you mean '%s' instead? Press Y for Yes or N for No: " % get_close_matches(word, data.keys(), cutoff = 0.8)[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys(), cutoff = 0.8)[0]]
        elif yn == "N" or yn == "n":
            return "Word not found. Please enter a valid word."
        else:
            return "Please enter a valid response."
    else:
        return "Word not found. Please enter a valid word."

user_input = input("Enter your word: ")
output = means(user_input)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)