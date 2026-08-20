class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        row,col = len(grid), len(grid[0])
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs (r,c):
            nonlocal currArea
            if r < 0 or c < 0:
                return 0
            if (r,c) in visited:
                return 0
            if r >= row or c >= col or grid[r][c] == 0:
                return 0
            currArea += 1
            #print(currArea, grid[r][c])
            visited.add((r,c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
            return currArea
        for r in range(row):
            for c in range(col):
                currArea = 0
                #if grid[r][c] == 1 and (r,c) not in visited:
                maxArea = max(dfs(r,c),maxArea)
        
        return maxArea

        

                
            
        
        