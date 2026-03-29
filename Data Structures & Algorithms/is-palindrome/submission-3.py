class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        if len(s) == 1:
            return True

        while l <= r:
            while not s[l].isalnum():
                if l < r:
                    l += 1
                else:
                    break;
            
            while not s[r].isalnum():
                if r > l:
                    r -= 1
                else:
                    break
            
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        
        return True



        

        