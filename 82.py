n = int(input())
a = list(map(int, input().split()))
sm = sum(a)
if sm % 3 != 0:
    print('Нет')
else:
    pt = sm // 3
    s = 0
    c = 0
    for i in range(n - 1):
        s += a[i]
        if sm == pt:
            c += 1
            s = 0
    if c >= 2:
        print('Да')
    else:
        print('Нет')
