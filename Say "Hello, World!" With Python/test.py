import unittest

class TestCaseRequired(unittest.TestCase):
    def test_result(self):
        my_str = "Hello, World!"
        self.assertEqual(my_str, "Hello, World!")