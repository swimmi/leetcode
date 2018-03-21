import unittest

from add_strings import Solution

class TestSolution(unittest.TestCase):

    def test_short_short(self):
        s = Solution();
        num1 = "123"
        num2 = "234"
        self.assertEqual(s.addStrings(num1, num2), '357')
    def test_short_long(self):
        s = Solution();
        num1 = "123"
        num2 = "123141412123131112311231234"
        self.assertEqual(s.addStrings(num1, num2), '357')

if __name__ == '__main__':
    unittest.main()