from __future__ import annotations

from collections.abc import Awaitable, Iterable, Sequence, Set as AbstractSet, Sized
from os import PathLike
from typing import Any, TypeVar, Union, overload
from typing_extensions import Buffer, Literal, Protocol, TypeAlias

_KT = TypeVar("_KT")
_KT_co = TypeVar("_KT_co", covariant=True)
_KT_contra = TypeVar("_KT_contra", contravariant=True)
_VT = TypeVar("_VT")
_VT_co = TypeVar("_VT_co", covariant=True)
_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)

# For partially known annotations. Usually, fields where type annotations
# haven't been added are left unannotated, but in some situations this
# isn't possible or a type is already partially known. In cases like these,
# use Incomplete instead of Any as a marker. For example, use
# "Incomplete | None" instead of "Any | None".
Incomplete: TypeAlias = Any


class IdentityFunction(Protocol):
    def __call__(self, __x: _T) -> _T:
        ...


# ====================
# Comparison protocols
# ====================


class SupportsDunderLT(Protocol[_T_contra]):
    def __lt__(self, __other: _T_contra) -> bool:
        ...


class SupportsDunderGT(Protocol[_T_contra]):
    def __gt__(self, __other: _T_contra) -> bool:
        ...


class SupportsDunderLE(Protocol[_T_contra]):
    def __le__(self, __other: _T_contra) -> bool:
        ...


class SupportsDunderGE(Protocol[_T_contra]):
    def __ge__(self, __other: _T_contra) -> bool:
        ...


class SupportsAllComparisons(
    SupportsDunderLT[Any],
    SupportsDunderGT[Any],
    SupportsDunderLE[Any],
    SupportsDunderGE[Any],
    Protocol,
):
    ...


SupportsRichComparison: TypeAlias = Union[SupportsDunderLT[Any], SupportsDunderGT[Any]]
SupportsRichComparisonT = TypeVar("SupportsRichComparisonT", bound=SupportsRichComparison)

# ====================
# Dunder protocols
# ====================


class SupportsNext(Protocol[_T_co]):
    def __next__(self) -> _T_co:
        ...


class SupportsAnext(Protocol[_T_co]):
    def __anext__(self) -> Awaitable[_T_co]:
        ...


class SupportsAdd(Protocol[_T_contra, _T_co]):
    def __add__(self, __x: _T_contra) -> _T_co:
        ...


class SupportsRAdd(Protocol[_T_contra, _T_co]):
    def __radd__(self, __x: _T_contra) -> _T_co:
        ...


class SupportsSub(Protocol[_T_contra, _T_co]):
    def __sub__(self, __x: _T_contra) -> _T_co:
        ...


class SupportsRSub(Protocol[_T_contra, _T_co]):
    def __rsub__(self, __x: _T_contra) -> _T_co:
        ...


class SupportsDivMod(Protocol[_T_contra, _T_co]):
    def __divmod__(self, __other: _T_contra) -> _T_co:
        ...


class SupportsRDivMod(Protocol[_T_contra, _T_co]):
    def __rdivmod__(self, __other: _T_contra) -> _T_co:
        ...


# This protocol is generic over the iterator type, while Iterable is
# generic over the type that is iterated over.
class SupportsIter(Protocol[_T_co]):
    def __iter__(self) -> _T_co:
        ...


# This protocol is generic over the iterator type, while AsyncIterable is
# generic over the type that is iterated over.
class SupportsAiter(Protocol[_T_co]):
    def __aiter__(self) -> _T_co:
        ...


class SupportsLenAndGetItem(Protocol[_T_co]):
    def __len__(self) -> int:
        ...

    def __getitem__(self, __k: int) -> _T_co:
        ...


class SupportsTrunc(Protocol):
    def __trunc__(self) -> int:
        ...


# ====================
# Mapping-like protocols
# ====================


class SupportsItems(Protocol[_KT_co, _VT_co]):
    def items(self) -> AbstractSet[tuple[_KT_co, _VT_co]]:
        ...


class SupportsKeysAndGetItem(Protocol[_KT, _VT_co]):
    def keys(self) -> Iterable[_KT]:
        ...

    def __getitem__(self, __key: _KT) -> _VT_co:
        ...


class SupportsGetItem(Protocol[_KT_contra, _VT_co]):
    def __contains__(self, __x: Any) -> bool:
        ...

    def __getitem__(self, __key: _KT_contra) -> _VT_co:
        ...


class SupportsItemAccess(SupportsGetItem[_KT_contra, _VT], Protocol[_KT_contra, _VT]):
    def __setitem__(self, __key: _KT_contra, __value: _VT) -> None:
        ...

    def __delitem__(self, __key: _KT_contra) -> None:
        ...


# ====================
# File handling
# ====================

StrPath: TypeAlias = Union[str, "PathLike[str]"]
BytesPath: TypeAlias = Union[bytes, "PathLike[bytes]"]
StrOrBytesPath: TypeAlias = Union[str, bytes, "PathLike[str]", "PathLike[bytes]"]

OpenTextModeUpdating: TypeAlias = Literal[
    "r+",
    "+r",
    "rt+",
    "r+t",
    "+rt",
    "tr+",
    "t+r",
    "+tr",
    "w+",
    "+w",
    "wt+",
    "w+t",
    "+wt",
    "tw+",
    "t+w",
    "+tw",
    "a+",
    "+a",
    "at+",
    "a+t",
    "+at",
    "ta+",
    "t+a",
    "+ta",
    "x+",
    "+x",
    "xt+",
    "x+t",
    "+xt",
    "tx+",
    "t+x",
    "+tx",
]
OpenTextModeWriting: TypeAlias = Literal["w", "wt", "tw", "a", "at", "ta", "x", "xt", "tx"]
OpenTextModeReading: TypeAlias = Literal[
    "r", "rt", "tr", "U", "rU", "Ur", "rtU", "rUt", "Urt", "trU", "tUr", "Utr"
]
OpenTextMode: TypeAlias = Union[OpenTextModeUpdating, OpenTextModeWriting, OpenTextModeReading]
OpenBinaryModeUpdating: TypeAlias = Literal[
    "rb+",
    "r+b",
    "+rb",
    "br+",
    "b+r",
    "+br",
    "wb+",
    "w+b",
    "+wb",
    "bw+",
    "b+w",
    "+bw",
    "ab+",
    "a+b",
    "+ab",
    "ba+",
    "b+a",
    "+ba",
    "xb+",
    "x+b",
    "+xb",
    "bx+",
    "b+x",
    "+bx",
]
OpenBinaryModeWriting: TypeAlias = Literal["wb", "bw", "ab", "ba", "xb", "bx"]
OpenBinaryModeReading: TypeAlias = Literal["rb", "br", "rbU", "rUb", "Urb", "brU", "bUr", "Ubr"]
OpenBinaryMode: TypeAlias = Union[
    OpenBinaryModeUpdating, OpenBinaryModeReading, OpenBinaryModeWriting
]


class HasFileno(Protocol):
    def fileno(self) -> int:
        ...


FileDescriptor: TypeAlias = int
FileDescriptorLike: TypeAlias = Union[int, HasFileno]
FileDescriptorOrPath: TypeAlias = Union[int, StrOrBytesPath]


class SupportsRead(Protocol[_T_co]):
    def read(self, __length: int = ...) -> _T_co:
        ...


class SupportsReadline(Protocol[_T_co]):
    def readline(self, __length: int = ...) -> _T_co:
        ...


class SupportsNoArgReadline(Protocol[_T_co]):
    def readline(self) -> _T_co:
        ...


class SupportsWrite(Protocol[_T_contra]):
    def write(self, __s: _T_contra) -> object:
        ...


# ====================
# Buffer protocols
# ====================

# Unfortunately PEP 688 does not allow us to distinguish read-only
# from writable buffers. We use these aliases for readability for now.
# Perhaps a future extension of the buffer protocol will allow us to
# distinguish these cases in the type system.
ReadOnlyBuffer: TypeAlias = Buffer
# Anything that implements the read-write buffer interface.
WriteableBuffer: TypeAlias = Buffer
# Same as WriteableBuffer, but also includes read-only buffer types (like bytes).
ReadableBuffer: TypeAlias = Buffer


class SliceableBuffer(Buffer, Protocol):
    def __getitem__(self, __slice: slice) -> Sequence[int]:
        ...


class IndexableBuffer(Buffer, Protocol):
    def __getitem__(self, __i: int) -> int:
        ...


class SupportsGetItemBuffer(SliceableBuffer, IndexableBuffer, Protocol):
    def __contains__(self, __x: Any) -> bool:
        ...

    @overload
    def __getitem__(self, __slice: slice) -> Sequence[int]:
        ...

    @overload
    def __getitem__(self, __i: int) -> int:
        ...


class SizedBuffer(Sized, Buffer, Protocol):
    ...
