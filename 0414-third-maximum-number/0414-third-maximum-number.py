class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = -inf
        second_max = -inf
        third_max = -inf
    
        for num in nums:
            if first_max == num or second_max == num or third_max == num:
                continue
            if first_max <= num:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif second_max <= num:
                third_max = second_max
                second_max = num
            elif third_max <= num:
                third_max = num

        if third_max == -inf:
            return first_max
        
        return third_max