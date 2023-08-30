"""Diagnostic tools."""
from __future__ import annotations

from typing import TYPE_CHECKING

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

if TYPE_CHECKING:
    from powerload.types import DatetimeArray, NumericArray


def plot_predictions(
    y_true: NumericArray,
    y_pred: NumericArray,
    dates: DatetimeArray,
    suptitle: str,
) -> None:
    """Display predictions and residuals diagnostic plots."""
    residuals = y_true - y_pred

    fig = plt.figure(tight_layout=True, figsize=(16, 12))
    grid = gridspec.GridSpec(3, 2)

    fig.suptitle(suptitle)

    ax_preds = fig.add_subplot(grid[0, :])
    ax_residuals = fig.add_subplot(grid[1, :])
    ax_diagnostics_l = fig.add_subplot(grid[2, 0])
    ax_diagnostics_r = fig.add_subplot(grid[2, 1])

    sns.despine(fig)

    # predictions vs residuals
    _ = sns.lineplot(x=dates, y=y_true, alpha=0.8, ax=ax_preds, c="seagreen")
    _ = sns.lineplot(x=dates, y=y_pred, alpha=0.8, ax=ax_preds, c="salmon")
    _ = ax_preds.set(
        title="Actual (green) vs Predicted (red)",
        xlabel=None,
        ylabel=None,
    )

    # plot residuals
    _ = sns.lineplot(x=dates, y=residuals, ax=ax_residuals)
    _ = ax_residuals.set(title="Residuals", xlabel=None, ylabel=None)

    # plot residual diagnostics
    _ = sns.histplot(x=residuals, kde=True, ax=ax_diagnostics_l)
    _ = sm.graphics.tsa.plot_acf(residuals, ax=ax_diagnostics_r, zero=False)

    _ = ax_diagnostics_l.set(title="Residuals distribution", xlabel=None, ylabel=None)
    _ = ax_diagnostics_r.set(
        title="Residuals autocorrelation", xlabel=None, ylabel=None
    )
