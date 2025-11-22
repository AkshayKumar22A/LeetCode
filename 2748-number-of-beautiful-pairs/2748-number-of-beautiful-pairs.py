import math

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        l = len(nums)
        count = 0
        
        for i in range(l-1):
            a = str(nums[i])
            for j in range(i+1,l):
                b = str(nums[j])
                if math.gcd(int(a[0]), int(b[-1])) == 1:
                    count+=1

        return count
