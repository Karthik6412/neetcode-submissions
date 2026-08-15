class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        print("s is: ",s)
        print("The length of nums is: ",len(nums), " and the length of s is: ", len(s) )
        if len(nums) > len(s):
            return True
        return False
        