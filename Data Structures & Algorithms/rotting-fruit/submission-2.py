class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        orangesF = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                if grid[r][c] == 1:
                    orangesF += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        
        print("queue is ", q)
        #bfs begins
        while q:
            qLen = len(q)
            rottedThisLevel = False        
            for i in range(qLen):
                r,c = q.popleft()
                for dr, dc in directions:
                    newR = r + dr
                    newC = c + dc
                    if newR < 0 or newC < 0 or newR >= rows or newC >= cols:
                        continue
                    if grid[newR][newC] == 0:
                        continue
                    if grid[newR][newC] == 1:
                        orangesF -= 1
                        grid[newR][newC] = 2
                        rottedThisLevel = True
                        q.append((newR,newC))
            if rottedThisLevel:
                minutes += 1
        
        if orangesF > 0:
            return -1
        return minutes
            

                        
        
           

        