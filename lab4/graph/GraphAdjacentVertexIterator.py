from __future__ import annotations

from collections.abc import Iterable
from typing import Generic, Iterator, List, TypeVar

from BidirectionalIterator import BidirectionalIterator
from GraphVertex import GraphVertex

T = TypeVar("T")


class GraphAdjacentVertexIterator(Generic[T], Iterator[T | GraphVertex[T]]):
    """Iterates over vertices adjacent to a particular vertex."""

    def __init__(self, adjacent_vertices: Iterable[GraphVertex[T]], *, reverse: bool = False, const: bool = False) -> None:
        self._adjacent_vertices: List[GraphVertex[T]] = list(adjacent_vertices)
        self._iterator = BidirectionalIterator(self._adjacent_vertices, reverse=reverse)
        self._const = const

    def __iter__(self) -> GraphAdjacentVertexIterator[T]:
        return self

    def __next__(self) -> T | GraphVertex[T]:
        vertex = next(self._iterator)
        return vertex.value if self._const else vertex

    def prev(self) -> T | GraphVertex[T]:
        vertex = self._iterator.prev()
        return vertex.value if self._const else vertex

    def current(self) -> T | GraphVertex[T]:
        vertex = self._iterator.current()
        return vertex.value if self._const else vertex

    def current_vertex(self) -> GraphVertex[T]:
        return self._iterator.current()

    def is_valid(self) -> bool:
        return self._iterator.is_valid()

    def is_const(self) -> bool:
        return self._const

    def reset(self) -> None:
        self._iterator.reset()

    def clone(self) -> GraphAdjacentVertexIterator[T]:
        clone = GraphAdjacentVertexIterator(self._adjacent_vertices, reverse=self._iterator.reverse_flag, const=self._const)
        clone._iterator.set_index(self._iterator.current_index())
        clone._iterator.set_last_index(self._iterator.last_index())
        return clone

    def reverse(self) -> GraphAdjacentVertexIterator[T]:
        return GraphAdjacentVertexIterator(self._adjacent_vertices, reverse=not self._iterator.reverse_flag, const=self._const)

    def to_list(self) -> list[T | GraphVertex[T]]:
        if self._const:
            return [vertex.value for vertex in self._adjacent_vertices]
        return list(self._adjacent_vertices)

    def last(self) -> T | GraphVertex[T]:
        vertex = self._iterator.last()
        return vertex.value if self._const else vertex

    def last_vertex(self) -> GraphVertex[T]:
        return self._iterator.last()
