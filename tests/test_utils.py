import pytest
import numpy as np

import dummypypi2 as dp


def test_get_signed_angle():
    a, b = np.array([1, 0]), np.array([0, 1])
    look = np.array([0, 0, 1])
    assert np.degrees(dp.get_signed_angle(a, b, look=look)) == pytest.approx(90)
    assert np.degrees(dp.get_signed_angle(a, b, np.cross(a, b))) == pytest.approx(90)
    

def test_divide():
    assert dp.divide(4, 2) == 2.0, "4 divided by 2 should be 2"
    with pytest.raises(ValueError):
        dp.divide(1, 0)