"""Typing for semver."""

import abc
from functools import partial
from typing import Union, Optional, Tuple, Dict, Iterable, Callable, TypeVar, Protocol

VersionPart = Union[int, Optional[str]]
VersionTuple = Tuple[int, int, int, Optional[str], Optional[str]]
VersionDict = Dict[str, VersionPart]
VersionIterator = Iterable[VersionPart]
String = Union[str, bytes]
F = TypeVar("F", bound=Callable)
Decorator = Union[Callable[..., F], partial]


class Comparable(Protocol):
    @abc.abstractmethod
    def __lt__(self, other: object) -> bool:
        ...

    @abc.abstractmethod
    def __gt__(self, other: object) -> bool:
        ...
