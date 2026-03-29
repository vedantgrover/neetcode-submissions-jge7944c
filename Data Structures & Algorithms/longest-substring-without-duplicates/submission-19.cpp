class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> visitedChars;
        int l = 0;
        int r = 0;

        int res = 0;
        for (; r < s.length(); ++r) {
            while (visitedChars.count(s[r]) > 0) {
                visitedChars.erase(s[l]);
                l++;
            }

            visitedChars.insert(s[r]);
            res = (r - l + 1) > res ? (r - l + 1) : res;
        }

        return res;
    }
};
