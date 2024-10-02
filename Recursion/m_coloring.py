def solve(node, color, m, N, graph):
    if node == N:
        return True
    
    for i in range(1, m+1):
        if isSafe(node, color, graph, N, i):
            color[node] = i
            if solve(node+1, color, m, N, graph):
                return True
            color[node] = 0
    
    return False
def isSafe(node, color, graph, n, col):
    for k in range(n):
        if k != node and graph[k][node] == 1 and color[k] == col: # 1st condn whther we are considering the same node with itself, 2nd condn need to be adjacent, 3rd condition whtether adjacent nodes contain the color that I want to provide. color = [1, 2, 0, 0]  # Node 0 is colored 1, Node 1 is colored 2, Node 2 and 3 are not yet colored
            return False
    return True
def graphColoring(graph, m, N):
    color = [0]*N
    if solve(0, color, m, N, graph):
        return True
    return False


if __name__ == "__main__":
    N =4
    m=3
    graph = [[0 for i in range(101)] for j in range(101)]

    graph[0][1] = 1
    graph[1][0] = 1
    graph[1][2] = 1
    graph[2][1]=1
    graph[2][3] = 1
    graph[3][2] = 1
    graph[3][0] = 1
    graph[0][3] = 1
    graph[0][2] = 1
    graph[2][0] = 1

    print(1 if graphColoring(graph, m, N) else 0)