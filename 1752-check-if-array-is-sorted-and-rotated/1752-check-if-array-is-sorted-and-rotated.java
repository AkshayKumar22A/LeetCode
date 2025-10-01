class Solution {
    public boolean check(int[] nums) {
        //Use a variable, count, to track the number of drops (where nums[i] > nums[i+1]).
        int drop = 0;
        for(int i = 0; i < nums.length; i++){
            // Compare current with the next (circular comparison)
            if(nums[i] > nums[(i + 1) % nums.length]){
                drop++;
            }
        }
        return drop <= 1;
    }
}