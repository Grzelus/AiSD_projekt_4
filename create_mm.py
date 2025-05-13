import numpy as np
import pandas as pd
from typing import List, Tuple

def turn_into_mm(filename):
    n, edge_list = create_edge_list(filename)
    return create_mm(n,edge_list)

def create_edge_list(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    edge_list = [tuple(map(int, line.rstrip().split())) for line in lines]
    n = edge_list[0][0]
    edge_list = edge_list[1:]
    return n, edge_list


def create_mm(n: int, edges: List[Tuple[int,int]]):
    LN = {i: [] for i in range(1, n+1)}
    LP = {i: [] for i in range(1, n+1)}
    incident_matrix = np.zeros((n + 1, n + 1), dtype=bool)

    for u, v in edges:
        LN[u].append(v)
        LP[v].append(u)
        incident_matrix[u][v] = True
    
    LB = {}
    for i in range(1, n+1):
        incident = set()
        incident.add(i)
        incident = set(LN[i]) | set(LP[i]) 
        LB[i] = [j for j in range(1,n+1) if j not in incident]
    

    M = np.zeros((n,n+4), dtype=int)


    for i in range(1, n + 1):
        M[i - 1][n] = LN[i][0] if LN[i] else 0
        M[i - 1][n + 1] = LP[i][0] if LP[i] else 0
        M[i - 1][n + 2] = LB[i][0] if LB[i] else 0
        M[i - 1][n + 3] = 0 

    for i in range(1, n + 1):
        successors = LN[i]
        for idx, j in enumerate(successors):
            if idx + 1 < len(successors):
                M[i - 1][j - 1] = successors[idx + 1]
            else:
                M[i - 1][j - 1] = successors[-1]

    for i in range(1, n + 1):
        preds = LP[i]
        for idx, j in enumerate(preds):
            if idx + 1 < len(preds):
                M[i - 1][j - 1] = preds[idx + 1] + n
            else:
                M[i - 1][j - 1] = preds[-1] + n

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if not incident_matrix[i][j] and not incident_matrix[j][i]:
                lb_list = LB[j]
                if not lb_list:
                    continue
                try:
                    idx = lb_list.index(i)
                    if idx + 1 < len(lb_list):
                        M[i - 1][j - 1] = -lb_list[idx + 1]
                    else:
                        M[i - 1][j - 1] = -lb_list[-1]
                except ValueError:
                    M[i - 1][j - 1] = -lb_list[0] if lb_list else 0
    
                
    columns = list(range(1, n + 1)) + ['LN', 'LP', 'LB', 'LC']
    index = list(range(1, n + 1))
    df = pd.DataFrame(M, columns=columns, index=index)

    return df
    