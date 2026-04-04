a = int(input())
b = int(input())
while b != 0:
    t = b
    b = a % b
    a = t
print(a)
