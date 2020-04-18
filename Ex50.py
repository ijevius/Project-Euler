def test_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True;
    else:
        for x in range(2, n):
            if n%x == 0:
                return False
        return True


total = 0
for i in range(2, 1000000):
    if test_prime(i):
        if test_prime(total+i):
            print(f"i={i}", total+i)
        total += i
        if total >= 1000000:
            print('^^^anwer^^^')
            break
