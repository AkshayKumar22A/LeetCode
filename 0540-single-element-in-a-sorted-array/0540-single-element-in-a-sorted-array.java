class Solution {
    public int singleNonDuplicate(int[] nums) {
        int ans = findnum(nums);
        return ans;

    }

    public static int findnum(int arr[]) {
        if (arr.length == 1) {
            return arr[0];
        }
        if (arr[0] != arr[1]) {
            return arr[0];
        }
        if (arr[arr.length - 1] != arr[arr.length - 2]) {
            return arr[arr.length - 1];
        }

        int start = 0;
        int end = arr.length - 1;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (arr[mid] != arr[mid + 1] && arr[mid] != arr[mid - 1]) {
                return arr[mid];
            }
            if (mid % 2 == 0) {
                if (arr[mid + 1] == arr[mid]) {
                    start = mid + 1;
                } else if (arr[mid - 1] == arr[mid]) {
                    end = mid;
                }
            } else {
                if (mid % 2 == 1 && arr[mid - 1] == arr[mid]) {
                    start = mid + 1;
                } else if (mid % 2 == 1 && arr[mid + 1] == arr[mid]) {
                    end = mid;
                }
            }
        }
        return -1;
    }
}