import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data: 
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys()))>0:
        yn = input("Do you mean %s instead? Enter Y if Yes, or N if No: " % get_close_matches(w, data.keys())[0])
        if yn.lower() == 'y':
            return  data[get_close_matches(w, data.keys())[0]]
        elif yn.lower() == 'n':
            return "Word doesn't exist. Please double check it."
        else:
            return "We don't understand your enter."
    else:
        return "Word doesn't exist. Please double check it."

word = input("Enter the word: ")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)