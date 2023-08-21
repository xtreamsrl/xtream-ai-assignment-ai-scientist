"""Type aliases."""

from __future__ import annotations

from typing import Literal, TypeAlias

import numpy as np
import numpy.typing as npt

# array types: building blocks for other aliases
IntegerArray: TypeAlias = npt.NDArray[np.integer]
NumericArray: TypeAlias = npt.NDArray[np.number]
IndexArray: TypeAlias = npt.NDArray[np.int32]
DatetimeArray: TypeAlias = npt.NDArray[np.datetime64]

# composite aliases
TrainTestIndices: TypeAlias = tuple[IndexArray, IndexArray]

# arguments to functions
BoundaryCheck: TypeAlias = Literal["neither", "both", "left", "right"]
