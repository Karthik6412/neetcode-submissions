class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,best_size,currsize = 0,0,0,0
        window = set()
        while r != len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
                currsize -= 1
            if s[r] not in window:
                window.add(s[r])
                currsize = r - l + 1
            if currsize > best_size:
                best_size = currsize
            r += 1
        return best_size

