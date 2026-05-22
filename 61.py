n = int(input())
a = list(map(int, input().split()))
def pal(l, r):
    while l < r:
        if a[l] != a[r]:
            return False
        l += 1
        r -= 1
    return True
i = 0
j = n - 1
while i < j:
    if a[i] == a[j]:
        i += 1
        j -= 1
    else:
        if pal(i + 1, j) or pal(i, j - 1):
            print("Да")
        else:
            print("Нет")
        break
else:
    print("Да")