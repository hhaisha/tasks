x1, y1 = map(float, input("A: ").split())
x2, y2 = map(float, input("B: ").split())
x3, y3 = map(float, input("C: ").split())
x4, y4 = map(float, input("D: ").split())

S1 = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2
S2 = abs(x1*(y3 - y4) + x3*(y4 - y1) + x4*(y1 - y3)) / 2
S = S1 + S2

print("Площадь четырёхугольника:", S)