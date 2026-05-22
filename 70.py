n = int(input())
a = list(map(int, input().split()))
sm = sum(a)
if sm % 2 != 0:
    print('Нет')
else:
    hf = sm // 2
    sm = 0
    for i in a:
        sm += i
        if sm == hf:
            print('Да')
            break
    else:
        print('Нет')