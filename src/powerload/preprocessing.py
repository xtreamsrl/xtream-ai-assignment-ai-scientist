"""Preprocessing utilities."""
from __future__ import annotations

from typing import TYPE_CHECKING

import holidays
import polars as pl

if TYPE_CHECKING:
    from typing import Literal

from itertools import chain
from math import pi


def add_time_steps(data: pl.DataFrame) -> pl.DataFrame:
    """Add a time step column."""
    return data.with_columns(pl.int_range(0, len(data), eager=False).alias("time"))


def add_fourier_terms(data: pl.DataFrame, K: int, seasonal_period: int) -> pl.DataFrame:
    """Add Fourier."""
    if K > seasonal_period / 2:
        raise ValueError(
            "The number of Fourier terms K must be smaller or equal to half of the seasonal_period"
        )

    # generate an expression that will be substituted below
    time_index = pl.int_range(0, len(data), eager=False)

    exprs = chain.from_iterable(
        (
            time_index.mul(2)
            .mul(pi)
            .mul(i)
            .truediv(seasonal_period)
            .sin()
            .alias(f"sin_{seasonal_period}_{i}"),
            time_index.mul(2)
            .mul(pi)
            .mul(i)
            .truediv(seasonal_period)
            .cos()
            .alias(f"cos_{seasonal_period}_{i}"),
        )
        for i in range(1, K + 1)
    )

    return data.with_columns(*exprs)


def add_holidays(data: pl.DataFrame, col: str, country: str) -> pl.DataFrame:
    """Add a categorical column for holidays of a given country."""
    min_date, max_date = data[col].dt.year().min(), data[col].dt.year().max()
    years = range(min_date, max_date + 1)  # type: ignore[operator,arg-type]

    calendar = holidays.country_holidays(country, years=years)
    holidays_map = {date: calendar[date] for date in calendar}

    expr = (
        pl.col(col)
        .map_dict(holidays_map)
        .fill_null("No")
        .cast(pl.Categorical)
        .alias("holiday"),
    )

    return data.with_columns(expr)


def add_weekends(data: pl.DataFrame, col: str) -> pl.DataFrame:
    """Add an indicator column that is 1 when the date is a weekend."""
    expr = (
        pl.when(pl.col(col).dt.weekday().is_in((5, 6)))
        .then(1)
        .otherwise(0)
        .alias("is_weekend")
    )
    return data.with_columns(expr)


def add_lagged_terms(
    data: pl.DataFrame, col: str, lags: int | list[int]
) -> pl.DataFrame:
    """Add lagged terms of a column."""
    lags = lags if isinstance(lags, list) else list(range(1, lags + 1))
    return data.with_columns(
        *[pl.col(col).shift(i).alias(f"load_lag_{i}") for i in lags]
    )


def extract_datetime_features(
    data: pl.DataFrame,
    col: str,
    components: list[
        Literal["minute", "hour", "day", "weekday", "week", "month", "quarter", "year"]
    ],
    date: Literal["drop", "keep"] = "keep",
) -> pl.DataFrame:
    """Extract datetime features from a column."""
    exprs = [
        getattr(pl.col(col).dt, component)().alias(component)
        for component in components
    ]

    result = data.with_columns(*exprs)
    if date == "keep":
        return result
    return result.drop(col)
