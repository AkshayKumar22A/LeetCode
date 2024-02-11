class Solution {
    public int searchInsert(int[] nums, int target) {
        int ans = find(nums,target);
        return ans;
    }

    public static int find(int nums[],int target)
    {
        int sol = 0;
        int start = 0;
        int end = nums.length-1;

        while(start<=end)
        {
            int mid = (start + end) / 2;
            if(nums[mid] == target)
            {
                return mid;
            }
            else if(nums[mid] < target)
            {
                start = mid + 1;
            }
            else
            {
                end = mid - 1;
            }
        }
        return start;
    }
}