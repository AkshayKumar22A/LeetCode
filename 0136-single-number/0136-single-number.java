class Solution {
    public int singleNumber(int[] nums) {
        int sol = 0;
        for(int i=0;i<nums.length;i++) {
            sol = nums[i]^sol;
        }
        return sol;
    }
}