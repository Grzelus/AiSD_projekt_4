import numpy as np
import pandas as pd
from typing import List, Tuple, Optional
from collections import defaultdict, deque


with open("test.txt", "r") as file:
    lines = file.readlines()

edge_list = [tuple(map(int, line.rstrip().split())) for line in lines]
n = edge_list[0][0]
edge_list = edge_list[1:]


def turn_into_mm(n: int, edges: List[Tuple[int,int]]):
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
    
M = turn_into_mm(n, edge_list)

def find_hamilton_cycle_ahg(M: pd.DataFrame) -> Optional[List[int]]:
    n = M.shape[0]
    visited = [False] * (n + 1)
    path = []
    successors = {i: [] for i in range(1, n + 1)}

    for i in range(1, n + 1):
        first_succ = M.iloc[i - 1, n]
        if first_succ != 0:
            successors[i].append(first_succ)
            current = first_succ
            while True:
                next_succ = M.iloc[i - 1, current - 1]
                if next_succ == 0 or next_succ == current or next_succ in successors[i]:
                    break
                successors[i].append(next_succ)
                current = next_succ

    def dfs(v: int, depth: int) -> bool:
        path.append(v)
        visited[v] = True
        if depth == n:
            return path[0] in successors[v]
        for u in successors[v]:
            if not visited[u]:
                if dfs(u, depth + 1):
                    return True
        path.pop()
        visited[v] = False
        return False

    for start in range(1, n + 1):
        path.clear()
        visited = [False] * (n + 1)
        if dfs(start, 1):
            path.append(start)
            return path

    return None

def find_euler_cycle_aeg(M: pd.DataFrame) -> List[int]:
    n = M.shape[0]
    graph = defaultdict(list)

    for i in range(1, n + 1):
        current = M.iloc[i - 1, n]
        if current == 0:
            continue
        graph[i].append(current)
        next_val = M.iloc[i - 1, current - 1]
        while next_val != current and next_val != 0 and next_val not in graph[i]:
            graph[i].append(next_val)
            current = next_val
            next_val = M.iloc[i - 1, current - 1]

    in_deg = defaultdict(int)
    out_deg = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            out_deg[u] += 1
            in_deg[v] += 1

    for i in range(1, n + 1):
        if in_deg[i] != out_deg[i]:
            return []

    stack = [next(iter(graph))]
    path = []
    local_graph = {u: deque(vs) for u, vs in graph.items()}

    while stack:
        v = stack[-1]
        if local_graph.get(v):
            u = local_graph[v].popleft()
            stack.append(u)
        else:
            path.append(stack.pop())

    return path[::-1]

print(find_euler_cycle_aeg(M))
print(find_hamilton_cycle_ahg(M))