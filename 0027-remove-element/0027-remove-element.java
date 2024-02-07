class Solution {
    public int removeElement(int[] nums, int val) {
        int ans = coutRemoveElement(nums, val);
        return ans;

    }

    public static int coutRemoveElement(int nums[], int val) {
        int temp = Integer.MAX_VALUE;
        int start = 0;
        int count = 0;
        ;

        while (start < nums.length) {
            if (nums[start] == val) {
                nums[start] = temp;
                count++;
            }
            start++;
        }
        Arrays.sort(nums);
        return nums.length - count;
    }
}