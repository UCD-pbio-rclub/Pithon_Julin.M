
f = open('../Chapter4/hangman_words.txt')

words = f.read()

words
words.splitlines()


# 06_03

words_file = '../Chapter4/hangman_words.txt'

try:
    f = open(words_file)
    line = f.readline()
    while line != '':
        print(line)
        if line == 'hummingbird\n':
            print(' there is a hummingbird in the file')
            break
        line = f.readline()
    f.close()
except IOError():
    print('Cannot find file: ' + words_file)

f = open('test.txt', 'w')

f.write('blah blah')

f.close()

# internet

import urllib.request

u = 'http://www.amazon.com/s/ref=nb_sb_noss?field-keywords=raspberry+pi'

f = urllib.request.urlopen(u)
contents = f.read()
contents
f.close()
