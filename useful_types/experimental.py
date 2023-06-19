from __future__ import annotations

from collections.abc import Callable
from dataclasses import Field
from types import FrameType, TracebackType
from typing import Any, ClassVar, Protocol, Tuple, TypeVar, Union
from typing_extensions import LiteralString, TypeAlias

ExcInfo: TypeAlias = Tuple[type[BaseException], BaseException, TracebackType]
OptExcInfo: TypeAlias = Union[ExcInfo, Tuple[None, None, None]]

# Superset of typing.AnyStr that also includes LiteralString
AnyOrLiteralStr = TypeVar("AnyOrLiteralStr", str, bytes, LiteralString)

# Represents when str or LiteralStr is acceptable. Useful for string processing
# APIs where literalness of return value depends on literalness of inputs
StrOrLiteralStr = TypeVar("StrOrLiteralStr", LiteralString, str)

# Objects suitable to be passed to sys.setprofile, threading.setprofile, and similar
ProfileFunction: TypeAlias = Callable[[FrameType, str, Any], object]

# Objects suitable to be passed to sys.settrace, threading.settrace, and similar
TraceFunction: TypeAlias = Callable[[FrameType, str, Any], Union["TraceFunction", None]]

# Might not work as expected for pyright, see
#   https://github.com/python/typeshed/pull/9362
#   https://github.com/microsoft/pyright/issues/4339
class DataclassInstance(Protocol):
    __dataclass_fields__: ClassVar[dict[str, Field[Any]]]
