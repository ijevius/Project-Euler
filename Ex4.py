b = 100001

for i in range(999999, 100000, -1):
    if str(i)[:3] == str(i)[3:][::-1]:
        for m in range(100, 1000):
            n = i/m
            if n.is_integer():
                if len(str(int(n))) == 3 and i > b:
                    b = i
print(b)
