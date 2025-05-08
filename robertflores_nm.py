def RobertFloresAlgorithm(Graph,Vertices):
    visitedVertices = [False for _ in range(len(Vertices)+1)]
    cyclePath=[]

    def Hamiltonian(startingVertice, actual):
        amountOfVertices=len(Vertices)
        visitedVertices[actual]=True
        counterOfVisited=visitedVertices.count(True)
        for i in Vertices:
            if Graph[actual][i]==1:
                
                if counterOfVisited==amountOfVertices and i==startingVertice:
                    return True
                elif not visitedVertices[i]:
                    if Hamiltonian(startingVertice, i):
                        cyclePath.insert(0,actual)
                        print(f"{cyclePath}" )
                        return True
        
        visitedVertices[actual]=False
        return False

    for i in Vertices:
        if Hamiltonian(i,i): 
            print("znaleziono cykl Hamiltona")
            return [cyclePath]
    return None