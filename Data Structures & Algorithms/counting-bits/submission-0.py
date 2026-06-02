class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for i in range(len(result)):
            n = i

            while n != 0:
                if n % 2 == 1:
                    result[i] += 1
                
                n = n >> 1
            
        return result