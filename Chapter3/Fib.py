# print the firt 100 numbers in the Fibonacci series

a,b = 0,1
for i in range(1,11):
    print(a)
    c = a + b
    a = b
    b = c
    
