from robertflores_nm import RobertFloresAlgorithm
from fleury_nm import FleuryAlgorithm
from create_nm import createNeighbourhoodMatrix
import time

def from_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines

##nie wiem czy to sie przyda do macierzy ale póki co zostawiam
def graph_al_from_file(filename):
    lines=from_file(filename)
    num_vertices, num_edges = map(int, lines[0].split())

    for line in lines[1:]:
        u, v = map(int, line.split())
        graph.add_edge(u, v)
    return graph

def graph_nm_from_file(filename):
    lines=from_file(filename)
    return createNeighbourhoodMatrix(lines)


print("wybierz format grafu:\n")
print("1) macierz sąsiedztwa\n")
print("2) macierz następników\n")

format = int(input())

if format == 1:
    file = input("wczytaj graf z pliku: ")
    [graph,Vertices] = graph_nm_from_file(file)
    print("wybór algorytmu:\n")
    print("1) Flores\n")
    print("2) Fleury\n")
    alg = int(input())
    if alg == 1:
        start = time.time()
        CyclePath = RobertFloresAlgorithm(graph,Vertices)
        end = time.time()
    if alg == 2:
        start = time.time()
        CyclePath=FleuryAlgorithm(graph,Vertices)
        end = time.time()

## zostawiłem tylko szkielet żeby dopisać twoje funkcje
elif format == 2:
    file = input("wczytaj graf z pliku: ")
    graph = graph_al_from_file(file)
    print("wybór algorytmu:\n")
    print("1) Flores\n")
    print("2) Fleury\n")
    alg = int(input())
    if alg == 1:
        start = time.time()
        end = time.time()
    elif alg == 2:
        start = time.time()
        end = time.time()
        
print(f"Czas wykonania algorytmu: {start-end}")