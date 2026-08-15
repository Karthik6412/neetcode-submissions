class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # frequency hashmap
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in nums: 
            freq[num] = 1 + freq.get(num,0)
        for num, counts in freq.items():
            buckets[counts].append(num)
        res = []
        for index in range(len(buckets) - 1, -1, -1):
            for num in buckets[index]:
                res.append(num)
                if len(res) == k:
                    return res

        return False 
        
                           

        
