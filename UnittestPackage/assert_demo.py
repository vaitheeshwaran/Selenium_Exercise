"""
https://docs.python.org/3/library/unittest.html#unittest.TestCase
"""
import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        # We can put error msg
        self.assertTrue(a, "a is not false")
        b = False
        self.assertFalse(b, "b is not true")

    def test_assertEqual(self):
        a = "Test"
        b = "Test"
        self.assertNotEqual(a, b, msg="'a' is equal to 'b'")


if __name__ == '__main__':
    unittest.main(verbosity=2)