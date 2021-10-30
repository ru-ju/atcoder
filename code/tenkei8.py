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


def main():
    n = int(input())
    s = input()

    mod = 10 ** 9 + 7

    l = "atcoder"

    dp = [0] * 8

    for i in range(n):
        next = copy(dp)
        for j in range(len(l)):
            if s[i] == l[j]:
                if j == 0:
                    next[j] += 1
                    next[j] %= mod
                else:
                    next[j] += next[j-1]
                    next[j] %= mod
        dp = next
    
    print(dp[6])

            

        

if __name__ == '__main__':
    main()