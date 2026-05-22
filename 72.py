n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ok = 0
for i in range(n):
    if a[i:] + a[:i] == b:
        ok = 1
if ok == 1:
    print('Да')
else:
    print('Нет')