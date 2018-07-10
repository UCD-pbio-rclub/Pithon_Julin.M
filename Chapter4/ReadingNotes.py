#  Chapter 4 reading notes

book_name = 'Programming Raspberry Pi'

book_name

print(book_name)

len(book_name)

book_name[1]

book_name[0:11]

book_name[12:]

book_name + ' by Simon Monk'

numbers = [123, 34, 55, 321, 9]  # a 1D array

len(numbers)

numbers[0]

numbers[1:3]

numbers[0] = 1
numbers

numbers.sort()

numbers.pop()

numbers

numbers.pop(1)

numbers.insert(1, 66)

big_list = [123, 'hello', ['inner list', 2, True]]
big_list

list = [1, 'one', 2, True]
for item in list:
    print(item)

# make a function
def make_polite(sentence):
    polite_sentence = sentence + ' please'
    return polite_sentence


print(make_polite('Pass the salt'))

# dictionaries

eggs_per_week = {'penny': 7, 'amy': 6, 'bernadette': 0}

eggs_per_week

eggs_per_week['amy']

# tuple.  like a list but immutable

tuple = 1, 2, 3
tuple
tuple[0]

a, b, c = 1, 2, 3

