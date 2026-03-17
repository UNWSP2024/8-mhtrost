#Micah Trost
#March 17, 2026
#Word Separator
def word_separator(sentence):
    new_sentence = sentence[0]

    for char in sentence[1:]:
        if char.isupper():
            new_sentence += " " + char.lower()
        else:
            new_sentence += char

    return new_sentence.strip()

if __name__=="__main__":
    sentence = input("Enter a sentence where the first letter of each word is capitalized and there are no spaces inbetween the words: ")
    new_sentence = word_separator(sentence)
    print(new_sentence)
