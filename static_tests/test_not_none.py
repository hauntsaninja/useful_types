from __future__ import annotations

from typing import Any
from typing_extensions import assert_type

from useful_types import not_none


def test(x: Any, y: str | None, z: str) -> None:
    assert_type(not_none(x), Any)
    assert_type(not_none(y), str)
    assert_type(not_none(z), str)
