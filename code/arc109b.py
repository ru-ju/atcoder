from math import floor, ceil
from collections import deque
from copy import deepcopy, copy
from heapq import heapify, heappop, heappush
from bisect import bisect_right, bisect_left
from functools import partial

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

def b_s_func(mini, maxi, func):
    l = mini
    r = maxi
    while(r - l > 1):
        mid = (l + r) // 2
        if func(mid):
            r = mid
        else:
            l = mid

    return l if func(l) else r

def func(n,p):
    return (n + 3) * n > 2 * p


def main():
    n = int(input())

    # c = [0,0]

    # while(sum(c) < n):
    #     c[0] += 1
    #     c[1] += c[0]
    
    # ans = n - (c[1] - c[0] + c[0] - 1) + c[1] - c[0]

    # print(ans)

    l = 1
    r = n

    r = b_s_func(l, r, partial(func, p=n))

    ans = n - r + 1

    print(ans)



if __name__ == '__main__':
    main()