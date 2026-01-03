"""Config file for global variables and settings"""

from __future__ import annotations
from typing import Literal

RTOL, ATOL = 1E-5, 1E-8

class _NumericalToleranceBase:
    """Base class with shared numerical tolerance setting functionality"""
    
    def _set_tolerance(self, *_, rtol: float | None = None, atol: float | None = None) -> None:
        """Set global numerical tolerance values"""
        global RTOL, ATOL
        if rtol is not None:
            RTOL = rtol
        if atol is not None:
            ATOL = atol
    
    def _save_current_tolerance(self) -> tuple[float, float]:
        """Save current numerical tolerance values for restoration"""
        return RTOL, ATOL

class NumericalToleranceContextManager(_NumericalToleranceBase):
    """Context manager for temporarily setting numerical tolerance values"""
    
    def __call__(self, *_, rtol: float | None = None, atol: float | None = None) -> NumericalToleranceContextManager:
        """Configure tolerance values for context manager use"""
        self._rtol = rtol
        self._atol = atol
        return self

    def __enter__(self) -> NumericalToleranceContextManager:
        """Enter context: save current values and set new ones"""
        self._prev_rtol, self._prev_atol = self._save_current_tolerance()
        self._set_tolerance(rtol=self._rtol, atol=self._atol)
        return self

    def __exit__(self, *_) -> None:
        """Exit context: restore previous numerical tolerance values"""
        global RTOL, ATOL
        RTOL, ATOL = self._prev_rtol, self._prev_atol

class NumericalToleranceSetter(_NumericalToleranceBase):
    """Global setter for numerical tolerance values"""
    
    def __call__(self, shortcut: Literal['default'] | None = None, *_, rtol: float | None = None, atol: float | None = None) -> None:
        """Set global numerical tolerance values permanently"""
        if shortcut is None:
            pass
        elif not isinstance(shortcut, str):
            raise ValueError("'set_algo_options' takes either no positional arguments or a single string argument 'default'. To set custom tolerances, use keyword arguments 'rtol' and/or 'atol'.")
        elif shortcut == 'default':
            self._set_tolerance(rtol=1E-5, atol=1E-8)
        self._set_tolerance(rtol=rtol, atol=atol)

set_algo_options = NumericalToleranceSetter()
algo_options = NumericalToleranceContextManager()