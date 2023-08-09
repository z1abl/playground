# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        if not intervals:
            return True
        for i in range(0,len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True