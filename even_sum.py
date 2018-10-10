sum = 0
upper = int(input('Enter upper bound: '))
for num in range(upper):
    sum += num
print('Sum of numbers from 0 - {} = '.format(upper), sum)
