n = int(input())
a = list(map(int, input().split()))
sm = 0
c = 0
for i in range(n):
    sm = 0
    for j in range(i, n):
        sm += a[j]
        if j - i + 1 >= 2 and sm == 0:
            print('Да')
            break
print('Нет')