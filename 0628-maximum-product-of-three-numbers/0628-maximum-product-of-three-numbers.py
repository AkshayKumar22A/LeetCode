class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        l = len(nums)
        nums.sort()
        a = nums[0]
        b = nums[1]
        d = nums[l-1]
        e = nums[l-2]
        f = nums[l-3]
        return max((a * b * d),(d * e * f))



        
            


        