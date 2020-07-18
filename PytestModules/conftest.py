import pytest
"""
file name should start with test
test method name should start with test

py.test test_mod.py   # run tests in module
py.test somepath      # run all tests below somepath
py.test test_module.py::test_method  # only run test_method in test_module

-s to print statements
-v verbose
"""

# Decorator After pytest version 2.10, you do not need @pytest.yield_fixture explicitly to use yield. We can use @pytest.fixture() itself work

@pytest.fixture()
def setUp():
    print("\nRunning conftest demo1 setUp")
    yield
    print("\nRunning conftest After execution")

@pytest.fixture(scope="package") # Scope we can assing module level(each file level)
def OneTimeSetUp():
    print("\nRunning One time conftest demo1 setUp")
    yield
    print("\nRunning One time conftest After execution")