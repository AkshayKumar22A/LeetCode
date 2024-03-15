class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
		int LP[] = new int[nums.length];
		LP[0] = 1;
		for(int i=1;i<nums.length;i++) {
			LP[i] = LP[i-1] * nums[i-1];
		}
		
		int RP[] = new int[nums.length];
		RP[nums.length-1] = 1;
		for(int i=nums.length-2;i>=0;i--) {
			RP[i] = RP[i+1] * nums[i+1];
		}
		
		for(int i=0;i<nums.length;i++) {
			LP[i] = LP[i] * RP[i];
		}
		return LP;
    }
}