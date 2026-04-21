class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        subans = 0
        left = 0
        right = len(height)-1
        while left < right:
                subans = (right-left) * min(height[left],height[right])
                ans = max(ans,subans)
                if height[left] < height[right]:
                    left += 1
                elif height[right] <= height[left]:
                    right -= 1
        return ans