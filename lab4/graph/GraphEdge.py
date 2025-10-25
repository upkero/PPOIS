from __future__ import annotations

from typing import Generic, Tuple, TypeVar

from GraphVertex import GraphVertex

T = TypeVar("T")


class GraphEdge(Generic[T]):
    """Edge representation that links two graph vertices."""

    def __init__(self, edge_id: int, vertex_a: GraphVertex[T], vertex_b: GraphVertex[T]) -> None:
        if vertex_a is vertex_b:
            raise ValueError("An edge cannot connect a vertex to itself")

        self._id = edge_id
        self._vertices: Tuple[GraphVertex[T], GraphVertex[T]] = (vertex_a, vertex_b)

    @property
    def edge_id(self) -> int:
        return self._id

    def endpoints(self) -> Tuple[GraphVertex[T], GraphVertex[T]]:
        return self._vertices

    def contains_vertex(self, vertex: GraphVertex[T]) -> bool:
        return vertex is self._vertices[0] or vertex is self._vertices[1]

    def other(self, vertex: GraphVertex[T]) -> GraphVertex[T]:
        if vertex is self._vertices[0]:
            return self._vertices[1]
        if vertex is self._vertices[1]:
            return self._vertices[0]
        raise ValueError("Vertex is not incident to this edge")

    def as_value_pair(self) -> Tuple[T, T]:
        return (self._vertices[0].value, self._vertices[1].value)

    def __repr__(self) -> str:
        a, b = self.as_value_pair()
        return f"GraphEdge(id={self._id}, vertices=({a!r}, {b!r}))"
