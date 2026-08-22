class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pset = set()
        aset = set ()
        DIRECTIONS = [[0,1],[1,0],[-1,0],[0,-1]]
        rows, cols = len(heights), len(heights[0])

        def dfs(r,c,reachable_set):
            if r < 0 or c < 0 or r >= rows or c >= cols :
                return None
            if (r,c) in reachable_set:
                return None
            reachable_set.add((r,c)) # being updated in the place
            for dr, dc in DIRECTIONS:
                new_r = dr +r
                new_c = dc + c
                if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols :
                    continue
                if heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c, reachable_set)
        
        # starting actual ocean searches from borders and then passing to dfs
        for r in range(rows):
            dfs(r, 0, pset)         # Pacific: left column
            dfs(r, cols - 1, aset)  # Atlantic: right column
        
        for c in range(cols):
            dfs(0, c, pset)         # Pacific: top row
            dfs(rows - 1, c, aset)  # Atlantic: bottom row
        
        final = []

        for coord in pset:
            if coord in aset:
                final.append([coord[0], coord[1]]) 

        return final    
        

        
            

            
