def pig_latin(sentence):
    # Write your solution here!
    new_sentence = sentence.split()
    new_words = []

    for word in new_sentence:
        new_word = pig_latin_word(word)
        new_words.append(new_word)

    return " ".join(new_words)

def pig_latin_word(word):
    if not word:
        return ""

    first_letter = word[0]
    if first_letter in ['a', 'e', 'i', 'o', 'u']:
        return word

    new_word = word[1:] + first_letter + 'ay'

    return new_word


# Test cases
assert pig_latin("something") == "omethingsay"
assert pig_latin("awesome") == "awesome"
assert pig_latin("latin is a hard language") == "atinlay is a ardhay anguagelay"
assert pig_latin("y") == "yay"
assert pig_latin("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")