class Solution {
    public int minimumDeletions(int[] nums) {
        int min = Integer.MAX_VALUE; int minidx = 0;
		int max = Integer.MIN_VALUE; int maxidx = 0;

		for(int i=0;i<nums.length;i++) {
			if(nums[i] < min) {
				min = nums[i];
				minidx = i;
			}
			if(nums[i]>max) {
				max = nums[i];
				maxidx = i;
			}
		}
		if(maxidx==minidx){
	            return Math.min(maxidx+1,nums.length-maxidx);
	    }
		if(maxidx>minidx){
	        int count = Math.min(maxidx+1,nums.length-minidx); 
            int count1 = minidx+1+(nums.length-maxidx); 
            return Math.min(count,count1);
	    } else{
	        int count = Math.min(minidx+1,nums.length-maxidx);
            int count1 = maxidx+1+(nums.length-minidx);
            return Math.min(count,count1);
	    }
    }
}