class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        visited = set()

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0),
        (-1,0),
        (0,1),
        (0,-1)]

        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0" or (r,c) in visited:
                return None
            visited.add((r,c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    island += 1
                    dfs(r,c)
        return island

        