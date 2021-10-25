from math import floor, ceil, log
from collections import deque
from copy import deepcopy, copy

INF = float('inf')

def main():
    a, k = list(map(int, input().split()))

    goal = 2 * 10**12

    if k == 0:
        print(goal - a)
        return

    n = ceil(log(goal + 1/k, k+1) - log(a + 1/k, k+1))
    print(n)

if __name__ == '__main__':
    main()