"""
file name should start with test
test method name should start with test

py.test test_mod.py   # run tests in module
py.test somepath      # run all tests below somepath
py.test test_module.py::test_method  # only run test_method in test_module

-s to print statements
-v verbose
"""

import pytest
# Decorator After pytest version 2.10, you do not need @pytest.yield_fixture explicitly to use yield. We can use @pytest.fixture() itself work
@pytest.yield_fixture()
def setUp():
    print("Running demo2 setUp")
    yield
    print("Running demo2 tearDown")

def test_demo2_methodA(setUp):
    print("Running demo2 method A")

def test_demo2_methodB(setUp):
    print("Running demo2 method B")