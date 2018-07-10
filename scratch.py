word = 'test'

word

len(word)

word.len

len(word) == len(word)


def test(word1, word2):
    if len(word1) == len(word2):
        print('equal length')

test('one','two')        
