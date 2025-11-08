
# Define Funktions
def word_count(words):
    words = words.split()
    return len(words)

def vowel_count(words):
    count = 0
    for char in words.lower():
        if char in "aeiou":
            count += 1
    return count