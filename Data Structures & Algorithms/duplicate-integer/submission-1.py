class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenValues = set()

        for i in range(len(nums)):
            if nums[i] in seenValues:
                return True
            else:
                seenValues.add(nums[i])
        
        return False
         