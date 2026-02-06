class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        l = len(nums)
        subsets = []
        for i in range(1<<l):
            current_subset = []
            for j in range(l):
                if (i>>j) & 1:
                    current_subset.append(nums[j])
            subsets.append(current_subset)
        
        ans = 0
        for subset in subsets:
            xor_sum = 0
            for i in subset:
                xor_sum ^= i
            ans += xor_sum
        return ans


                
        