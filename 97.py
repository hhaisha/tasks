n = int(input())
a = list(map(int, input().split()))
mx = max(a)
if a.count(mx) >= 2:
    print(mx)
else:
    s = sorted(set(a))
    if len(s) == 1:
        print(s[0])
    else:
        print(s[-2], s[-1])
        