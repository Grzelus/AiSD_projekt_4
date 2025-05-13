from robertflores_nm import RobertFloresAlgorithm
from fleury_nm import FleuryAlgorithm
from create_nm import createNeighbourhoodMatrix
from create_mm import turn_into_mm
from fleury_mm import find_euler_cycle_aeg
from robertflores_mm import find_hamilton_cycle_ahg
import time

def from_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines

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
    #graph = tworzenie grafu
    print("wybór algorytmu:\n")
    print("1) Flores\n")
    print("2) Fleury\n")
    alg = int(input())
    if alg == 1:
        start = time.time()
        #CyclePath= 
        end = time.time()
    elif alg == 2:
        start = time.time()
        #CyclePath=
        end = time.time()
if CyclePath:
    print(CyclePath)
print(f"Czas wykonania algorytmu: {start-end}")