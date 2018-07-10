# reverse sentence

sentence = input("enter a sentence to reverse: ")

punctuation = ''

if sentence[-1].isalpha() is False:
    punctuation = sentence[-1]
    sentence = sentence[:-1]

words = sentence.split()

words.reverse() # why don't I need to assign this to something?

words[0] = words[0].capitalize()

if len(punctuation) == 1:
    words[-1] = words[-1] + punctuation

print(' '.join(words))
