INF = float('inf')

def main():
    n = int(input())

    g = [[] for _ in range(n)]
    
    for _ in range(n-1):
        a, b = list(map(int, input().split()))
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    
    cost = [-1] * n 

    cost[0] = 0
    st = []
    opened_list = [0]

    for node in g[0]:
        st.append(node)
        cost[node] = 1
    
    while(len(st) != 0):
        open_node = st.pop()
        opened_list.append(open_node)
        for node in g[open_node]:
            if cost[node] == -1:
                st.append(node)
                cost[node] = cost[open_node] + 1

    s_node = cost.index(max(cost))

    cost = [-1] * n

    cost[s_node] = 0
    st = []
    opened_list = [s_node]

    for node in g[s_node]:
        st.append(node)
        cost[node] = 1
    
    while(len(st) != 0):
        open_node = st.pop()
        opened_list.append(open_node)
        for node in g[open_node]:
            if cost[node] == -1:
                st.append(node)
                cost[node] = cost[open_node] + 1
    
    print(max(cost) + 1)


if __name__ == '__main__':
    main()