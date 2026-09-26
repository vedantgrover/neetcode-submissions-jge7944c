class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        HashMap<String, List<String>> freqMaps = new HashMap<>();

        for (String s : strs) {
            int[] freq = new int[26];

            for (char c : s.toCharArray()) {
                freq[c - 'a']++;
            }

            String freqStr = Arrays.toString(freq);

            if (freqMaps.containsKey(freqStr)) {
                freqMaps.get(freqStr).add(s);
            } else {
                freqMaps.put(freqStr, new ArrayList<>());
                freqMaps.get(freqStr).add(s);
            }
        }

        for (List<String> vals : freqMaps.values()) {
            result.add(vals);
        }

        return result;
    }
}
