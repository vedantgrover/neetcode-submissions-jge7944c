class Solution {
public:
    bool isAnagram(string s, string t) {
        int sCharCount[26] = {0};
        int tCharCount[26] = {0};

        for (char c : s) {
            sCharCount[c - 'a']++;
        }

        for (char c : t) {
            tCharCount[c - 'a']++;
        }

        for (int i = 0; i < 26; ++i) {
            if (sCharCount[i] != tCharCount[i]) return false;
        }

        return true;
    }
};
