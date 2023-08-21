"""Dummy forecaster."""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

from powerload.base import BaseForecaster
from powerload.utils import as_2d_array, check_is_positive_finite, check_is_shorter

if TYPE_CHECKING:
    import sys
    from typing import Literal

    import numpy.typing as npt

    from powerload.types import NumericArray

    if sys.version_info < (3, 11):
        from typing_extensions import Self
    else:
        from typing import Self


class NaiveForecaster(BaseForecaster):
    """A naive forecaster that predicts the last value seen."""

    def __init__(
        self,
        strategy: Literal["last"] = "last",
    ) -> None:
        self.strategy: Literal["last"] = strategy
        self.is_fitted: bool = False

    def fit(
        self,
        X: npt.ArrayLike,
        y: npt.ArrayLike | None = None,
    ) -> Self:
        """Fit the naive forecaster."""
        self.window_: NumericArray = as_2d_array(X)[-1]
        self.is_fitted = True
        return self

    def predict(
        self,
        X: npt.ArrayLike,
    ) -> NumericArray:
        """Return predictions."""
        forecasting_horizon: int = len(as_2d_array(X))

        return np.full(forecasting_horizon, self.window_)


class SeasonalNaiveForecaster(BaseForecaster):
    """Forecast based on naive assumptions about past trends continuing."""

    def __init__(self, seasonal_period: int) -> None:
        self.seasonal_period: int = check_is_positive_finite(
            seasonal_period, name="seasonal_period"
        )
        self.is_fitted: bool = False

    def fit(
        self,
        X: npt.ArrayLike,
        y: npt.ArrayLike | None = None,
    ) -> Self:
        """Fit the naive forecaster."""
        n_samples = len(X_ := as_2d_array(X))

        sp = check_is_shorter(self.seasonal_period, n_samples, name="seasonal_period")
        self.window_: NumericArray = X_[-sp:].flatten()
        self.is_fitted = True

        return self

    def predict(
        self,
        X: npt.ArrayLike,
    ) -> NumericArray:
        """Return predictions."""
        if self.seasonal_period == 1:
            return self.window_[-1]  # type: ignore[no-any-return]

        fh: int = len(as_2d_array(X))

        if fh == self.seasonal_period:
            return self.window_

        if fh < self.seasonal_period:
            return self.window_[:fh]

        quotient, remainder = divmod(fh, self.seasonal_period)

        result: NumericArray = np.concatenate(
            (
                np.tile(self.window_.flatten(), quotient),
                self.window_[:remainder].flatten(),
            ),
            axis=0,
        )

        return result
