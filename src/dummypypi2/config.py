"""Config file for global variables and settings"""

from __future__ import annotations

RTOL, ATOL = 1E-5, 1E-8

class _NumericalToleranceBase:
    """Base class with shared numerical tolerance setting functionality"""
    
    def _set_tolerance(self, rtol: float, atol: float | None = None) -> None:
        """Set global numerical tolerance values"""
        global RTOL, ATOL
        RTOL = rtol
        if atol is not None:
            ATOL = atol
    
    def _save_current_tolerance(self) -> tuple[float, float]:
        """Save current numerical tolerance values for restoration"""
        return RTOL, ATOL

class NumericalToleranceContextManager(_NumericalToleranceBase):
    """Context manager for temporarily setting numerical tolerance values"""
    
    def __call__(self, rtol: float, atol: float | None = None) -> NumericalToleranceContextManager:
        """Configure tolerance values for context manager use"""
        self._rtol = rtol
        self._atol = atol
        return self

    def __enter__(self) -> NumericalToleranceContextManager:
        """Enter context: save current values and set new ones"""
        self._prev_rtol, self._prev_atol = self._save_current_tolerance()
        self._set_tolerance(self._rtol, self._atol)
        return self

    def __exit__(self, *_) -> None:
        """Exit context: restore previous numerical tolerance values"""
        global RTOL, ATOL
        RTOL, ATOL = self._prev_rtol, self._prev_atol

class NumericalToleranceSetter(_NumericalToleranceBase):
    """Global setter for numerical tolerance values"""
    
    def __call__(self, rtol: float, atol: float | None = None) -> None:
        """Set global numerical tolerance values permanently"""
        self._set_tolerance(rtol, atol)

set_algo_options = NumericalToleranceSetter()
algo_options = NumericalToleranceContextManager()