class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for s in strs:
            char_freq = [0] * 26

            for c in s:
                char_freq[ord(c) - ord('a')] += 1
            
            t_char_freq = tuple(char_freq)
            if t_char_freq in anagrams:
                anagrams[t_char_freq].append(s)
            else:
                anagrams[t_char_freq] = [s]
            
        result = []
        for a in anagrams:
            result.append(anagrams[a])
        
        return result