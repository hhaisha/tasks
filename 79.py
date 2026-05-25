n = int(input())
a = list(map(int, input().split()))
c = 0
sm = 0
for i in a:
    sm += i
    if (sm - i) == i:
        c = 1
        break
if c == 1:
    print('Да')
else:
    print('Нет')
