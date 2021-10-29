from math import floor, ceil
from collections import deque
from copy import deepcopy, copy
from heapq import heapify, heappop, heappush
from bisect import bisect_left, bisect_right

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
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    a.sort()
    
    ans = []

    for i in range(q):
        bi = int(input())
        idx = bisect_left(a,bi)

        if idx == 0:
            ans.append(abs(a[idx] - bi))
        elif idx == n:
            ans.append(abs(a[idx-1] - bi))
        else:
            ans.append(min(abs(a[idx-1] - bi), abs(a[idx] - bi)))

    [print(an) for an in ans]

if __name__ == '__main__':
    main()