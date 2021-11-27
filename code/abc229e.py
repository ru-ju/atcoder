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

# funcがTrueになる最左端を見つける
# funcがTrueになるものが右側に配置されており、かつTrueになるものは一つは存在しなければならない
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


class UnionFind:
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        # 根の数
        self.n_root = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        self.root = [-1]*(n+1)
        # 木をくっつける時にアンバランスにならないように調整する
        self.rank = [0]*(n+1)

    # ノードxのrootノードを見つける
    def findRoot(self, x):
        if(self.root[x] < 0): # 根
            return x
        else:
            # ここで代入しておくことで、後の繰り返しを避ける
            self.root[x] = self.findRoot(self.root[x])
            return self.root[x]
    # 木の併合、入力は併合したい各ノード
    def unite(self, x, y):
        # 入力ノードのrootノードを見つける
        x = self.findRoot(x)
        y = self.findRoot(y)
        # すでに同じ木に属していた場合
        if x == y:
            return 
        # 違う木に属していた場合rankを見てくっつける方を決める
        if self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
            self.n_root -= 1

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            self.n_root -= 1
            # rnkが同じ（深さに差がない場合）は1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
    # xとyが同じグループに属するか判断
    def isSameGroup(self, x, y):
        return self.findRoot(x) == self.findRoot(y)

    # ノードxが属する木のサイズを返す
    def size_x(self, x):
        return -self.root[self.findRoot(x)]
    
    # 木の総数（グループ総数）を返す
    def count_tree(self):
        return self.n_root



def main():
    n, m = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]

    g = [[] for _ in range(n+1)]

    uf = UnionFind(n)

    ans = [0]

    for a, b in ab:
        g[a].append(b)
    
    for i in range(n,1,-1):
        for edge in g[i]:
            uf.unite(i, edge)
        ans.append(uf.count_tree()-(i-1))

    ans = ans[::-1]    

    [print(a) for a in ans]

if __name__ == '__main__':
    main()