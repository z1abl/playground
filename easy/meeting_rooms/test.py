import unittest
from .solution import Solution

class TestMeetingRooms(unittest.TestCase):
    def test_meeting_rooms(self):
        solution = Solution()
        canAttendMeetings = solution.canAttendMeetings
        self.assertEqual(canAttendMeetings([]),True)
        self.assertEqual(canAttendMeetings([[0,30],[5,10],[15,20]]),False)
        self.assertEqual(canAttendMeetings([[7,10],[2,4]]), True)
        self.assertEqual(canAttendMeetings([[11,100],[100,102],[200,210]]), True)
        self.assertEqual(canAttendMeetings([[5,10],[1,2],[2,90]]), False)