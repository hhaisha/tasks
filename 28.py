n = int(input())
for i in range(n):
    a = int(input())
    b = int(input())
    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print('Равны')