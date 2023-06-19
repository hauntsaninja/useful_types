import types
import unittest
from dataclasses import dataclass, is_dataclass
from unittest import skipUnless

from useful_types.experimental import DataclassLike

class DataclassLikeTests(unittest.TestCase):
    def test_basics(self):
        # As an abstract base class for all dataclasses,
        # it makes sense for DataclassLike to also be considered a dataclass
        self.assertTrue(is_dataclass(DataclassLike))
        self.assertTrue(issubclass(DataclassLike, DataclassLike))

        with self.assertRaises(TypeError):
            DataclassLike()

        with self.assertRaises(TypeError):
            class Foo(DataclassLike):
                pass
    def test_isinstance_issubclass(self):
        @dataclass
        class Dataclass:
            x: int
        self.assertTrue(issubclass(Dataclass, DataclassLike))
        self.assertIsInstance(Dataclass(42), DataclassLike)

        with self.assertRaises(TypeError):
            issubclass(Dataclass(42), DataclassLike)

        class NotADataclass:
            def __init__(self):
                self.x = 42
        self.assertFalse(issubclass(NotADataclass, DataclassLike))
        self.assertNotIsInstance(NotADataclass(), DataclassLike)

        class NotADataclassButDataclassLike:
            """A class from an outside library (attrs?) with dataclass-like behaviour"""

            __dataclass_fields__ = {}
        self.assertTrue(issubclass(NotADataclassButDataclassLike, DataclassLike))
        self.assertIsInstance(NotADataclassButDataclassLike(), DataclassLike)

        class HasInstanceDataclassFieldsAttribute:
            def __init__(self):
                self.__dataclass_fields__ = {}
        self.assertFalse(issubclass(HasInstanceDataclassFieldsAttribute, DataclassLike))
        self.assertNotIsInstance(HasInstanceDataclassFieldsAttribute(), DataclassLike)

        class HasAllAttributes:
            def __getattr__(self, name):
                return {}
        self.assertFalse(issubclass(HasAllAttributes, DataclassLike))
        self.assertNotIsInstance(HasAllAttributes(), DataclassLike)
    @skipUnless(
        hasattr(types, "GenericAlias"),
        "Cannot test subclasses of GenericAlias if GenericAlias does not exist"
    )
    def test_dataclass_subclassing_GenericAlias(self):
        @dataclass
        class GenericAliasSubclass(types.GenericAlias):
            origin: type
            args: type
        self.assertTrue(issubclass(GenericAliasSubclass, DataclassLike))
        self.assertIsInstance(GenericAliasSubclass(int, str), DataclassLike)

if __name__ == "__main__":
    unittest.main()
