class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False

        
        b = 1
        n -= 10

        for i in range(9, 0, -1):
            if n < i:
                return b == 1
            n -= i
            b = 1 - b

        return False