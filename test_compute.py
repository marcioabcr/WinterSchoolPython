import pytest
import numpy as np
from numpy import allclose

from compute import divide
from compute import multiply

def test_divide():
    x = divide(1,2)
    assert x == pytest.approx(0.5)

def test_divide_array():
    a = np.array([1,1,1])
    b = np.array([2,2,2])
    x = divide(a,b)
    assert_allclose(x, np.array([0.5,0.5,0.5]))

def test_divide_zero():
    assert np.isinf(divide(1,0))

def test_multiply():
    assert multiply(2,2) == 4