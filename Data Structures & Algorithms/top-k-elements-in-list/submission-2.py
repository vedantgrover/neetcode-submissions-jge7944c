class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = [];
        freqCounter = defaultdict(int)

        for n in nums:
            freqCounter[n] += 1
        
        freqList = sorted(list(freqCounter.items()), key=lambda item: item[1], reverse=True)

        print(freqList)
        
        for i in range(k):
            result.append(freqList[i][0])

        return result
