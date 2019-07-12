import sys
import time

b = 100001
big_m = 0
big_i = 0
s = 0

z = time.time()

for i in range(999999, 100000, -1):
    if str(i)[:3] == str(i)[3:][::-1]:
        for m in range(100, 1000):
            if i < big_i and m < big_m:
                print(b);
                x = time.time();
                print("%.20f" % float(x-z));
                print(f's = {s}');
                sys.exit();
            n = i/m
            s += 1
            if n.is_integer():
                if len(str(int(n))) == 3 and i > b:
                    b = i
                    big_m = m; big_i = i;
print(b)
x = time.time()
print("%.20f" % x-z)
print(f's = {s}')
