from math import floor, ceil
from collections import deque
from copy import deepcopy, copy

INF = float('inf')

def dot(a,b):
    return [[sum([a[i][k] * b[k][j] for k in range(len(b))]) for j in range(len(b[0]))] for i in range(len(a))]

def dot_mod(a,b,mod):
    return [[sum([(a[i][k] * b[k][j]) % mod for k in range(len(b))]) % mod for j in range(len(b[0]))] for i in range(len(a))]

def pow_mat(a, n):
    ans = [[0] * len(a) for _ in range(len(a))]
    for i in range(len(a)):
        ans[i][i] = 1

    while(n):
        if n % 2:
            ans = dot(a, ans)
        a = dot(a,a)
        n >>= 1
    return ans

def pow_mat_mod(a, n, mod):
    ans = [[0] * len(a) for _ in range(len(a))]
    for i in range(len(a)):
        ans[i][i] = 1

    while(n):
        if n % 2:
            ans = dot_mod(a, ans, mod)
        a = dot_mod(a,a,mod)
        n >>= 1
    return ans

def main():
    s = input()

    c = "WBWBWWBWBWBW"

    code = ["Do", "Re", "Mi", "Fa", "So", "La", "Si"]

    for i in range(7):
        if s[:12] == c:
            print(code[i])
            break
        if c[:2] == "WB":
            c = c[2:] + c[:2]
        else:
            c = c[1:] + c[:1]

if __name__ == '__main__':
    main()