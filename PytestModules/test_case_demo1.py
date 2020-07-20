import pytest
from PytestModules.class_to_test import SomeClassToTest


# To access fixture for entire class
@pytest.mark.usefixtures("OneTimeSetUp", "setUp")
class TestClassDemo():
    # To use this object to remaining methods ( autouse method )
    @pytest.fixture(autouse=True)
    def classSetup(self):
        # create a object for SomeClassTest and pass 10 value
        self.abc = SomeClassToTest(10)

    def test_sum(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running conftest method sum of the numbers")

    def test_demo1_methodB(self):
        print("Running conftest demo1 method B")
