class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] result = new int[k];
        HashMap<Integer, Integer> freq = new HashMap<>();

        for (int n : nums) {
            if (freq.containsKey(n)) {
                freq.put(n, freq.get(n) + 1);
            } else {
                freq.put(n, 1);
            }
        }

        PriorityQueue<Pair<Integer, Integer>> maxHeap = new PriorityQueue<>((a, b) -> b.value - a.value);
        for (int key : freq.keySet()) {
            maxHeap.add(new Pair(key, freq.get(key)));
        }

        for (int i = 0; i < k; i++) {
            result[i] = maxHeap.poll().key;
        }
        
        return result;
    }

    private record Pair<K, V>(K key, V value) {}
}
