class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        count = 0
        zero = 0
        l = len(nums)
        slow = 0
        fast = 0
        while fast < l:
            if nums[fast] == 1:
                count += 1
                fast += 1
            elif zero < k and nums[fast] == 0:
                count += 1
                fast += 1
                zero += 1
            else:
                while slow <= fast and zero == k:
                    if nums[slow] == 0:
                        zero -= 1
                    count -= 1
                    slow += 1
                    #fast += 1
            ans = max(ans,count)
            #fast += 1
        return ans