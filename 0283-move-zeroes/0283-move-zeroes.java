class Solution {
    public void moveZeroes(int[] nums) {
        if(nums.length<2) {
            return;
        }
        int slow = 0;
        int fast = 1;

        while(fast<nums.length) {
            if(nums[slow]!=0) {
                slow++;
                fast++;
            } else if(nums[fast]==0) {
                fast++;
            } else {
                int temp = nums[fast];
                nums[fast] = nums[slow];
                nums[slow] = temp;
            }
        }
    }
}