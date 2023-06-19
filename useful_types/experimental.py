from __future__ import annotations

import abc
from dataclasses import Field, dataclass, is_dataclass
from types import FrameType, TracebackType
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    Protocol,
    Tuple,
    Type,
    TypeVar,
    Union,
    final,
    runtime_checkable,
)
from typing_extensions import LiteralString, TypeAlias

ExcInfo: TypeAlias = Tuple[Type[BaseException], BaseException, TracebackType]
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

if TYPE_CHECKING:
    # Might not work as expected for pyright, see
    #   https://github.com/python/typeshed/pull/9362
    #   https://github.com/microsoft/pyright/issues/4339
    #
    # The type ignore is to workaround a mypy complaint:
    # Final class useful_types.experimental.DataclassLike has abstract attributes "__dataclass_fields__"
    @final
    @runtime_checkable
    class DataclassLike(Protocol):  # type: ignore[misc]
        __dataclass_fields__: ClassVar[dict[str, Field[Any]]]

else:
    @dataclass(init=False, repr=False, eq=False)
    class DataclassLike(metaclass=abc.ABCMeta):
        """Abstract base class for all dataclass types.

        Mainly useful for type-checking.
        """

        def __init_subclass__(cls):
            raise TypeError(
                "Use the @dataclass decorator to create dataclasses, "
                "rather than subclassing dataclasses.DataclassLike"
            )
        def __new__(cls):
            raise TypeError(
                "dataclasses.DataclassLike is an abstract class that cannot be instantiated"
            )
        __subclasshook__ = is_dataclass
