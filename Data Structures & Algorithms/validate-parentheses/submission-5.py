class Solution:
    def isValid(self, s: str) -> bool:
        validParenthesis = ['(', ')','{', '}', '[',']']
        stack = []

        for i in range(len(s)):
            if s[i] not in validParenthesis:
                return False
            
            index = validParenthesis.index(s[i])
            
            if index % 2 == 0:
                stack.append(s[i])
            else:
                if len(stack) == 0: return False

                p = stack.pop()
                openParen = validParenthesis[index - 1]
                if p != openParen:
                    return False
            
        return len(stack) == 0

        
        