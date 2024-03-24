class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> output_arr = new ArrayList();
        Arrays.sort(nums);
		for(int i = 1;i<nums.length;i++){
            if(nums[i-1]==nums[i]){
                output_arr.add(nums[i]);  
            }
        }
		return output_arr;
    }
}