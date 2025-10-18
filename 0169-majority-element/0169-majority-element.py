class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        for num in nums:
            print(count)
            if count == 0:
                candidate = num
            if num == candidate:
                count+=1
            else:
                count-=1
        return candidate