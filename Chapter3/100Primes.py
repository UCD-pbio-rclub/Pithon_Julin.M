# 100 primes

prime_total = 0

current_test = 1

div_by = 0

while (prime_total < 100):
    start = min(current_test, 2)  # necessary so that we get "1"
    for i in range(start, current_test+1):
        div_by = i
        if (current_test % i == 0):  # current_test divisible by i
            break
    if (current_test == div_by):    # this means we did not find current test
                                    # to be divisible by any lower numbers
        print(current_test)
        prime_total = prime_total + 1
    current_test = current_test + 1
