n = int(input())

st = [".".join(input().split()) for _ in range(n)]

st.sort()

for i in range(n-1):
    if st[i] == st[i+1]:
        print("Yes")
        break
else:
    print("No")    
