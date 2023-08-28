"""Utilities."""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
from sklearn.utils import check_scalar

if TYPE_CHECKING:
    from collections.abc import Sized
    from typing import Literal

    import numpy.typing as npt

    from powerload.types import BoundaryCheck

__all__ = [
    "as_2d_array",
    "check_seasonality",
    "check_is_positive_finite",
    "check_is_shorter",
]


def as_2d_array(x: npt.ArrayLike) -> npt.NDArray:
    """Convert an array-like object to a NumPy array with shape (-1, 1)."""
    x_: npt.NDArray = np.asarray(x)
    if x_.ndim == 1:
        return x_.reshape(-1, 1)
    if x_.ndim > 2:
        raise NotImplementedError("Only 1D and 2D arrays are supported.")
    return x_


def check_is_positive_finite(
    x: object,
    *,
    zero: Literal["include", "exclude"] = "exclude",
    name: str,
) -> int:
    """Check if a variable is positive and finite.

    Parameters
    ----------
    x : object
        A scalar array.

    name : str
        The name or description of the variable.

    zero : Literal["include", "exclude"], optional
        A flag indicating whether zero is allowed or excluded in the check.
        "include" means zero is allowed, while "exclude" means zero is not allowed.
        Defaults to "exclude".

    Returns
    -------
    int
        The validated positive finite integer value of the variable.

    Raises
    ------
    ValueError
        If the variable is not a positive finite integer.

    Notes
    -----
    This function checks if the given variable is both positive and finite,
    according to the specified criteria. The variable is considered positive if
    it is greater than zero and finite if it is not infinite.

    Examples
    --------
    >>> check_is_positive_finite(5, "num_elements")
    5

    >>> check_is_positive_finite(0, "num_elements", zero="include")
    0

    >>> check_is_positive_finite(-3, "num_elements")
    ValueError: The variable 'num_elements' must be a positive finite integer.

    >>> check_is_positive_finite(float('inf'), "num_elements")
    ValueError: The variable 'num_elements' must be a positive finite integer.
    """
    boundaries: BoundaryCheck = "left" if zero == "include" else "neither"

    value: int = check_scalar(
        x,
        name=name,
        target_type=int,
        min_val=0,
        max_val=np.inf,
        include_boundaries=boundaries,
    )

    return value


def check_seasonality(
    x: object,
    *,
    y: Sized | None = None,
    name: str,
) -> int:
    """
    Check if a x can represent a seasonal periodicity.

    Parameters
    ----------
    x : object
        A scalar array, representing seasonal periodicity.
    y : array-like, optional
        An optional array of values, used to determine the maximum value of x.
    name : str
        A descriptive name for the value, used by `sklearn.utils.check_scalar`.

    Returns
    -------
    int
        The checked and validated seasonal value.

    Notes
    -----
    This function checks whether the provided value meets certain criteria for
    being a valid seasonal term. The value must be an integer greater than or
    equal to 2. If the optional `y` parameter is provided, the function also
    ensures that the value is less than or equal to the length of `y`.

    Examples
    --------
    >>> check_seasonality(4, name="seasonal_periodicity")
    4

    >>> check_seasonality(1, y=[10, 20, 30, 40], name="seasonal_periodicity")
    Traceback (most recent call last):
        ...
    ValueError: Period must be between 2 and 4 (inclusive).

    """
    if y is None:
        max_val, boundaries = None, "left"
    else:
        max_val, boundaries = len(y), "both"

    value: int = check_scalar(
        x,
        name=name,
        target_type=int,
        min_val=2,
        max_val=max_val,
        include_boundaries=boundaries,
    )

    return value


def check_is_shorter(
    x: object,
    y: Sized | int,
    *,
    name: str,
) -> int:
    """Check if a variable's length is shorter than the length of y.

    Parameters
    ----------
    x : object
        A scalar array.

    y : Sized or int
        The reference length against which the variable's length is compared.
        It can be either an integer or an object that supports the `len()` function.

    name : str
        The name or description of the variable.

    Returns
    -------
    int
        The validated integer value representing the length of the variable.

    Raises
    ------
    ValueError
        If the variable's length is not shorter than the length of y.

    Examples
    --------
    >>> check_is_shorter_than("hello", 10, "string_length")
    5

    >>> check_is_shorter_than([1, 2, 3], [4, 5, 6], "list_length")
    3

    >>> check_is_shorter_than([1, 2, 3], 2, "list_length")
    ValueError: The variable 'list_length' must have a length shorter than 2.

    >>> check_is_shorter_than("hello", 5, "string_length")
    ValueError: The variable 'string_length' must have a length shorter than 5.
    """
    value: int = check_scalar(
        x,
        name=name,
        target_type=int,
        min_val=None,
        max_val=y if isinstance(y, int) else len(y),
        include_boundaries="both",
    )
    return value
