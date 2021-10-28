from math import floor, ceil
from collections import deque
from copy import deepcopy, copy
from heapq import heapify, heappop, heappush

INF = float('inf')

# def dot(a,b):
#     return [[sum([a[i][k] * b[k][j] for k in range(len(b))]) for j in range(len(b[0]))] for i in range(len(a))]

# def dot_mod(a,b,mod):
#     return [[sum([(a[i][k] * b[k][j]) % mod for k in range(len(b))]) % mod for j in range(len(b[0]))] for i in range(len(a))]

# def pow_mat(a, n):
#     ans = [[0] * len(a) for _ in range(len(a))]
#     for i in range(len(a)):
#         ans[i][i] = 1

#     while(n):
#         if n % 2:
#             ans = dot(a, ans)
#         a = dot(a,a)
#         n >>= 1
#     return ans

# def pow_mat_mod(a, n, mod):
#     ans = [[0] * len(a) for _ in range(len(a))]
#     for i in range(len(a)):
#         ans[i][i] = 1

#     while(n):
#         if n % 2:
#             ans = dot_mod(a, ans, mod)
#         a = dot_mod(a,a,mod)
#         n >>= 1
#     return ans

def main():
    n, k = list(map(int, input().split()))
    s = input()

    base = ord("a")

    ans = ""

    table = []

    t = [-1] * 26

    for i in range(n-1,-1,-1):
        t[ord(s[i]) - base] = i
        table.append(copy(t))

    table = table[::-1]

    idx = 0
    while len(ans) < k:
        for i in range(26):
            if table[idx][i] < n - (k - len(ans)) + 1 and table[idx][i] >= 0:
                idx = table[idx][i] + 1
                ans += chr(base + i)
                break
    
    print(ans)

if __name__ == '__main__':
    main()