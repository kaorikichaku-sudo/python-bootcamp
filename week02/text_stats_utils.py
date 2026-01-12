import re


# funcions
def count_characters(user_input):
    counter = 0
    for char in user_input:
        if char != " ":
            counter += 1
    return counter


def count_words(user_input):
    counter = 0
    text = user_input.split()
    for word in text:
        counter += 1
    return counter


def count_sentences(user_input):
    if user_input.strip() == "":
        return 0
    
    text = re.split(r"[?!.]", user_input)
    sentences = [w.strip() for w in text if w.strip() != ""]
    return len(sentences)
 

def count_vowel(user_input):
    counter = 0
    for char in user_input.lower():
        if char in "aeiou":
            counter += 1
    return counter

def vowel_percentage(character, vowels):
    try:
        percentage = vowels * 100 / character
        return percentage
    except ZeroDivisionError:
        return 0
    