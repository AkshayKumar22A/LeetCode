class Solution {
    public int countPairs(List<Integer> nums, int target) {
        int ans = countPair(nums, target);
        return ans;
    }

    public static int countPair(List<Integer> arr, int target) {
        int count = 0;
        int start = 0;
        int end = arr.size() - 1;
        Collections.sort(arr);
        while (start < end) {
            int left = arr.get(start);
            int right = arr.get(end);
            if (left + right < target) {
                count += end - start;
                start++;
            } else {
                end--;
            }
        }
        return count;
    }
}