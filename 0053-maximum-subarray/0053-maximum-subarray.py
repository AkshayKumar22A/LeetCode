class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        sum = 0
        ans = -1
        if l < 2:
            return nums[0]
        for i in range(l):
            if sum < 0:
                sum = 0
            sum = sum + nums[i]
            ans = max(sum,ans)
            print(f"sum:{sum},ans:{ans}")
        return ans