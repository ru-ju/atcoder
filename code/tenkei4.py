INF = float('inf')

def main():
    h, w = list(map(int,input().split()))
    a = []
    row_sum = []
    col_sum = [0] * w

    for _ in range(h):
        inp = list(map(int, input().split()))
        a.append(inp)
        row_sum.append(sum(inp))
        for i in range(w):
            col_sum[i] += inp[i]
    
    b = []

    for i in range(h):
        row = []
        for j in range(w):
            row.append(row_sum[i] + col_sum[j] - a[i][j])
        b.append(row)

    [print(*b[i]) for i in range(h)]

if __name__ == '__main__':
    main()