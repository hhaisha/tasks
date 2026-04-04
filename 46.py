n = int(input())
for i in range(10):
    c = 0
    t = n
    while t > 0:
        if t % 10 == i:
            c += 1
        t //= 10
    print(i, c)