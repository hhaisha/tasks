n = int(input())
s = 0
while n > 0:
    m = n % 10
    if m > s:
        s = m
    n //= 10
print(s)