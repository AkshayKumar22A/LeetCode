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

        loc = 0
        while loc < l//2:
            nums[loc*2] = p[loc]
            nums[loc*2+1] = n[loc]
            loc+=1
        return nums
