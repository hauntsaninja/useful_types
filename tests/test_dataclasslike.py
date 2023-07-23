import unittest
from dataclasses import dataclass

from useful_types.experimental import DataclassLike


class DataclassLikeTests(unittest.TestCase):
    def test_basics(self):
        with self.assertRaises(TypeError):
            DataclassLike()

        with self.assertRaises(TypeError):

            class Foo(DataclassLike):
                pass

    def test_not_runtime_checkable(self):
        # dataclasses already has `is_dataclass()`
        # for determining whether a class is a dataclass,
        # and the semantics for how isinstance() or issubclass()
        # should work at runtime against DataclassLike aren't 100% clear,
        # so make sure that the class isn't runtime-checkable
        @dataclass
        class Dataclass:
            x: int

        with self.assertRaises(TypeError):
            isinstance(Dataclass(42), DataclassLike)

        with self.assertRaises(TypeError):
            issubclass(Dataclass(42), DataclassLike)


if __name__ == "__main__":
    unittest.main()
