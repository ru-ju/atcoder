n, l = list(map(int, input().split()))
k = int(input())
a = list(map(int, input().split()))

right = l // k + 1

left = 1

def check(th):
    c = 0
    pre = 0
    for i in range(n):
        if a[i] - pre >= th :
            c += 1
            pre = a[i]
        if c >= k:
            if l - a[i] >= th:
                return True
            return False
    return False

while((right - left) > 1):
    mid = (right + left) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print(left)