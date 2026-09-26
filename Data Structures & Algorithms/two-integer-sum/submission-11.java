class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> differences = new HashMap<>();
        int result[] = new int[2];

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];

            if (differences.containsKey(diff)) {
                result[0] = Math.min(differences.get(diff), i);
                result[1] = Math.max(differences.get(diff), i);
            } else {
                differences.put(nums[i], i);
            }
        }

        return result;
    }

    private record Pair<K, V>(K key, V value) {}
}
