class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bestmaxH = 0
        l,r = 0, len(heights) - 1
        while l < r:
            width = r - l
            maxA = min(heights[r],heights[l]) * abs(r-l)
            if maxA > bestmaxH:
                bestmaxH = maxA
            if heights[l] == min(heights[r],heights[l]):
                l += 1
            elif heights[r] == min(heights[r],heights[l]):
                r -= 1
        return bestmaxH
            