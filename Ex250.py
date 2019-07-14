import itertools
import numpy

nums = list()
subnums = list()
s = 0

for i in range(1, 250251):
    nums.append(numpy.power(i, i))

for i in range(2, len(nums)-1):
    subnums = set().union(subnums, list(itertools.combinations(nums, i)))

for t in subnums:
    if numpy.sum(t) % 250 == 0:
        s+=1

print(s[-16:])
