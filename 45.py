n = int(input())
r = n
mn = 10
while n > 0:
    d = n % 10
    t = r
    c = 0
    while t > 0:
        if t % 10 == d:
            c += 1
        t //= 10
    if c == 1 and d < mn:
        mn = d
    n //= 10
if mn == 10:
    print('Нет')
else:
    print(mn)