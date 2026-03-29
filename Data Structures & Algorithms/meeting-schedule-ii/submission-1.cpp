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
    int minMeetingRooms(vector<Interval>& intervals) {
        vector<int> startTimes;
        vector<int> endTimes;

        for (const Interval& interval : intervals) {
            startTimes.push_back(interval.start);
            endTimes.push_back(interval.end);
        }

        sort(startTimes.begin(), startTimes.end());
        sort(endTimes.begin(), endTimes.end());

        int e = 0, count = 0, res = 0;

        for (int s = 0; s < startTimes.size();) {
            if (startTimes[s] == endTimes[e] || startTimes[s] > endTimes[e]) {
                ++e;
                --count;
            } else {
                ++s;
                ++count;
            }

            res = count > res ? count : res;
        }

        return res;
    }
};
