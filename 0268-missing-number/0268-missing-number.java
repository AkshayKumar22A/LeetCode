class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int val=0;
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i=0;i<n;i++)
            arr.add(nums[i]);
        for(int j=0;j<=n;j++)
        {
            if(!arr.contains(j))
               val=j;
        }
        return val;
    }
}