class Solution {
    public int findDuplicate(int[] nums) {
        return printDuplicates(nums);
    }

    static int printDuplicates(int[] nums) {
        int slow = 0;
        int fast = 0;

        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        int slow2 = 0;

        do {
            slow = nums[slow];
            slow2 = nums[slow2];
        } while (slow != slow2);

        return slow2;
    }

}