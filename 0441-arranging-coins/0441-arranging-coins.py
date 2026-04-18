class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        i = 1
        while n != 0:
            if n < i:
                break
            count += 1
            n = n - i
            i+= 1
        return count