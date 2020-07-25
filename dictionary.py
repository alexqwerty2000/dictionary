import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data: 
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
        return "Do you mean %s instead?" % get_close_matches(w, data.keys())[0]
    else:
        return "Word doesn't exist. Please double check it"

word = input("Enter the word: ")

print(translate(word))