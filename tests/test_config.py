"""Tests for global configuration of variables, algorithms, solvers, and display settings"""

import pytest

import dummypypi2 as dp


def test_set_algo_options():
    # Test resetting to default
    dp.set_algo_options('default')
    assert dp._config._algo.RTOL == 1E-5 and dp._config._algo.ATOL == 1E-8, "RTOL and ATOL should be set to 1E-5 and 1E-8 by default, respectively"

    # Test closeness with default tolerances
    a, delta = 0.1, 1E-5; b = a + delta
    assert not dp.is_close(a, b), "The default tolerances (ATOL=1E-8, RTOL=1E-5) should not consider a and b close"

    # Test setting custom tolerances
    dp.set_algo_options(atol=1E-3)
    assert dp._config._algo.RTOL == 1E-5 and dp._config._algo.ATOL == 1E-3, "RTOL and ATOL should be set by the global setter to 1E-5 and 1E-3, respectively"
    
    # Test closeness with updated tolerances
    assert dp.is_close(a, b), "With ATOL=1E-3, a and b should be considered close"


def test_algo_options_context_manager():
    # FROM: https://stackoverflow.com/questions/39896716/can-i-perform-multiple-assertions-in-pytest  # nopep8
    errors = []

    import dummypypi2._config.algo as cfg
    dp.set_algo_options('default')  # FIXME: This does not work, because the previous test modified the global state... so we need to either modify the order, or reset the state here
    if not (cfg.RTOL == 1E-5 and cfg.ATOL == 1E-8):
        errors.append("RTOL and ATOL should be set to 1E-5 and 1E-8 by default, respectively")
    a, delta = 0.1, 1E-5; b = a + delta
    if dp.is_close(a, b):
        errors.append("With RTOL=1E-5 and ATOL=1E-8, a and b should not be considered close")
    with dp.algo_options(atol=1E-3):
        if not dp.is_close(a, b):
            errors.append("Within context manager with ATOL=1E-3, a and b should be considered close")
    if dp.is_close(a, b):
        errors.append("Outside context manager, a and b should not be considered close anymore")

    assert not errors, "errors occurred:\n{}".format("\n".join(errors))