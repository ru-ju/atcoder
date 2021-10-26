from math import floor, ceil
from collections import deque
from copy import deepcopy, copy

INF = float('inf')

def main():
    n, m = list(map(int, input().split()))
    disk = [int(input()) for _ in range(m)]

    l = list(range(n+1))

    now = 0
    for d in disk:
        l[now], l[d], now = l[d], 0, d
    
    idx = list(range(n+1))

    l2 = sorted(list(zip(l, idx)))

    [print(ele[1]) for ele in l2[1:]]

if __name__ == '__main__':
    main()