INF = float("inf")

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))

    ans = [INF] * n

    min_t = t.index(min(t))

    for i in range(n):
        ans[(min_t + i) % n] = min(t[(min_t + i) % n], ans[(min_t + i) % n - 1] + s[(min_t + i) % n - 1])

    [print(ans[i]) for i in range(n)]

if __name__ == '__main__':
    main()