class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        slow = 0
        fast = n
        while fast <= len(nums)-1:
            ans.append(nums[slow])
            ans.append(nums[fast])
            slow +=1
            fast+=1
        return ans