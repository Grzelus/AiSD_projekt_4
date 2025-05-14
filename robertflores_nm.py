def RobertFloresAlgorithm(Graph,Vertices):
    visitedVertices = [False for _ in range(0,len(Vertices)+1)]
    cyclePath=[]
    dest=[True for _ in range(0,len(Vertices)+1) ]
    dest[0]=False
    def Hamiltonian(startingVertice, actual):
        amountOfVertices=len(Vertices)
        visitedVertices[actual]=True
        counterOfVisited=visitedVertices.count(True)
        for i in Vertices:
            if Graph[actual][i]==1:
                
                if visitedVertices==dest and i==startingVertice:
                    cyclePath.insert(0,i)
                    cyclePath.insert(0,actual)
                    return True
                elif not visitedVertices[i]:
                    if Hamiltonian(startingVertice, i):
                        cyclePath.insert(0,actual)
                       #print(f"{cyclePath}" )
                        return True
        
        visitedVertices[actual]=False
        return False

    for i in Vertices:
        cyclePath=[]
        if Hamiltonian(i,i): 
            print("znaleziono cykl Hamiltona")
            return [cyclePath]
    return None