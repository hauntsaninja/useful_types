from __future__ import annotations
from typing import Sequence, TypeVar
from useful_types import SequenceNotStr

T = TypeVar("T")


def takes_sequence(x: Sequence[T]) -> T:
    return next(iter(x))


def takes_sequence_not_str(x: SequenceNotStr[T]) -> T:
    return next(iter(x))


takes_sequence_not_str("abc")  # type: ignore
takes_sequence("abc")

_1: int = takes_sequence_not_str([1, 2, 3])
_2: int = takes_sequence([1, 2, 3])

_3: int = takes_sequence_not_str((1, 2, 3))
_4: int = takes_sequence((1, 2, 3))

_5: str = takes_sequence_not_str(["a", "b", "c"])
_6: str = takes_sequence(["a", "b", "c"])

_7: str = takes_sequence_not_str(("a", "b", "c"))
_8: str = takes_sequence(("a", "b", "c"))

takes_sequence_not_str(iter([1, 2, 3]))  # type: ignore
takes_sequence(iter([1, 2, 3]))  # type: ignore
