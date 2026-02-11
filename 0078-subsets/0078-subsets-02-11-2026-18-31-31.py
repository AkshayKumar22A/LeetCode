class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total_subsets = 1<<n # 2^n
        subset = []
        for num in range(0,total_subsets):
            current_subset = []
            for i in range(0,n):
                if (num & (1<<i)) != 0:
                    current_subset.append(nums[i])
            subset.append(current_subset)
        return subset