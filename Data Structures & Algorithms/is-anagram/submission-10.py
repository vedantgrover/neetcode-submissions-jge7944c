class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqCounter = [0] * 26

        for ch in s.lower():
            freqCounter[ord(ch) - ord('a')] += 1
        
        for ch in t.lower():
            freqCounter[ord(ch) - ord('a')] -= 1

        return all(i == 0 for i in freqCounter)

        