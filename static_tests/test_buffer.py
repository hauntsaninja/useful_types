import pickle
from typing import Sequence, cast
from typing_extensions import assert_type

import useful_types as ut


def takes_read_only_buffer(b: ut.ReadOnlyBuffer) -> None:
    b[0]  # type: ignore


def takes_writeable_buffer(b: ut.ReadOnlyBuffer) -> None:
    b[0]  # type: ignore


def takes_readable_buffer(b: ut.ReadableBuffer) -> None:
    b[0]  # type: ignore


# We can't actually distinguish between read-only and writable buffers
takes_read_only_buffer(cast(bytes, None))
takes_readable_buffer(cast(bytes, None))
takes_writeable_buffer(cast(bytes, None))

takes_read_only_buffer(cast(pickle.PickleBuffer, None))
takes_readable_buffer(cast(pickle.PickleBuffer, None))
takes_writeable_buffer(cast(pickle.PickleBuffer, None))


def takes_sliceable_buffer(b: ut.SliceableBuffer) -> None:
    assert_type(b[0:1], Sequence[int])


takes_sliceable_buffer(cast(bytes, None))
takes_sliceable_buffer(cast(pickle.PickleBuffer, None))  # type: ignore
