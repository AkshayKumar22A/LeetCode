class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        s = (len(nums)*(len(nums)+1))//2
        freq_map = dict()
        for num in nums:
            freq_map[num] = freq_map.get(num,0) + 1
            if freq_map[num] == 2:
                ans.append(num)
        missing = s - (sum(nums) - ans[0])
        ans.append(missing)
        return ans

        