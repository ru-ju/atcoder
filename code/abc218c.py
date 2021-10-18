n = int(input())

s = [list(input()) for _ in range(n)]

t = [list(input()) for _ in range(n)]

def rot_90(mat):
    return list(zip(*mat[::-1]))


s_col = -1

s_c = 0
t_c = 0

for i in range(n):
    try:
        if s_col == -1:
            s_col = s[i].index("#")
            s_top = (i, s_col)
    except:
        c = 0

    s_c += s[i].count("#")
    t_c += t[i].count("#")

def check():
    for j in range(n):
        try:
            t_col = t[j].index("#")
            t_top = (j, t_col)
            break
        except:
            c = 0
    
    ofs = (s_top[0] - t_top[0], s_top[1] - t_top[1])

    for j in range(n):
        for k in range(n):
            if j + ofs[0] < n and j + ofs[0] >= 0 and k + ofs[1] < n and k + ofs[1] >= 0:
                if s[j + ofs[0]][k + ofs[1]] != t[j][k]:
                    return False
            else:
                if t[j][k] == "#":
                    return False
    
    return True
    

if t_c != s_c:
    print("No")
else:
    f = 0
    for i in range(4):
        if check():
            print("Yes")
            f = 1
            break
        t = rot_90(t)
                            
    if f == 0:
        print("No")
        