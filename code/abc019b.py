from math import floor, ceil
from collections import deque
from copy import deepcopy, copy
from heapq import heapify, heappop, heappush

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

    ans = ""

    c = 0

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            c += 1
        else:
            ans += s[i] + str(c+1)
            c = 0
    else:
        if c == 0:
            ans += s[-1] + "1"
        else:
            ans += s[-1] + str(c+1)

    print(ans)
        

if __name__ == '__main__':
    main()