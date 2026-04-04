n = int(input())
l = n % 10
n //= 10
c = 0
while n > 0:
    d = n % 10
    if d >= l:
        c = 1
    l = d
    n //= 10
if c == 0:
    print('Да')
else:
    print('Нет')
