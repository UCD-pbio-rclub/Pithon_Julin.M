# Demo built-in
# this is to demo use of a builtin module

import statistics
import random

print 'Demo of the statistics module'

print 'Will generate a set of random numbers and then compute descriptive statistics'

numbers = []

size = 20

while len(numbers) < size:
    numbers.append(random.gauss(mu=10, sigma=4))

print('The numbers are:', numbers)

print('The mean is:', round(statistics.mean(numbers),3))

print('The variance is:', round(statistics.variance(numbers),3))
