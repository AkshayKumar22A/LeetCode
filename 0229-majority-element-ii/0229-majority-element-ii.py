class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums)
        freq_map = dict()
        ans = list()
        for i in range(l):
            freq_map[nums[i]] = freq_map.get(nums[i],0) + 1
        print(freq_map)
        for i in freq_map:
            if freq_map[i] > (len(nums)//3):
                ans.append(i)
        return ans
