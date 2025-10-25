from __future__ import annotations

from collections import OrderedDict
from typing import Generic, Iterable, TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from GraphEdge import GraphEdge

T = TypeVar("T")


class GraphVertex(Generic[T]):
    """Vertex representation for the orthogonal adjacency list graph."""

    def __init__(self, value: T) -> None:
        self._value = value
        self._adjacent: "OrderedDict[T, GraphEdge[T]]" = OrderedDict()

    @property
    def value(self) -> T:
        return self._value

    def degree(self) -> int:
        return len(self._adjacent)

    def attach_edge(self, neighbor_value: T, edge: "GraphEdge[T]") -> None:
        self._adjacent[neighbor_value] = edge

    def detach_edge(self, neighbor_value: T) -> None:
        self._adjacent.pop(neighbor_value, None)

    def incident_edges(self) -> list["GraphEdge[T]"]:
        return list(self._adjacent.values())

    def adjacent_values(self) -> list[T]:
        return list(self._adjacent.keys())

    def has_neighbor(self, neighbor_value: T) -> bool:
        return neighbor_value in self._adjacent

    def get_edge(self, neighbor_value: T) -> "GraphEdge[T] | None":
        return self._adjacent.get(neighbor_value)

    def clear(self) -> None:
        self._adjacent.clear()

    def __repr__(self) -> str:
        return f"GraphVertex(value={self._value!r}, degree={self.degree()})"
