class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seenNums = new HashSet<>();
        
        for (int n : nums) {
            seenNums.add(n);
        }

        return nums.length != seenNums.size();
    }
}