import unittest

# Run the unit tests: python -m unittest test.py

class TestCaseRequired(unittest.TestCase):
    def test_result(self):
        a = 4
        b = 3
        self.assertEqual(1, a // b)
        self.assertEqual(1.3333333333333333, a / b)
    
    def test_result_1(self):
        a = 6564424525
        b = 323252462
        self.assertEqual(20, a // b)
        self.assertEqual(20.30742313418173, a / b)