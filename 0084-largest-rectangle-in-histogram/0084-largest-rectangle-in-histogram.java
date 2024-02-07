class Solution {
    public int largestRectangleArea(int[] heights) {
        return Area(heights);
    }

    public static int Area(int arr[]) {
        Stack<Integer> st = new Stack<>();
        int ans = 0;
        for (int i = 0; i < arr.length; i++) {
            while (!st.isEmpty() && arr[i] < arr[st.peek()]) {
                int height = arr[st.pop()];
                int r = i;
                if (st.isEmpty()) {
                    int area = height * r;
                    ans = Math.max(ans, area);

                } else {
                    int l = st.peek();
                    int area = height * (r - l - 1);
                    ans = Math.max(ans, area);
                }
            }
            st.push(i);
        }
        int r = arr.length;
        while (!st.isEmpty()) {
            int height = arr[st.pop()];
            if (st.isEmpty()) {
                int area = height * r;
                ans = Math.max(ans, area);

            } else {
                int l = st.peek();
                int area = height * (r - l - 1);
                ans = Math.max(ans, area);
            }
        }
        return ans;
    }
}