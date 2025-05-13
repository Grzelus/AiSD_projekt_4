import copy
def countVertices(GraphCopy,v):
    n = len(GraphCopy)
    visited = [False] * (n+1)

    def dfs_count(v):
        visited[v] = True
        count = 1
        print(v)
        for u in range(1,n):
            if GraphCopy[v][u]==1 and not visited[u]:
                count += dfs_count(u)
        return count

    count = dfs_count(v)
    return count

def check_bridge(GraphCopy, indexA,indexB):
    GraphCopy[indexA][indexB]=0
    GraphCopy[indexB][indexA]=0
    withoutBridge=countVertices(GraphCopy, indexB)
    GraphCopy[indexA][indexB]=1
    GraphCopy[indexB][indexA]=1
    withBridge=countVertices(GraphCopy, indexB)
   # print(f"{withBridge}, {withoutBridge}")
    return withoutBridge <withBridge

def checkVerticeDegree(Graphcopy, Vertice):
    i=Graphcopy[Vertice].count(1)
    return i

def allEdgesUsed(G,n):
    Zeros=[[0 for _ in range(n+1)] for _ in range(n+1)]
    #print(Zeros)
    if Zeros==G:   
        return True
    return False
def FleuryAlgorithm(Graph, Vertices, V):
    amountOfVertices = len(Vertices)
    GraphCopy = copy.deepcopy(Graph)
    cyclePath=[]
    def ECycle(startingPoint, actual):
        cyclePath.append(actual)

        if startingPoint==1 and len(cyclePath)<=7:
            print(cyclePath)
            printGraph(GraphCopy)
            print(checkVerticeDegree(GraphCopy,actual))

        if allEdgesUsed(GraphCopy,amountOfVertices) and actual == startingPoint:
            return True
        
        if checkVerticeDegree(GraphCopy, actual)==0:
            return False
        
        for i in Vertices:
            if GraphCopy[actual][i] == 1:
                if check_bridge(GraphCopy, actual, i) and checkVerticeDegree(GraphCopy, actual) > 1:
                    continue

                GraphCopy[actual][i] = 0
                GraphCopy[i][actual] = 0

                if ECycle(startingPoint, i):
                    return True
                else: 
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