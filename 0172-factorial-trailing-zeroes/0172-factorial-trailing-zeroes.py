class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        fact = 1
        for i in range(n,1,-1):
            fact = fact * i
        count = 0
        while fact>0:
            last_digit = fact % 10
            if last_digit == 0:
                count+=1
            if last_digit != 0:
                break
            fact = fact // 10
        return count
        