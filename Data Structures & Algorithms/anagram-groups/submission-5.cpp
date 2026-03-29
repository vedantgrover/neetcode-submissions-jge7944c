class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;

        for (const string& str : strs) {
            int strCount[26] = {0};
            for (char c : str) {
                strCount[c - 'a']++;
            }

            string key = "";

            for (int n : strCount) key += to_string(n) + ", ";

            if (groups.count(key) > 0) {
                groups[key].push_back(str);
            } else {
                groups[key] = {str};
            }
        }

        vector<vector<string>> res;

        for (const auto& pair : groups) {
            res.push_back(pair.second);
        }

        return res;
    }
};
