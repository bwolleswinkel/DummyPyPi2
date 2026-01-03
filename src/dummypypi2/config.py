"""Config file for global variables and settings"""

from __future__ import annotations

RTOL, ATOL = 1E-5, 1E-8

class Tolerance:
    def __call__(self, rtol: float, atol: float | None = None) -> Tolerance:
        global RTOL, ATOL
        self._prev_rtol, self._prev_atol = RTOL, ATOL  # NOTE: This is necessary for context manager use, as the `with` statement calls __call__ first (which is unwanted, and thus needs to be mitigated by storing the 'true' globals before this call is made).
        RTOL = rtol
        if atol is not None:
            ATOL = atol
        self._rtol, self._atol = rtol, atol  # Store for context manager use
        return self

    def __enter__(self) -> Tolerance:
        global RTOL, ATOL
        RTOL = self._rtol
        if self._atol is not None:
            ATOL = self._atol
        return self

    def __exit__(self, *_) -> None:
        global RTOL, ATOL
        RTOL, ATOL = self._prev_rtol, self._prev_atol

set_tol = Tolerance()