class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numbSet = Arrays.stream(nums).boxed().collect(Collectors.toSet());

        int maxCount = 0;
        for (int n : nums) {
            if (!numbSet.contains(n - 1)) {
                int count = 1;
                int curr = n;
                while (numbSet.contains(curr + 1)) {
                    count++;
                    curr += 1;
                }
                maxCount = Math.max(maxCount, count);
            }
        }

        return maxCount;
    }
}
