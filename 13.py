h = int(input())
m = int(input())
s = int(input())
angle = h * 30 + m * 0.5 + s * (0.5/60)
if 0 < h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
    if angle > 360:
        print(angle - 360)
    else:
        print(angle)