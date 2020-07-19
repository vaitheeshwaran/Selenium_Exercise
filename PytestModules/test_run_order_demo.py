"""
http://pytest-ordering.readthedocs.io/en/develop/
"""

import pytest

# B, A, C, E, D, F
@pytest.mark.run(order=2)
def test_run_order_methodA(OneTimeSetUp, setUp):
    print("Running method A")

@pytest.mark.run(order=1)
def test_run_order_methodB(OneTimeSetUp, setUp):
    print("Running method B")

@pytest.mark.run(order=3)
def test_run_order_methodC(OneTimeSetUp, setUp):
    print("Running method C")

@pytest.mark.run(order=5)
def test_run_order_methodD(OneTimeSetUp, setUp):
    print("Running method D")

@pytest.mark.run(order=4)
def test_run_order_methodE(OneTimeSetUp, setUp):
    print("Running method E")

@pytest.mark.run(order=6)
def test_run_order_methodF(OneTimeSetUp, setUp):
    print("Running method F")
