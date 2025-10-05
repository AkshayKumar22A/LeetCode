class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        p = [] * (l//2)
        n = [] * (l//2)

        for i in range(l):
            if nums[i] > 0:
                p.append(nums[i])
            else:
                n.append(nums[i])
        
        for i in range(l//2):
            nums[i*2] = p[i]
            nums[i*2+1] = n[i]
        return nums
