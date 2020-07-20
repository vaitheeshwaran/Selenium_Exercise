import pytest
import unittest

# get the password from passWD parameter
@pytest.fixture(scope="session")
def passWD(pytestconfig):
    return pytestconfig.getoption("passWD")

# Test the password and skip only this test case
def test_password(passWD):
    if passWD is None:
        pytest.skip("password is none", allow_module_level=True)
    assert passWD == "admin" # True if password is admin , False if password is wrong

def test_command_line_methodA(OneTimeSetUp, setUp):
    print("Running method A")


def test_command_line_methodB(OneTimeSetUp, setUp):
    print("Running method B")


