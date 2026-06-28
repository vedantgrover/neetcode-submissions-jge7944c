class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        frequency = dict()

        for n in nums:
            if n not in frequency:
                frequency[n] = 1
            else:
                frequency[n] += 1
        
        for i in range(k):
            mx_item = max(frequency, key=frequency.get)
            result.append(mx_item)
            frequency[mx_item]= 0
        
        return result