import pandas as pd
from typing import List
from collections import defaultdict, deque

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
