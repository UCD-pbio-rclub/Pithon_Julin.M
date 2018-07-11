# test for palindrome

text = input("enter a word and I will test for a palindrome: ")

result = "Palindrome!"

for i in range(1, int(len(text)/2) + 1):
    if text[i-1] != text[-i]:
        result = "Not a palindrome"
        break

print(result)

