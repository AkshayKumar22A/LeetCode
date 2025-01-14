class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for(int i=m,j=0;i<nums1.length && j<n;i++,j++) {
            nums1[i] = nums2[j];
        }
        
        for(int i=1;i<nums1.length;i++) {
            int picked = nums1[i];
            int j=i-1;
            while(j>=0 && nums1[j]>picked) {
                nums1[j+1] = nums1[j];
                j--;
            }
            nums1[j+1] = picked;
        }
    }
}