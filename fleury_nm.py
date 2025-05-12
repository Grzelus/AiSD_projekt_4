def count_components(Graph,v):
    n = len(Graph)
    visited = [False] * n

    def dfs_count(v):
        visited[v] = True
        count = 1
        for u in range(n):
            if Graph[v][u] and not visited[u]:
                count += dfs_count(u)
        return count

    count = dfs_count(v)
    return count
def check_bridge(Graph, indexA,indexB):
    withBridge=count_components(Graph, indexA)
    Graph[indexA][indexB]=0
    Graph[indexB][indexA]=0
    withoutBridge=count_components(Graph, indexA)
    Graph[indexA][indexB]=1
    Graph[indexB][indexA]=1
    return withoutBridge>withBridge

def checkVerticeDegree(Graph, Vertice):
    i=Graph[Vertice].count(1)
    return i

def allEdgesUsed(G):
    return all(G[i][j] == 0 for i in range(len(G)) for j in range(i, len(G)))

def FleuryAlgorithm(Graph, Vertices, V):
    amountOfVertices = len(Vertices)
    GraphCopy = copy.deepcopy(Graph)
    cyclePath=[]
    def ECycle(startingPoint, actual):
        print(cyclePath)
        cyclePath.append(actual)
        if allEdgesUsed(GraphCopy) and actual == startingPoint:
            return True
        for i in Vertices:
            if GraphCopy[actual][i] == 1:
                if check_bridge(GraphCopy, actual, i) and checkVerticeDegree(GraphCopy, actual) > 1:
                    continue

                GraphCopy[actual][i] = 0
                GraphCopy[i][actual] = 0

                if ECycle(startingPoint, i):
                    return True

                GraphCopy[actual][i] = 1
                GraphCopy[i][actual] = 1



        cyclePath.pop()
        return False
    for _ in Vertices:
        cyclePath=[]
        if ECycle(_,_):
            print("Jest obwód Eulera")
            return cyclePath
    print("Obwód nie istnieje")
    return None