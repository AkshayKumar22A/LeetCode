class Solution {
    public int findMaxLength(int[] nums) {
        return sol(nums);
    }

    public static int sol(int[] nums) {
        // Map to store the cumulative count of 0s and 1s encountered
        Map<Integer, Integer> countMap = new HashMap<>();
        // Initialize countMap with 0 count for both 0s and 1s
        countMap.put(0, -1);

        int maxLength = 0;
        int count = 0; // Difference between count of 0s and 1s

        for (int i = 0; i < nums.length; i++) {
            // Increment count if nums[i] is 1, else decrement count
            count += nums[i] == 1 ? 1 : -1;
            if (countMap.containsKey(count)) {
                // If the count is already present in the map, update maxLength
                maxLength = Math.max(maxLength, i - countMap.get(count));
            } else {
                // If count is not present, add it to the map with its index
                countMap.put(count, i);
            }
        }
        return maxLength;
    }
}