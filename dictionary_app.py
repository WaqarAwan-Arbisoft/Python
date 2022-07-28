import json
from difflib import get_close_matches

dictionary = json.load(open("data.json"))


def findWord(wordToSearch):
    wordToSearch = wordToSearch.lower()
    if wordToSearch in dictionary:
        return dictionary[wordToSearch]
    elif len(get_close_matches(wordToSearch, dictionary.keys())) > 0:
        closestMatch = get_close_matches(wordToSearch, dictionary.keys())[0]
        askUser = input(f"Did you mean {closestMatch}. Press Y for yes: ")
        if askUser == 'y' or askUser == 'Y':
            return dictionary[closestMatch]
        else:
            return "Unable to process the input"
    else:
        return "No word found for your search."


inputWord = input("Enter the word you want to search: ")
print(findWord(inputWord))
