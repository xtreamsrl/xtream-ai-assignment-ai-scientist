"""Base class for all forecasters."""
from __future__ import annotations

from sklearn.base import BaseEstimator, RegressorMixin

__all__ = ["BaseForecaster"]


class BaseForecaster(BaseEstimator, RegressorMixin):  # type: ignore[no-any-unimported]
    """Abstract base class for all forecasters."""

    ...
