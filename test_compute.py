import pytest
import numpy as np
from compute import divide
from compute import multiply

def test_divide():
    x = divide(1,2)
    assert x == pytest.approx(0.5)

def test_divide_zero():
    assert np.isinf(divide(1,0))

def test_multiply():
    assert multiply(2,2) == 4