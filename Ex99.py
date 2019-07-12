nums = open('nums.txt', 'r')
f = iter(nums)
number = mx = -1

for i in range(1, 1001):
    n = next(f).split(',')    
    p = int(n[0])**int(n[1])
    if p > mx:
        mx = p; number = i
print(number, mx)
nums.close()
