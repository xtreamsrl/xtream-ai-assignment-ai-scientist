"""Implementation of the `Dataset` class.

The `Dataset` class is the container of objects retrieved via `datasets.fetch_*`
functions.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Generic, TypeVar

import numpy as np
import pandas as pd
import polars as pl

if TYPE_CHECKING:
    import numpy.typing as npt

_T = TypeVar("_T", np.datetime64, np.integer, np.float64)


@dataclass
class Dataset(Generic[_T]):
    """An object retrieved from a `fetch_*` function in `powerload.datasets`."""

    data: pl.DataFrame | pd.DataFrame | tuple[npt.NDArray[_T], npt.NDArray[_T]]
    feature_names: list[str]
    target_names: list[str]
    DESCR: str | None = None
