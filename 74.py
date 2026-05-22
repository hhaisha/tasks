n = int(input())
a = list(map(int, input().split()))
mx = 0
for i in a:
    c = a.count(i)
    if c > mx:
        mx = c
if mx <= (n + 1)//2:
    print('Да')
else:
    print('Нет')