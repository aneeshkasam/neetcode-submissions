"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        first = []
        second = []
        rooms = 0
        for interval in intervals:
            first.append(interval.start)
            second.append(interval.end)
        first = sorted(first)
        second = sorted(second)

        first_pointer = 0
        second_pointer = 0
        while (first_pointer < len(first)) and (second_pointer < len(second)):
            if first[first_pointer] < second[second_pointer]:
                rooms += 1
                first_pointer += 1
            else:
                first_pointer += 1
                second_pointer += 1
        return rooms
            
