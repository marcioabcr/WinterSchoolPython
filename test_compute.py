import pytest
from compute import divide
from compute import multiply

def test_divide():
    x = divide(1,2)
    assert x == pytest.approx(0.5)

def test_multiply():
    assert multiply(2,2) == 4