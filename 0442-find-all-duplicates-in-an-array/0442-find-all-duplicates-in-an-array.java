class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> output_arr = new ArrayList();
        printDuplicates(nums,output_arr);
        return(output_arr);
        
    }

    static void printDuplicates(int[] arr,List<Integer> output_arr) 
    { 
        int n = arr.length;
        Arrays.sort(arr); // sort array for binary search 
  
        for (int i = 0; i < n; i++) { 
            // index of first and last occ of arr[i] 
            int firstIndex = lowerBound(arr, arr[i]); 
            int lastIndex = upperBound(arr, arr[i]); 
  
            int occurTime = lastIndex - firstIndex + 1; // frequency of arr[i] 
            
            if (occurTime > 1) { // elements that occur more than 1 
                i = lastIndex; // update i to last_index 
                output_arr.add(arr[i]); 
            } 
        }  
    } 
	
	// Function to find lower bound of target in arr 
    public static int lowerBound(int[] arr, int target) 
    { 
        int lo = 0, hi = arr.length - 1; 
        int ans = -1; 
        while (lo <= hi) { 
            int mid = lo + (hi - lo) / 2; 
            if (arr[mid] >= target) { 
                ans = mid; 
                hi = mid - 1; 
            } 
            else { 
                lo = mid + 1; 
            } 
        } 
        return ans; 
    } 
  
    // Function to find upper bound of target in arr 
    public static int upperBound(int[] arr, int target) 
    { 
        int lo = 0, hi = arr.length - 1; 
        int ans = -1; 
        while (lo <= hi) { 
            int mid = lo + (hi - lo) / 2; 
            if (arr[mid] <= target) { 
                ans = mid; 
                lo = mid + 1; 
            } 
            else { 
                hi = mid - 1; 
            } 
        } 
        return ans; 
    } 
}