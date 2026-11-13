class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        i = 0
        res = []
        while i < len(intervals) - 1:
            curr_interval = intervals[i]
            next_interval = intervals[i + 1]

            if curr_interval[1] >= next_interval[0]:
                if curr_interval[1] < next_interval[1]:
                    intervals[i] = ([curr_interval[0], next_interval[1]])
                intervals.remove(next_interval)
            else:
                i += 1
        return intervals