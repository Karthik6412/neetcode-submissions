import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        curr_rate = 0
        def feasibility(k):
            total_hours = 0
            for i in piles:
               total_hours += math.ceil(i/k)
            if total_hours > h:
                return False
            return True



            
        
        l, r = 1, sum(piles)
        while l < r:
            m = (l + r) // 2
            if feasibility(m):
                r = m
            else:
                l = m + 1
        return l 