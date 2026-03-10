class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums))
        result = []
        for num in nums:
            ans[num-1] = 1
        for i in range(0,len(nums)):
            if ans[i] == 0:
                result.append(i+1)
        return result