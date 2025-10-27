class Solution {
    public List<Integer> relocateMarbles(int[] nums, int[] moveFrom, int[] moveTo) {
                final int n = moveFrom.length;
        final Set<Integer> set = new HashSet<>();

        for(final int num : nums)
            set.add(num);

        for(int i = 0; i < n; ++i) {
            set.remove(moveFrom[i]);
            set.add(moveTo[i]);
        }

        final List<Integer> result = new ArrayList<>(set);

        Collections.sort(result);

        return result;
    }
}