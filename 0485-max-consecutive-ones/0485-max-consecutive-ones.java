class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int current = 0;
        int sol = 0;

        for(int i=0;i<nums.length;i++) {
            if(nums[i]==0) {
                current = 0;
            } else {
                current +=1;
            }
            sol = Math.max(sol,current);
        }
        return sol;
    }
}