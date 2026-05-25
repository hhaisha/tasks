n = int(input())
a = list(map(int, input().split()))
mx = max(a)
s = []
for i in range(n):
    if a[i] == mx:
        s.append(i)
fst = s[0]
lst = s[-1]
st = set()
for i in range(fst + 1, lst):
    st.add(a[i])
print(len(st))

