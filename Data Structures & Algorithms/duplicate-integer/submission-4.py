class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arraySet = set(nums)

        return len(nums) != len(arraySet)
        