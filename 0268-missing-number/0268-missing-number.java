class Solution {
    public int missingNumber(int[] nums) {
        int count[] = new int[nums.length+1];
        for(int i=0;i<nums.length;i++) {
            count[nums[i]] +=1;
        }
        int sol=0;
        for(int i=0;i<count.length;i++) {
            if(count[i]==0) {
                sol = i;
            }
        }
        return sol;
    }
}