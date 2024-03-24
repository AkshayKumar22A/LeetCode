class Solution {
    public List<Integer> findDuplicates(int[] nums) {
         List<Integer> sol = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            int index = Math.abs(nums[i]) - 1;
            if (nums[index] < 0) {
                sol.add(Math.abs(nums[i]));
                continue;
            }
            nums[index] *= -1;
        }
        return sol;
    }
}