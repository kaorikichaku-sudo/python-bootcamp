from text_stats_utils import (
    count_characters, 
    count_words, 
    count_sentences, 
    count_vowel, 
    vowel_percentage
)

# Program name
print(" TEXT STATISTIK\n\n")

# User instructions
print(" Enter below your sentence or 'exit'.\n\n")

# Program logic
while True:

    # User query
    user_input = input(" Sentence or 'exit': ")

    # Check and output
    if user_input.lower() == "exit":
        break

    else:
        character = count_characters(user_input)
        words = count_words(user_input)
        sentences = count_sentences(user_input)
        vowels = count_vowel(user_input)
        percentge_vowels = vowel_percentage(character, vowels)

        print(
            f"\n\n"
            f" Characters: {character}\n"
            f" Words: {words}\n"
            f" Sentence: {sentences}\n"
            f" Vowels: {vowels}\n" 
            f" Vowel-percentage: {percentge_vowels:.1f}%\n\n"
        )

