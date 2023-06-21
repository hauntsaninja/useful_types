import dataclasses as dc
from typing import Any, Dict, Tuple, Type, Union
from typing_extensions import assert_type

from useful_types.experimental import DataclassLike

def test_DataclassLike(x: DataclassLike, y: Union[DataclassLike, Type[DataclassLike]]) -> None:
    assert_type(dc.fields(x), Tuple[dc.Field[Any], ...])
    assert_type(dc.fields(y), Tuple[dc.Field[Any], ...])

    if not isinstance(y, type):
        assert_type(y, DataclassLike)

    assert_type(dc.fields(x), Tuple[dc.Field[Any], ...])
    assert_type(dc.asdict(x), Dict[str, Any])
    assert_type(dc.astuple(x), Tuple[Any, ...])

    # DataclassLike cannot be subclassed
    class Foo(DataclassLike):  # type: ignore
        pass
    # DataclassLike cannot be instantiated
    DataclassLike()  # type: ignore

@dc.dataclass
class Foo:
    x: int

test_DataclassLike(Foo(42), Foo)
