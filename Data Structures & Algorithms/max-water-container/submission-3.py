class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bestmaxH = 0
        l,r = 0, len(heights) - 1
        while l < r:
            width = r - l
            lH = min(heights[r],heights[l])
            maxA =  lH * (r-l)
            if heights[l] == lH:
                l += 1
            elif heights[r] == lH:
                r -= 1
            if maxA > bestmaxH:
                bestmaxH = maxA
        return bestmaxH
            