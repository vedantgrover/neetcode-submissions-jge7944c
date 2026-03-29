import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        sWithoutSpaces = ''.join([char for char in s if char not in punctuation]).replace(" ", "").lower()
        
        n = len(sWithoutSpaces) - 1
        
        for i in range(n):
            if i >= (n - i):
                break
            
            if (sWithoutSpaces[i] != sWithoutSpaces[n - i]):
                return False

        return True
        