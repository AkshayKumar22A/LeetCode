class Solution {
    public int largestAltitude(int[] gain) {
        for(int i=1;i<gain.length;i++) {
            gain[i] = gain[i-1] + gain[i];
        }
        int sol = 0;
        for(int i=0;i<gain.length;i++) {
            if(sol<gain[i]) {
                sol = gain[i];
            }
        }
        return sol;
    }
}