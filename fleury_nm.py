def FleuryAlgorithm(Graph, Vertices,V):
    amountOfVertices=len(Vertices)
    GraphCopy=Graph
    
    def ECycle(startingPoint, actual):
        cyclePath.append(actual)
        print(f"{cyclePath} \n")
        for i in Vertices:
            if GraphCopy[actual][i]==1:
                if len(cyclePath)==V+1 and i==startingPoint:
                    cyclePath.append(i)
                    return True
                GraphCopy[actual][i]=0
                GraphCopy[i][actual]=0
                if ECycle(startingPoint,i):
                    return True
        
        GraphCopy[cyclePath[len(cyclePath)-2]][actual]=1
        GraphCopy[actual][cyclePath[len(cyclePath)-2]]=1
        return False
    for _ in Vertices:
        cyclePath=[]
        if ECycle(_,_):
            print("Jest obwód Eulera")
            return cyclePath
    print("Obwód nie istnieje")
    return None