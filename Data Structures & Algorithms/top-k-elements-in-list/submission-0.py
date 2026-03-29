class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counts = {}

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        sortedCounts = sorted(counts, key=counts.get, reverse=True)

        return sorted(sortedCounts[:k])

        