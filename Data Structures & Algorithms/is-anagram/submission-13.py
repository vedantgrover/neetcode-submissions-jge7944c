class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sLetterFreq = dict()
        tLetterFreq = dict()

        for i in range(len(s)):
            currentSLetter = s[i]
            currentTLetter = t[i]

            if sLetterFreq.get(currentSLetter):
                sLetterFreq[currentSLetter] += 1
            else:
                sLetterFreq[currentSLetter] = 1
            
            if tLetterFreq.get(currentTLetter):
                tLetterFreq[currentTLetter] += 1
            else:
                tLetterFreq[currentTLetter] = 1

        
        return sLetterFreq == tLetterFreq


        