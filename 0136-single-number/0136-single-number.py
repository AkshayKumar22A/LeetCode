class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_all = 0
        for i in nums:
            xor_all ^= i
        return xor_all
        
        