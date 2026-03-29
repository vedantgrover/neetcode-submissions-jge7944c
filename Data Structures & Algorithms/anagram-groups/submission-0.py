class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        sortedStrs = []
        history = {} # val: count

        for s in strs:
            sortedStrs.append(''.join(sorted(s)))

        for i in range(len(sortedStrs)):
            if sortedStrs[i] in history:
                history[sortedStrs[i]].append(strs[i])
            else:
                history[sortedStrs[i]] = [strs[i]]
        
        for key in history:
            result.append(history[key])
        
        return result

        

        

        