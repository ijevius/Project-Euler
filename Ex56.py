m = 1

for a in range(1, 101):
    for b in range(1, 101):
        s = int(sum(list(map(int, str(a**b)))))
        if s > m: m = s
print(m)
