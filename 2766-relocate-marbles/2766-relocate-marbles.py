class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        i = 0
        nums = set(nums)
        while(i < len(moveFrom)):
            if moveFrom[i] in nums:
                nums.remove(moveFrom[i])
                nums.add(moveTo[i])
            i+=1
        return sorted(nums)

        