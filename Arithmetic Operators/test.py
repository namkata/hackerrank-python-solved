import unittest

class TestCaseRequired(unittest.TestCase):
    def test_result(self):
        a = 6564424525
        b = 323252462
        self.assertEqual(6887676987, a + b)
        self.assertEqual(6241172063, a-b)
        self.assertEqual(2121966389319430550, a*b)

    def test_result_1(self):
        a = 3
        b = 2
        self.assertEqual(5, a + b)
        self.assertEqual(1, a-b)
        self.assertEqual(6, a*b)