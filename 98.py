n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            m = a[i+1:j]
            if len(m) == len(set(m)):
                c = 1
                break
    if c == 1:
        break
if c == 1:
    print('Да')
else:
    print('Нет')
