class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
		Arrays.sort(nums2);
		ArrayList<Integer> list = new ArrayList<>();
		
		int i=0, j=0, idx=0;
		
		while(i<nums1.length && j<nums2.length) {
			if(nums1[i]<nums2[j]) {
				i++;
			} else if (nums1[i]>nums2[j]){
				j++;
			} else {
				if(list.contains(nums1[i])) {
                    i++;
                    j++;
					continue;
				} else {
					list.add(nums1[i]);
				}
				i++;
				j++;
			}
		}
		int[] sol = list.stream().mapToInt(Integer::intValue).toArray();
        return sol;

    }
}