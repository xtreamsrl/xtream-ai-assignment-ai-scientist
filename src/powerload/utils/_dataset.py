"""Implementation of the `Dataset` class.

The `Dataset` class is the container of objects retrieved via `datasets.fetch_*`
functions.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Generic, TypeVar

import numpy as np
import numpy.typing as npt
import pandas as pd
import polars as pl

if TYPE_CHECKING:
    pass

T = TypeVar(
    "T",
    pl.DataFrame,
    pd.DataFrame,
    tuple[npt.NDArray[np.generic], npt.NDArray[np.generic]],
)


@dataclass
class Dataset(Generic[T]):
    """An object retrieved from a `fetch_*` function in `powerload.datasets`."""

    data: T
    feature_names: list[str]
    target_names: list[str]
    DESCR: str | None = None
