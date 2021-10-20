n = int(input())

for i in range(2 ** n):
    c = 0
    b = format(i, "0" + str(n) + "b")
    arr = []
    for j in range(n):
        if c < 0 :
            break
        if b[j] == "0":
            c += 1
            arr.append("(")
        else:
            c -= 1
            arr.append(")")
    else:
        if c == 0:
            print("".join(arr))

    