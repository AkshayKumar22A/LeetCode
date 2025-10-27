class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        l = len(moveFrom)
        l2 = len(nums)
        i = 0
        nums = set(nums)
        while(i < l):
            if moveFrom[i] in nums:
                nums.remove(moveFrom[i])
                nums.add(moveTo[i])
            i+=1
        nums = list(nums)
        nums.sort()
        return nums

        