def Fleury(Graph, Vertices,V):
    amountOfVertices=len(Vertices)
    cyclePath=[]
    GraphCopy=Graph
    for _ in Vertices:
        if ECycle(_):
            print("Jest obwód Eulera")
    def ECycle(startingPoint, actual):
        for i in Vertices:
            if GraphCopy[actual][i]==1:
                if len(cyclePath)==V and i==startingPoint:
                    return True
                cyclePath.append(i)
                GraphCopy[actual][i]=2
                if ECycle(startingPoint,i):
                    return True
        
        GraphCopy[len(cyclePath)-2][actual]=1
        return False
    return 