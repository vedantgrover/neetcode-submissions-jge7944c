class Solution {
    /*
        
    */
    public int longestConsecutive(int[] nums) {
        Set<Integer> numbSet = Arrays.stream(nums).boxed().collect(Collectors.toSet());

        int maxCount = 0;
        for (int n : nums) {
            int count = 0;
            if (!numbSet.contains(n - 1)) {
                count = 1;
                int cur = n;
                while (numbSet.contains(cur + 1)) {
                    count++;
                    cur++;
                }
                maxCount = Math.max(count, maxCount);
            }
        }

        return maxCount;
    }
}
