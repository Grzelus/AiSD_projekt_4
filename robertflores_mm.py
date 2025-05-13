import pandas as pd
from typing import List, Optional


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