"""Model selection utilities."""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

from powerload.utils import as_2d_array, check_is_positive_finite, check_is_shorter

if TYPE_CHECKING:
    from collections.abc import Iterator
    from typing import Literal

    import numpy.typing as npt

    from powerload.types import TrainTestIndices


class TimeSeriesCrossValidation:
    """Yields train/test indices to run time series cross-validation.

    This class provides functionality to generate train/test indices for time series
    cross-validation. The indices are generated based on the specified train size,
    test size, and gap between consecutive windows. The `strategy` parameter determines
    whether the windows are expanding or rolling.

    Parameters
    ----------
    train_size : int
        The size of the training window for each fold.

    forecasting_horizon : int
        The length of the predictions for each fold.

    stride : int, optional
        The stride between consecutive windows. If None, defaults to the forecasting
        horizon. Defaults to None.

    gap : int, optional
        The gap between consecutive windows. Defaults to 0.

    strategy : Literal["expanding", "rolling"], optional
        The strategy for generating the train/test indices. "expanding" means each
        testing window includes all data up to the current window, while "rolling"
        means each testing window moves forward with the specified test size.
        Defaults to "rolling".

    Attributes
    ----------
    train_size : int
        The size of the training window for each fold.

    test_size : int
        The size of the testing window for each fold.

    gap : int
        The gap between consecutive windows.

    strategy : "expanding" or "rolling"
        The strategy for generating the train/test indices. If "rolling", the training
        window moves forward with the specified stride. If "expanding", the training
        window includes all data up to the current window.

    Methods
    -------
    split(
        X: None = None,
        y: np.ndarray,
        groups: None = None
    ) -> Iterator[TrainTestIndices]:
        Yield train/test indices for time series cross-validation.

    get_n_splits(
        X: None = None,
        y: np.ndarray,
        groups: None = None
    ) -> int:
        Return the number of splits for time series cross-validation.

    Examples
    --------
    >>> cv = TimeSeriesCrossValidation(train_size=3, forecasting_horizon=2, gap=1, strategy="rolling")
    >>> y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> for train_idx, test_idx in cv.split(X=y):
    ...     print("Train:", train_idx, "Test:", test_idx)
    ...
    Train: [0 1 2] Test: [4 5]
    Train: [2 3 4] Test: [6 7]
    Train: [4 5 6] Test: [8 9]

    >>> cv = TimeSeriesCrossValidation(train_size=3, forecasting_horizon=2, stride=1, strategy="rolling")
    >>> y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> for train_idx, test_idx in cv.split(X=y):
    ...     print("Train:", train_idx, "Test:", test_idx)
    ...
    Train: [0 1 2] Test: [3 4]
    Train: [1 2 3] Test: [4 5]
    Train: [2 3 4] Test: [5 6]
    Train: [3 4 5] Test: [6 7]
    Train: [4 5 6] Test: [7 8]
    Train: [5 6 7] Test: [8 9]
    """  # noqa: W505

    def __init__(
        self,
        train_size: int,
        forecasting_horizon: int,
        stride: int | None = None,
        gap: int = 0,
        strategy: Literal["expanding", "rolling"] = "rolling",
    ) -> None:
        self.train_size = check_is_positive_finite(train_size, name="train_size")
        self.forecasting_horizon = check_is_positive_finite(
            forecasting_horizon, zero="exclude", name="forecasting_horizon"
        )
        self.gap = check_is_positive_finite(gap, zero="include", name="gap")

        if stride is None:
            self.stride = self.forecasting_horizon
        else:
            self.stride = check_is_positive_finite(
                stride, zero="include", name="stride"
            )
        self.strategy = strategy

    def split(
        self,
        X: npt.ArrayLike,
        y: npt.ArrayLike | None = None,
        groups: None = None,
    ) -> Iterator[TrainTestIndices]:
        """Yield train/test indices for time series cross-validation.

        Parameters
        ----------
        X : ArrayLike
            The target variable. Named `X` for compatibility purposes.

        y : None, optional
            This parameter is present for compatibility purposes but is not used.
            Defaults to None.

        groups : None, optional
            This parameter is present for compatibility purposes but is not used.
            Defaults to None.

        Yields
        ------
        TrainTestIndices
            Tuple of `numpy.ndarray`s of the train/test indices in each fold.
        """
        n_samples = len(as_2d_array(X))

        train_size = check_is_shorter(self.train_size, n_samples, name="train_size")
        fh = check_is_shorter(
            self.forecasting_horizon, n_samples, name="forecasting_horizon"
        )
        stride = check_is_shorter(self.stride, n_samples, name="stride")
        gap = check_is_shorter(self.gap, n_samples, name="gap")

        indices = np.arange(n_samples)

        train_start, train_end = 0, train_size
        test_start, test_end = train_end + gap, train_end + gap + fh
        yield indices[train_start:train_end], indices[test_start:test_end]

        while test_end < n_samples:
            if self.strategy == "rolling":
                train_start += stride
            train_end += stride
            test_start += stride
            test_end += stride

            yield indices[train_start:train_end], indices[test_start:test_end]

    def get_n_splits(
        self,
        X: npt.ArrayLike,
        y: None = None,
        groups: None = None,
    ) -> int:
        """Return the number of splits for time series cross-validation.

        Parameters
        ----------
        X : np.ndarray
            The target variable. Named `X` for compatibility purposes.

        y : None, optional
            This parameter is present for compatibility purposes but is not used.
            Defaults to None.

        groups : None, optional
            This parameter is present for compatibility purposes but is not used.
            Defaults to None.

        Returns
        -------
        int
            The number of splits (folds) that will be generated during cross-validation.
        """
        n_samples = len(as_2d_array(X))

        train_size = check_is_shorter(self.train_size, n_samples, name="train_size")
        stride = check_is_shorter(self.stride, n_samples, name="stride")
        gap = check_is_shorter(self.gap, n_samples, name="gap")
        fh = check_is_shorter(
            self.forecasting_horizon, n_samples, name="forecasting_horizon"
        )

        quotient, remainder = divmod(n_samples - (train_size + gap + fh), stride)

        if remainder > 0:
            return quotient + 2
        return quotient + 1
