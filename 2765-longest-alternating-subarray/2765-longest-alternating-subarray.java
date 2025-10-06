class Solution {
    public int alternatingSubarray(int[] nums) {
                int ans=-1,i=0,j=1,check=1;
        while(j<nums.length){
            if(nums[j]-nums[j-1]==check){
                j++;
                check*=-1;
            }
            else{
                
                if(j-i+1>2){
                    ans=Math.max(j-i,ans);
                    i=j-1;
                }
                else{
                    i=j;
                    j++;
                }
                check=1;
            }
        }
        if(j-i+1>2){
            ans=Math.max(j-i,ans);
        }
        return ans;
    }
}