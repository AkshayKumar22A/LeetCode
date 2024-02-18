class Solution {
    public int[] sortedSquares(int[] nums) {
        int sol[] = new int[nums.length];

        int start = 0;
        int end = nums.length - 1;
        int idx = sol.length - 1;

        while (start <= end) {
            if (nums[start] * nums[start] >= nums[end] * nums[end]) {
                sol[idx] = nums[start] * nums[start];
                start++;
            } else {
                sol[idx] = nums[end] * nums[end];
                end--;
            }
            idx--;
        }
        return sol;
    }
}