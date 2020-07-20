import pytest
from PytestModules.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("OneTimeSetUp", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(10) # To get value from conftest file, return 10 if we pass firefox or return 20 if other browser

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        print("Running method B")
