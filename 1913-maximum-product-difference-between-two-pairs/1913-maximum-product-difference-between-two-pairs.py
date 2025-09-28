class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        l = len(nums)
        largest = float('-inf')
        seclargest = float('-inf')
        smallest = float('inf')
        secsmallest = float('inf')
        for i in range(l):
            if largest < nums[i]:
                seclargest = largest
                largest = nums[i]
            elif seclargest < nums[i] and seclargest != largest:
                seclargest = nums[i]
            if smallest > nums[i]:
                secsmallest = smallest
                smallest = nums[i]
            elif secsmallest > nums[i] and secsmallest != smallest:
                secsmallest = nums[i]
        return (largest * seclargest) - (smallest * secsmallest)
