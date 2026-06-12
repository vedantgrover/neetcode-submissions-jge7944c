class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = 0

        for num in nums:
            n = n ^ num
        
        for i in range(len(nums) + 1):
            n = i ^ n
        
        return n