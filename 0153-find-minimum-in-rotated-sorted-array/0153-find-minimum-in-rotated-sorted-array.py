class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float("inf")
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = low + (high - low) // 2
            ans = min(ans,nums[mid])
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return ans     
        