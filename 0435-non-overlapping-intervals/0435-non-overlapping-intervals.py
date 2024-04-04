class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count, res = 0, []
        for i in range(len(intervals)):
            if res and intervals[i][0] < res[-1][1]:
                count +=1
                res[-1][1] = min(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        return count
        