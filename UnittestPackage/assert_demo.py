"""
https://docs.python.org/3/library/unittest.html#unittest.TestCase

Just follow this link to see how you can add PYTHONPATH to environment variable

Windows:
http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7

Mac:
http://stackoverflow.com/questions/3387695/add-to-python-path-mac-os-x

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