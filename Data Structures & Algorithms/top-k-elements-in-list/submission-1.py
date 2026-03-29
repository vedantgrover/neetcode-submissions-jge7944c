class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counts = {}

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        
        sortedCounts = sorted(counts, key=counts.get, reverse=True)

        return sorted(sortedCounts[:k])

        