class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        l = len(nums)
        sum = 0            
        sumD = 0
        for i in range(l):
            sum += nums[i]

            temp = nums[i]
            while temp > 0:
                digit = temp % 10
                sumD += digit
                temp //= 10
        return abs(sum - sumD)
        