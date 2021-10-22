from math import ceil

INF = float('inf')

def main():
    q, h, s, d = list(map(int, input().split()))
    n = int(input())

    q = q * 8
    h = h * 4
    s = s * 2
    d = d

    min_val = min([q, h ,s ,d])

    if n % 2 == 0:
        print((n//2) * min_val)
    else:
        min_val2 = min([q//2, h//2, s//2])
        print(((n-1)//2) * min_val + min_val2)
        


if __name__ == '__main__':
    main()