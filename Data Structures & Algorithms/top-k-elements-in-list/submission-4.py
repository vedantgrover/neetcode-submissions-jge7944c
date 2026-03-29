class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = [];
        freqCounter = defaultdict(int)

        for n in nums:
            freqCounter[n] += 1
        
        for i in range(k):
            maxFreq = max(freqCounter, key=freqCounter.get)
            freqCounter.pop(maxFreq, None)
            result.append(maxFreq)

        return result
