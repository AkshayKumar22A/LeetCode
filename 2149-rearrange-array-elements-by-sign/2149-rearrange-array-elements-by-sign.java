class Solution {
    public int[] rearrangeArray(int[] nums) {
        int pos[] = new int[nums.length/2];
		int nev[] = new int[nums.length/2];
		int idx1 = 0;
		int idx2 = 0;
		for(int i=0;i<nums.length;i++) {
			if(nums[i] < 0) {
				nev[idx1] = nums[i];
				idx1++;
			}
			if(nums[i]>0) {
				pos[idx2] = nums[i];
				idx2++;
			}
		}
		int idx = 0;
		for(int i=0;i<nums.length/2;i++) {
			nums[idx] = pos[i];
			nums[idx+1] = nev[i];
			idx+=2;
		}
        return nums;
    }
}