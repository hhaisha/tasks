n = int(input())
m = 1
c = 1
l = n % 10

while n > 0:
    d = n % 10
    if d == l:
        c += 1
    else:
        c = 1
    if c > m:
        m = c
    l = d
    n //= 10
print(m)
