class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        if k ==0:
            return
        l = len(nums)
        k = k if k <= l else k % l 
        self.reverse(nums,0,l-k-1)
        self.reverse(nums,l-k,l-1)
        self.reverse(nums,0,l-1)
        
    def reverse(self,nums,start,end):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1
        