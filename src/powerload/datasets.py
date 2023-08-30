"""Dataloading utilities."""

from __future__ import annotations

import os
from pathlib import Path

import polars as pl

__all__ = ["fetch_powerload"]

from typing import TYPE_CHECKING, overload

from powerload.utils import Dataset, as_2d_array

if TYPE_CHECKING:
    from typing import Literal

    import pandas as pd

    from powerload.types import DatetimeArray, NumericArray


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
    data_home: str | Path | None,
    download_if_missing: bool,
    parser: Literal["polars"],
    return_X_y: Literal[True],
) -> pl.DataFrame:
    ...


@overload
def fetch_powerload(
    *,
    data_home: str | Path | None,
    download_if_missing: bool,
    parser: Literal["pandas"],
    return_X_y: Literal[True],
) -> pd.DataFrame:
    ...


@overload
def fetch_powerload(
    *,
    data_home: str | Path | None,
    download_if_missing: bool,
    parser: Literal["numpy"],
    return_X_y: Literal[True],
) -> tuple[DatetimeArray, NumericArray]:
    ...


@overload
def fetch_powerload(
    *,
    data_home: str | Path | None,
    download_if_missing: bool,
    parser: Literal["polars"],
    return_X_y: Literal[False],
) -> Dataset:
    ...


@overload
def fetch_powerload(
    *,
    data_home: str | Path | None,
    download_if_missing: bool,
    parser: Literal["pandas"],
    return_X_y: Literal[False],
) -> Dataset:
    ...


@overload
def fetch_powerload(
    *,
    data_home: str | Path | None,
    download_if_missing: bool,
    parser: Literal["numpy"],
    return_X_y: Literal[False],
) -> Dataset:
    ...


def fetch_powerload(
    *,
    data_home: str | Path | None = None,
    download_if_missing: bool = True,
    parser: Literal["polars", "pandas", "numpy"] = "numpy",
    return_X_y: bool = False,
) -> pl.DataFrame | pd.DataFrame | tuple[DatetimeArray, NumericArray] | Dataset:
    """Load the Italian Powerload dataset.

    Parameters
    ----------
    data_home : str or Path, default=None
        The directory path to use for caching the dataset. Default is
        '~/powerload_data' if `POWERLOAD_DATA` environment variable is not set.

    download_if_missing : bool, default=True
        If True, the dataset will be downloaded from the source URL.

    parser : Literal["pandas", "polars", "numpy"], default="numpy"
        If "polars", the data is returned as a polars DataFrame.
        If "pandas", the data is returned as a pandas DataFrame.
        If "numpy", the data is returned as a tuple of (-1, 1)-shaped numpy arrays.

    Returns
    -------
    data : polars.DataFrame or tuple[DateTimeArray, FloatArray]
        The powerload data. If `parser` is True, a polars DataFrame is returned.
        Otherwise, a tuple of (-1, 1)-shaped numpy arrays:
        - The first array contains dates represented as np.datetime64.
        - The second array contains powerload values represented as np.float64.

    Raises
    ------
    OSError
        If the data is not found locally and `download_if_missing` is False.
    """
    data_home_: Path = _get_data_home(data_home)
    data_home_.mkdir(exist_ok=True)

    dataset: pl.DataFrame

    try:
        dataset = pl.read_csv(
            data_home_ / "powerload.csv",
            dtypes=[pl.Date, pl.Float32],
            new_columns=["date", "load"],
        )
    except FileNotFoundError:
        url: str = "https://raw.githubusercontent.com/xtreamsrl/xtream-ai-assignment/main/datasets/italian-power-load/load.csv"
        dataset = pl.read_csv(
            url,
            dtypes=[pl.Date, pl.Float32],
            new_columns=["date", "load"],
        )

        if download_if_missing:
            dataset.write_csv(data_home_ / "powerload.csv")

    if parser == "polars" and return_X_y:
        return dataset
    if parser == "pandas" and return_X_y:
        return dataset.to_pandas()
    if parser == "numpy" and return_X_y:
        return as_2d_array(dataset["date"]), as_2d_array(dataset["load"])

    if parser == "polars":
        return Dataset(
            data=dataset,
            feature_names=["date"],
            target_names=["load"],
            DESCR="The data represents powerload data in Italy, expressed in GW, at the daily level. Data ranges from 2006-01-01 to 2022-02-07, for a total of 5882 observations.",
        )

    if parser == "pandas":
        return Dataset(
            data=dataset.to_pandas(),
            feature_names=["date"],
            target_names=["load"],
            DESCR="The data represents powerload data in Italy, expressed in GW, at the daily level. Data ranges from 2006-01-01 to 2022-02-07, for a total of 5882 observations.",
        )

    return Dataset(
        data=(as_2d_array(dataset["date"]), as_2d_array(dataset["load"])),
        feature_names=["date"],
        target_names=["load"],
        DESCR="The data represents powerload data in Italy, expressed in GW, at the daily level. Data ranges from 2006-01-01 to 2022-02-07, for a total of 5882 observations.",
    )
