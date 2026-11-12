"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        i = 1
        intervals = sorted(intervals, key=lambda x: x.start)
        while i < len(intervals):
            curr_meeting = intervals[i - 1]
            next_meeting = intervals[i]

            if curr_meeting.end > next_meeting.start:
                return False
            i += 1
        return True