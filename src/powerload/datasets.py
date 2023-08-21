"""Dataloading utilities."""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np
import polars as pl

__all__ = ["fetch_powerload"]

from typing import TYPE_CHECKING, overload

if TYPE_CHECKING:
    from typing import Literal, TypeAlias

    import numpy.typing as npt

    DateLoadNDArrayTuple: TypeAlias = tuple[
        npt.NDArray[np.datetime64], npt.NDArray[np.float64]
    ]


def _get_data_home(data_home: str | Path | None = None) -> Path:
    if data_home is None:
        data_home_var = os.environ.get("POWERLOAD_DATA", "~/powerload_data")
        return Path(data_home_var).expanduser()
    if isinstance(data_home, str):
        return Path(data_home).expanduser()
    return data_home.expanduser()


@overload
def fetch_powerload(
    *,
    data_home: str | Path | None = None,
    download_if_missing: bool = True,
    as_frame: Literal[True],
) -> pl.DataFrame:
    ...


@overload
def fetch_powerload(
    *,
    data_home: str | Path | None = None,
    download_if_missing: bool = True,
    as_frame: Literal[False] = False,
) -> DateLoadNDArrayTuple:
    ...


def fetch_powerload(
    *,
    data_home: str | Path | None = None,
    download_if_missing: bool = True,
    as_frame: bool = False,
) -> pl.DataFrame | DateLoadNDArrayTuple:
    """Load the Italian Powerload dataset.

    Parameters
    ----------
    data_home : str or Path, default=None
        The directory path to use for caching the dataset. The default is
        '~/powerload_data', where the data is stored in subfolders.

    download_if_missing : bool, default=True
        If False, an OSError will be raised if the dataset is not available
        locally, instead of attempting to download it from the source site.

    as_frame : bool, default=False
        If True, the data is returned as a polars DataFrame with columns
        having appropriate data types (numeric, string, or categorical).
        The target is a polars DataFrame or Series depending on the number
        of target_columns.

    Returns
    -------
    data : pl.DataFrame or tuple[np.ndarray[np.datetime64], np.ndarray[np.float64]]
        The powerload data. If `as_frame` is True, a polars DataFrame is returned.
        Otherwise, a tuple containing two numpy arrays is returned:
        - The first array contains dates represented as np.datetime64.
        - The second array contains powerload values represented as np.float64.

    Raises
    ------
    OSError
        If the data is not found locally and `download_if_missing` is False.
    """
    data_home_: Path = _get_data_home(data_home)
    data_home_.mkdir(exist_ok=True)

    data: pl.DataFrame

    try:
        data = pl.read_csv(
            data_home_ / "powerload.csv",
            dtypes=[pl.Date, pl.Float32],
            new_columns=["date", "load"],
        )
    except FileNotFoundError as e:
        if not download_if_missing:
            raise OSError("Data not found and `download_if_missing` is False") from e

        url: str = "https://raw.githubusercontent.com/xtreamsrl/xtream-ai-assignment/main/datasets/italian-power-load/load.csv"
        data = pl.read_csv(
            url,
            dtypes=[pl.Date, pl.Float32],
            new_columns=["date", "load"],
        )

        data.write_csv(data_home_ / "powerload.csv")

    if as_frame:
        return data
    return np.array(data["date"]), data["load"].to_numpy()
