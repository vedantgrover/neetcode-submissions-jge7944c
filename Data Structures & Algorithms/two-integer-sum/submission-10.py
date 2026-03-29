class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = dict()

        """
        7 - 3 = 4
        7 - 4 = 3
        7 - 5 = 2
        7 - 6 = 1

        """

        result = []
        for i in range(len(nums)):
            diff = target - nums[i]

            if nums[i] in differences:
                result.append(differences[nums[i]])
                result.append(i)
                return result;
            else:
                differences[diff] = i
            
        return result