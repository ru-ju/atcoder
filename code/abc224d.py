from math import floor, ceil
from collections import deque
from copy import copy, deepcopy
INF = float('inf')

def main():
    m = int(input())
    g = [[] for _ in range(10)]
    for i in range(m):
        u, v = list(map(int, input().split()))
        g[u].append(v)
        g[v].append(u)

    p = ["0"] + list(input().split())

    if "".join(p) == "012345678":
        print(0)
        return

    for i in range(1, 10):
        if not (str(i) in p):
            p.append(str(i))


    opened = {int("".join(p[1:]))}

    d = deque()

    for node in g[int(p[-1])]:
        koma = p.index(str(node))
        l = copy(p)
        l[koma] = p[-1]
        l[-1] = p[koma]
        l[0] = str(int(p[0]) - 1)
        d.append(l)

    while(len(d) > 0):
        state = d.popleft()
        if int("".join(state[1:])) in opened:
            continue
        if "".join(state[1:]) == "123456789":
            print(-1 * int(state[0]))
            return
        opened.add(int("".join(state[1:])))
        for node in g[int(state[-1])]:
            koma = state.index(str(node))
            l = copy(state)
            l[koma] = state[-1]
            l[-1] = state[koma]
            l[0] = str(int(state[0]) - 1)
            if not(int("".join(l[1:])) in opened):
                d.append(l)

    print(-1)    


if __name__ == '__main__':
    main()