class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> seenNumbers;

        for (int n : nums) {
            int currentSetSize = seenNumbers.size();
            seenNumbers.insert(n);
            if (currentSetSize == seenNumbers.size()) return true;
        }

        return false;
    }
};