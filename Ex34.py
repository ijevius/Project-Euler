import math

n = 500000000
sum = 0

for i in range(3, n+1):
    d_sum = 0
    for digit in str(i):
        d_sum += math.factorial(int(digit))
    if d_sum == i:
        sum += i
        print(i)

print(sum)
