class Solution {
    public int missingNumber(int[] nums) {
        int sol[] = new int[nums.length+1];
        for(int i=0;i<nums.length;i++) {
            sol[nums[i]] +=1;
        }
        int flag=0;
        for(int i=0;i<sol.length;i++) {
            System.out.print(sol[i]+" ");
            if(sol[i]==0) {
                flag = i;
            }
        }
        return flag;
    }
}