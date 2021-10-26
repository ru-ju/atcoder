from math import floor, ceil
from collections import deque
from copy import copy, deepcopy

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

# 小課題２まで
def main():
    n, b, k = list(map(int, input().split()))
    c = list(map(int, input().split()))

    mod = 10**9 + 7

    t = [[0] * b for _ in range(b)]

    for i in range(b):
        for ck in c:
            t[i][(10*i + ck) % b] += 1

    dp = [[0] for _ in range(b)]

    dp[0][0] = 1

    print(dot_mod(pow_mat_mod(t,n,mod), dp, mod)[0][0])

# 小課題３
def main():
    n, b, k = list(map(int, input().split()))
    c = list(map(int, input().split()))

    mod = 10**9 + 7

    dp = [0] * b

    ans = [0] * b

    ans[0] = 1

    for ck in c:
        dp[ck % b] += 1

    pow10mod = 10 % b

    while n:
        next_ans = [0] * b
        next_dp = [0] * b
        for i in range(b):
            for j in range(b):
                next_dp[(pow10mod * i + j) % b] += dp[i] * dp[j]
                next_dp[(pow10mod * i + j) % b] %= mod
                if n % 2:
                    next_ans[(pow10mod * i + j) % b] += ans[i] * dp[j]
                    next_ans[(pow10mod * i + j) % b] %= mod
        if n % 2:
            ans = next_ans
        dp = next_dp
        n >>= 1
        pow10mod = pow10mod**2 % b

    print(ans[0])

         

if __name__ == '__main__':
    main()