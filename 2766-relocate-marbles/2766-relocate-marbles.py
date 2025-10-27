class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        nums = set(nums)
        for from_pos, to_pos in zip(moveFrom, moveTo):
            nums.discard(from_pos)  # Remove the marble from current position
            nums.add(to_pos)         # Add the marble to new position
        return sorted(nums)        