import unittest
from solved import solution

# Run the unit tests: python -m unittest unittest.py

class TestCaseRequired(unittest.TestCase):
    def test_result(self):
        self.assertEqual("Weird", solution(3))
        self.assertEqual("Not Weird", solution(24))
        self.assertEqual("Not Weird", solution(4))
        self.assertEqual("Weird", solution(18))
        self.assertEqual("Weird", solution(5))
        self.assertEqual("Weird", solution(20))
        self.assertEqual("Not Weird", solution(100))