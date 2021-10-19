xy = float(input())

x = int(xy)

y = (xy - x) * 10

if y <= 2:
    print(str(x)+"-")
elif y >= 7:
    print(str(x)+ "+")
else:
    print(str(x))