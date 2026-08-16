class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,best_size,currsize = 0,0,0,0
        window = set()
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
                currsize -= 1
            window.add(s[r])
            currsize = r - l + 1
            best_size = max(best_size, currsize)
            
        return best_size

