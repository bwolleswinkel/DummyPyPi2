import pytest
import numpy as np

import dymmypypi2 as dp

pytestmark = pytest.mark.utils

def test_get_signed_angle():
    a = [1, 0]
    b = [0, 1]
    look = [0, 0, 1]

    theta = dp.get_signed_angle(b, a, look=look)

    assert pytest.approx(theta, 0.0001) == np.pi / 2