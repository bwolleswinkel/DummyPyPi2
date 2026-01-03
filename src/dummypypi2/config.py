"""Config file for global variables and settings"""

from __future__ import annotations
from typing import Literal

RTOL, ATOL = 1E-5, 1E-8

class _NumericalToleranceBase:
    """Base class with shared numerical tolerance setting functionality"""
    
    def _set_tolerance(self, *, rtol: float | None = None, atol: float | None = None) -> None:
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
    """Context manager for temporarily setting numerical tolerance values.
    
    Call signature: (*, rtol=None, atol=None) -> NumericalToleranceContextManager
    
    Parameters
    ----------
    rtol : float or None, optional
        Relative tolerance value to use within the context.
        If None, the current rtol is unchanged within the context.
    atol : float or None, optional
        Absolute tolerance value to use within the context.
        If None, the current atol is unchanged within the context.
        
    Examples
    --------
    >>> with algo_options(rtol=1E-6, atol=1E-10):
    ...     # Code here uses the specified tolerances
    ...     pass
    >>> # Tolerances are automatically restored after the context
    """
    
    def __call__(self, *, rtol: float | None = None, atol: float | None = None) -> NumericalToleranceContextManager:
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
    """Global setter for numerical tolerance values.
    
    Call signature: (shortcut=None, *, rtol=None, atol=None) -> None
    
    Parameters
    ----------
    shortcut : {'default'} or None, optional
        Shortcut to set predefined tolerance values:
        - 'default': Sets rtol=1E-5, atol=1E-8
        If None, custom tolerances can be set via rtol/atol parameters.
    rtol : float or None, optional
        Relative tolerance value. If None, the current rtol is unchanged.
    atol : float or None, optional
        Absolute tolerance value. If None, the current atol is unchanged.
        
    Examples
    --------
    >>> set_algo_options('default')  # Set to default values
    >>> set_algo_options(rtol=1E-6, atol=1E-10)  # Set custom values
    >>> set_algo_options(rtol=1E-4)  # Only change rtol
    
    """
    
    def __call__(self, shortcut: Literal['default'] | None = None, *_, rtol: float | None = None, atol: float | None = None) -> None:
        """Set global numerical tolerance values permanently"""
        if shortcut is None:
            pass
        elif not isinstance(shortcut, str):
            raise ValueError("'set_algo_options' takes either no positional arguments or a single string argument 'default'. To set custom tolerances, use keyword arguments 'rtol' and/or 'atol'.")
        elif shortcut == 'default':
            self._set_tolerance(rtol=1E-5, atol=1E-8)
        self._set_tolerance(rtol=rtol, atol=atol)

_algo_options_setter = NumericalToleranceSetter()

def set_algo_options(shortcut: Literal['default'] | None = None, /, *, rtol: float | None = None, atol: float | None = None) -> None:
    """Set global numerical tolerance values permanently.

    Parameters
    ----------
    shortcut : {'default'} or None, optional
        Shortcut to set predefined tolerance values:
        - 'default': Sets rtol=1E-5, atol=1E-8
        If None, custom tolerances can be set via rtol/atol parameters.
    rtol : float or None, optional
        Relative tolerance value. If None, the current rtol is unchanged.
    atol : float or None, optional  
        Absolute tolerance value. If None, the current atol is unchanged.

    Examples
    --------
    >>> set_algo_options('default')  # Set to default values
    >>> set_algo_options(rtol=1E-6, atol=1E-10)  # Set custom values
    >>> set_algo_options(rtol=1E-4)  # Only change rtol
    
    """
    return _algo_options_setter(shortcut, rtol=rtol, atol=atol)

_tolerance_context_manager = NumericalToleranceContextManager()

def algo_options(*, rtol: float | None = None, atol: float | None = None) -> NumericalToleranceContextManager:
    """Context manager for temporarily setting numerical tolerance values.

    Parameters
    ----------
    rtol : float or None, optional
        Relative tolerance value to use within the context.
        If None, the current rtol is unchanged within the context.
    atol : float or None, optional
        Absolute tolerance value to use within the context.
        If None, the current atol is unchanged within the context.
        
    Returns
    -------
    NumericalToleranceContextManager
        Context manager that temporarily sets the specified tolerances.

    Examples
    --------
    >>> with algo_options(rtol=1E-6, atol=1E-10):
    ...     # Code here uses the specified tolerances
    ...     pass
    >>> # Tolerances are automatically restored after the context
    
    >>> with algo_options(rtol=1E-4):
    ...     # Only rtol is temporarily changed
    ...     pass
    
    """
    return _tolerance_context_manager(rtol=rtol, atol=atol)


CLR_MATPLOTLIB = ["#1f77b4",  # 0: Blue
                  "#ff7f0e",  # 1: Orange
                  "#2ca02c",  # 2: Green
                  "#d62728",  # 3: Red
                  "#9467bd",  # 4: Purple
                  "#8c564b",  # 5: Brown
                  "#e377c2",  # 6: Pink
                  "#7f7f7f",  # 7: Gray
                  "#bcbd22",  # 8: Olive
                  "#17becf"]  # 9: Cyan


CLR_MATPLOTLIB_LEGACY = ['b', 'g', 'r', 'c', 'm', 'y', 'k']


CLR_TABLEAU_10 = ["#4E79A7",  # 0: Blue
                  "#F28E2B",  # 1: Orange
                  "#E15759",  # 2: Red
                  "#76B7B2",  # 3: Teal
                  "#59A14F",  # 4: Green
                  "#EDC948",  # 5: Yellow
                  "#B07AA1",  # 6: Purple
                  "#FF9DA7",  # 7: Pink
                  "#9C755F",  # 8: Brown
                  "#BAB0AC"]  # 9: Gray


class DisplayOptionsSetter:
    """Global setter for display options.
    
    Call signature: (*, color_cycle=None) -> None
    
    Parameters
    ----------
    color_cycle : {'matplotlib', 'matplotlib_legacy', 'tableau_10'} or None, optional
        Color palette to use for matplotlib plots. Options:
        - 'matplotlib': Default matplotlib color cycle (10 colors)
        - 'matplotlib_legacy': Legacy matplotlib single-letter colors (7 colors)
        - 'tableau_10': Tableau 10 color palette (10 colors)
        If None, no changes are made to the color cycle.
        
    Examples
    --------
    >>> set_display_options(color_cycle='tableau_10')
    >>> set_display_options(color_cycle='matplotlib_legacy')
    
    """
    
    def __call__(self, *, color_cycle: Literal['matplotlib', 'matplotlib_legacy', 'tableau_10'] | None = None) -> None:
        """Set global display options permanently"""
        if color_cycle is not None:
            color_dict = {
                'matplotlib': CLR_MATPLOTLIB,
                'matplotlib_legacy': CLR_MATPLOTLIB_LEGACY,
                'tableau_10': CLR_TABLEAU_10
            }
            try:
                import matplotlib as mpl
                mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=color_dict[color_cycle])
            except ImportError:
                raise ImportWarning("Package 'matplotlib' is not installed. Please install it to use this color palette.")
            

_display_options_setter = DisplayOptionsSetter()

def set_display_options(*, color_cycle: Literal['matplotlib', 'matplotlib_legacy', 'tableau_10'] | None = None) -> None:
    """Set global display options permanently.

    Parameters
    ----------
    color_cycle : {'matplotlib', 'matplotlib_legacy', 'tableau_10'} or None, optional
        Color palette to use for matplotlib plots. Options:
        - 'matplotlib': Default matplotlib color cycle (10 colors)
        - 'matplotlib_legacy': Legacy matplotlib single-letter colors (7 colors)  
        - 'tableau_10': Tableau 10 color palette (10 colors)
        If None, no changes are made to the color cycle.
        
    Raises
    ------
    ImportWarning
        If matplotlib is not installed when trying to set a color cycle.

    Examples
    --------
    >>> set_display_options(color_cycle='tableau_10')
    >>> set_display_options(color_cycle='matplotlib_legacy')
    
    """
    return _display_options_setter(color_cycle=color_cycle)