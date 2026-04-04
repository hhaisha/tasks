x1 = float(input())
y1 = float(input())
w1 = float(input())
h1 = float(input())
x2 = float(input())
y2 = float(input())
w2 = float(input())
h2 = float(input())

a = (x1 >= x2 and x1 + w1 <= x2 + w2 and y1 >= y2 and y1 + h1 <= y2 + h2)
a2 = (x2 >= x1 and x2 + w2 <= x1 + w1 and y2 >= y1 and y2 + h2 <= y1 + h1)
b = a or a2
no_intersection = (x1 + w1 <= x2 or x2 + w2 <= x1 or y1 + h1 <= y2 or y2 + h2 <= y1)
c = not no_intersection

print("а)", a)
print("б)", b)
print("в)", c)