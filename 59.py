n = list(map(int, input().split()))
mxn = 0
mxi = 0
for i in range(len(n)):
    if n[i] > mxn:
        mxn = n[i]
        mxi = i
print(mxi)