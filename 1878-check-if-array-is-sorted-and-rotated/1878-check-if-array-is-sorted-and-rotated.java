class Solution {
    public boolean check(int[] nums) {
        int drop = 0;
        for(int i = 1; i < nums.length; i++){
            // Count drops where the current element is greater than the next one
            if(nums[i - 1] > nums[i]){
                drop++;
            }
        }

        // Check if there is a drop from the last element to the first element
        if(nums[0] < nums[nums.length - 1]) drop++;
        
        // The array is sorted or can be sorted with at most one rotation if drop count <= 1
        return drop <= 1;
    }
}