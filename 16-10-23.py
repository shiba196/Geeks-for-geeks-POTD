from typing import List

class Solution:
    
        
    def largestIsland(self, grid : List[List[int]]) -> int:
        
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        parentSize = {}

        def is_valid(i, j):
            return 0 <= i < n and 0 <= j < n

        def set_graph_parent(graphParent, grid, i, j, parent):
            graphParent[i][j] = parent
            count = 1
            for dir in directions:
                dx, dy = i + dir[0], j + dir[1]
                if is_valid(dx, dy) and grid[dx][dy] == 1 and graphParent[dx][dy] == -1:
                    count += set_graph_parent(graphParent, grid, dx, dy, parent)
            parentSize[parent] = count
            return count

        graphParent = [[-1] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and graphParent[i][j] == -1:
                    set_graph_parent(graphParent, grid, i, j, i * n + j)

        an = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    distinct_parent = set()
                    for dir in directions:
                        dx, dy = i + dir[0], j + dir[1]
                        if is_valid(dx, dy) and grid[dx][dy] == 1 and graphParent[dx][dy] not in distinct_parent:
                            distinct_parent.add(graphParent[dx][dy])
                    temp = 0
                    for parent in distinct_parent:
                        temp += parentSize[parent]
                    an = max(an, temp + 1)
                else:
                    an = max(an, parentSize[graphParent[i][j]])

        return an
        
       