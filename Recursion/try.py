def isSafe(node, color, m, N, col, graph):
    for k in range(N):
        if k!= node and graph[k][node] == 1 and color[k] == col:
            return False
    return True

def graphColoring(node, graph, m, N):
    color = [0]*N

    if node == N:
        return True
    for i in range(1, m+1):
        if isSafe(node, color, m, N, i, graph):
            color[node] = i
            if graphColoring(node+1, graph, m, N):
                return True
            color[node] = 0
    return False

if __name__ == '__main__':
    N = 4
    m = 3


    graph = [[0 for i in range(101)] for j in range(101)]


    # Edges are (0, 1), (1, 2), (2, 3), (3, 0), (0, 2)
    graph[0][1] = 1
    graph[1][0] = 1
    graph[1][2] = 1
    graph[2][1] = 1
    graph[2][3] = 1
    graph[3][2] = 1
    graph[3][0] = 1
    graph[0][3] = 1
    graph[0][2] = 1
    graph[2][0] = 1


    print(1 if graphColoring(0, graph, m, N) else 0)