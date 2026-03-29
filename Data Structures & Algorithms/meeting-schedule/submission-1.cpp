/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        vector<int> startValues(intervals.size());
        vector<int> endValues(intervals.size());

        sort(intervals.begin(), intervals.end(), [](const Interval &a, const Interval &b) {
            return a.start < b.start;
        });

        for (int i = 0; i < intervals.size(); ++i) {
            startValues[i] = intervals[i].start;
            endValues[i] = intervals[i].end;
        }

        for (int i = 1; i < startValues.size(); ++i) {
            if (startValues[i] < endValues[i - 1]) return false;
        }

        return true;
    }
};
