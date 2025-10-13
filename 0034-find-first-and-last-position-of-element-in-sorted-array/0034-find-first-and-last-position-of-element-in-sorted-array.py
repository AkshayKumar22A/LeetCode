class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            if nums[i]==target:
                ans.append(i) 
                break     
           
        for j in range(len(nums),0,-1):
            if nums[j-1]==target:
                ans.append(j-1)  
                break
        if len(ans)==0:
            return [-1,-1]
        elif len(nums)==1:
            return [0,0]                
        return ans  