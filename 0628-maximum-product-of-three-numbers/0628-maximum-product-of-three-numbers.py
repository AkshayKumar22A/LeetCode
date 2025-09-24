class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        fe, se, te = float("-inf"), float("-inf"), float("-inf") 
        min1, min2 = float("inf"), float("inf")                 

        for num in nums:
            # Update top 3 max
            if num > fe:
                te, se, fe = se, fe, num
            elif num > se:
                te, se = se, num
            elif num > te:
                te = num

            # Update bottom 2 min
            if num < min1:
                min2, min1 = min1, num
            elif num < min2:
                min2 = num

        return max(fe * se * te, fe * min1 * min2)