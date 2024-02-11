class Solution {
    public int mySqrt(int x) {
        int ans = (int)findsqrRoot(x);
        return ans;
    }

    public static double findsqrRoot(int n)
    {
        double start = 0;
		double end = n;
		double sol = 0;
        
        while(start<=end)
        {
        	double mid = Math.floor((start + end) / 2);
            if(mid*mid == n)
            {
                return mid;
            }
            else if(mid*mid<n)
            {
                start = mid+1;
                sol= mid;
                System.out.println(sol);
            }
            else if(mid*mid>n)
            {
                end = mid-1;
            }
        }
        return sol;
    }
}