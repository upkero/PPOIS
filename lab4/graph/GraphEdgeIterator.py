from __future__ import annotations

from collections.abc import Iterable
from typing import Generic, Iterator, List, Tuple, TypeVar

from BidirectionalIterator import BidirectionalIterator
from GraphEdge import GraphEdge

T = TypeVar("T")


class GraphEdgeIterator(Generic[T], Iterator[GraphEdge[T] | Tuple[T, T]]):
    """Bidirectional iterator over graph edges."""

    def __init__(self, edges: Iterable[GraphEdge[T]], *, reverse: bool = False, const: bool = False) -> None:
        self._edges: List[GraphEdge[T]] = list(edges)
        self._iterator = BidirectionalIterator(self._edges, reverse=reverse)
        self._const = const

    def __iter__(self) -> GraphEdgeIterator[T]:
        return self

    def __next__(self) -> GraphEdge[T] | Tuple[T, T]:
        edge = next(self._iterator)
        return edge.as_value_pair() if self._const else edge

    def prev(self) -> GraphEdge[T] | Tuple[T, T]:
        edge = self._iterator.prev()
        return edge.as_value_pair() if self._const else edge

    def current(self) -> GraphEdge[T] | Tuple[T, T]:
        edge = self._iterator.current()
        return edge.as_value_pair() if self._const else edge

    def current_edge(self) -> GraphEdge[T]:
        return self._iterator.current()

    def is_valid(self) -> bool:
        return self._iterator.is_valid()

    def is_const(self) -> bool:
        return self._const

    def reset(self) -> None:
        self._iterator.reset()

    def clone(self) -> GraphEdgeIterator[T]:
        clone = GraphEdgeIterator(self._edges, reverse=self._iterator.reverse_flag, const=self._const)
        clone._iterator.set_index(self._iterator.current_index())
        clone._iterator.set_last_index(self._iterator.last_index())
        return clone

    def reverse(self) -> GraphEdgeIterator[T]:
        return GraphEdgeIterator(self._edges, reverse=not self._iterator.reverse_flag, const=self._const)

    def to_list(self) -> list[GraphEdge[T] | Tuple[T, T]]:
        if self._const:
            return [edge.as_value_pair() for edge in self._edges]
        return list(self._edges)

    def last(self) -> GraphEdge[T] | Tuple[T, T]:
        edge = self._iterator.last()
        return edge.as_value_pair() if self._const else edge

    def last_edge(self) -> GraphEdge[T]:
        return self._iterator.last()
