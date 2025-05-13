def printGraph(Tab):
    for i in Tab:
        print(i)

def createNeighbourhoodMatrix(Tab):
    A,V=map(int,Tab[0].split())
    AvailableVertices=[]
    for i in range(1,A+1):
        AvailableVertices.append(i)

    Graph=[[0 for x in range(A+1)]for y in range(A+1)]
    
    for i in range(1,V+1):
        a,b=map(int,Tab[i].split())
        if(a<=A and b<=A):
            Graph[a][b]=1 
            Graph[b][a]=-1
        else:
            print(f"Out of range {a} and {b}")

    printGraph(Graph)
    return [Graph,AvailableVertices]