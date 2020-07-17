import unittest
from UnittestPackage.TestcaseDemo1 import TestCaseDemo1
from UnittestPackage.Testcase2 import TestCaseDemo2

# Get the all testcases from  TestcaseDem1 and Testcase2

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)

# create testsuite for both the testcases class
Reg_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(Reg_test)

