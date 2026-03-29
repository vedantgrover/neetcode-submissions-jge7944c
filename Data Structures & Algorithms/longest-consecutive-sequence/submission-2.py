class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nonDuplicateNums = list(set(nums))
        nonDuplicateNums.sort()
        largestFreq = 0;

        print(nonDuplicateNums)

        if not nonDuplicateNums:
            return largestFreq
        
        freq = 1
        for i in range(len(nonDuplicateNums) - 1):
            if nonDuplicateNums[i] == (nonDuplicateNums[i + 1] - 1):
                freq += 1
            else:
                if freq > largestFreq:
                    largestFreq = freq
                freq = 1
        
        if freq > largestFreq:
            largestFreq = freq
        
        return largestFreq
        