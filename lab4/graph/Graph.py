from __future__ import annotations

from collections import OrderedDict
from typing import Generic, Hashable, Iterable, Iterator, Tuple, TypeVar

from ForEachAlgorithm import ForEachAlgorithm
from GraphAdjacentVertexIterator import GraphAdjacentVertexIterator
from GraphEdge import GraphEdge
from GraphEdgeIterator import GraphEdgeIterator
from GraphIncidentEdgeIterator import GraphIncidentEdgeIterator
from GraphVertex import GraphVertex
from GraphVertexIterator import GraphVertexIterator

T = TypeVar("T", bound=Hashable)


class Graph(Generic[T]):
    """Undirected graph implemented with an orthogonal adjacency list."""

    value_type = T
    reference = GraphVertex[T]
    const_reference = GraphVertex[T]
    pointer = GraphVertex[T]
    size_type = int
    difference_type = int

    def __init__(self, other: "Graph[T] | None" = None) -> None:
        self._vertices: "OrderedDict[T, GraphVertex[T]]" = OrderedDict()
        self._edges: "OrderedDict[frozenset[T], GraphEdge[T]]" = OrderedDict()
        self._next_edge_id = 0
        if other is not None:
            self._copy_from(other)

    def empty(self) -> bool:
        return not self._vertices

    def clear(self) -> None:
        for vertex in self._vertices.values():
            vertex.clear()
        self._vertices.clear()
        self._edges.clear()
        self._next_edge_id = 0

    def has_vertex(self, value: T) -> bool:
        return value in self._vertices

    def has_edge(self, value_a: T, value_b: T) -> bool:
        key = self._edge_key(value_a, value_b)
        return key in self._edges

    def vertex_count(self) -> int:
        return len(self._vertices)

    def edge_count(self) -> int:
        return len(self._edges)

    def add_vertex(self, value: T) -> GraphVertex[T]:
        if self.has_vertex(value):
            raise ValueError(f"Vertex {value!r} already exists")
        vertex = GraphVertex(value)
        self._vertices[value] = vertex
        return vertex

    def add_edge(self, value_a: T, value_b: T) -> GraphEdge[T]:
        vertex_a = self._require_vertex(value_a)
        vertex_b = self._require_vertex(value_b)
        if value_a == value_b:
            raise ValueError("Loops are not allowed in an undirected graph")

        key = self._edge_key(value_a, value_b)
        if key in self._edges:
            raise ValueError(f"Edge between {value_a!r} and {value_b!r} already exists")

        edge = GraphEdge(self._next_edge_id, vertex_a, vertex_b)
        self._next_edge_id += 1
        self._edges[key] = edge
        vertex_a.attach_edge(value_b, edge)
        vertex_b.attach_edge(value_a, edge)
        return edge

    def remove_vertex(self, vertex: GraphVertex[T] | T) -> None:
        vertex_obj = self._normalize_vertex(vertex)
        for neighbor_value in list(vertex_obj.adjacent_values()):
            self.remove_edge((vertex_obj.value, neighbor_value))
        self._vertices.pop(vertex_obj.value, None)

    def remove_edge(self, edge: GraphEdge[T] | Tuple[T, T]) -> None:
        edge_obj = self._normalize_edge(edge)
        value_a, value_b = edge_obj.as_value_pair()
        key = self._edge_key(value_a, value_b)
        if key not in self._edges:
            raise ValueError("Edge does not belong to the graph")

        self._edges.pop(key, None)
        self._vertices[value_a].detach_edge(value_b)
        self._vertices[value_b].detach_edge(value_a)

    def remove_vertex_by_iterator(self, iterator: GraphVertexIterator[T]) -> None:
        if iterator.is_const():
            raise TypeError("Cannot remove vertex through const iterator")
        try:
            vertex = iterator.last_vertex()
        except StopIteration:
            vertex = iterator.current_vertex()
        self.remove_vertex(vertex)

    def remove_edge_by_iterator(self, iterator: GraphEdgeIterator[T]) -> None:
        if iterator.is_const():
            raise TypeError("Cannot remove edge through const iterator")
        try:
            edge = iterator.last_edge()
        except StopIteration:
            edge = iterator.current_edge()
        self.remove_edge(edge)

    def vertex_degree(self, vertex: GraphVertex[T] | T) -> int:
        vertex_obj = self._normalize_vertex(vertex)
        return vertex_obj.degree()

    def edge_degree(self, edge: GraphEdge[T] | Tuple[T, T]) -> int:
        edge_obj = self._normalize_edge(edge)
        vertex_a, vertex_b = edge_obj.endpoints()
        adjacent_edges = {
            neighbor_edge
            for vertex in (vertex_a, vertex_b)
            for neighbor_edge in vertex.incident_edges()
            if neighbor_edge is not edge_obj
        }
        return len(adjacent_edges)

    def vertex_iterator(self, *, reverse: bool = False, const: bool = False) -> GraphVertexIterator[T]:
        return GraphVertexIterator(self._vertices.values(), reverse=reverse, const=const)

    def vertex_reverse_iterator(self, *, const: bool = False) -> GraphVertexIterator[T]:
        return self.vertex_iterator(reverse=True, const=const)

    def edge_iterator(self, *, reverse: bool = False, const: bool = False) -> GraphEdgeIterator[T]:
        return GraphEdgeIterator(self._edges.values(), reverse=reverse, const=const)

    def edge_reverse_iterator(self, *, const: bool = False) -> GraphEdgeIterator[T]:
        return self.edge_iterator(reverse=True, const=const)

    def incident_edge_iterator(
        self,
        vertex: GraphVertex[T] | T,
        *,
        reverse: bool = False,
        const: bool = False,
    ) -> GraphIncidentEdgeIterator[T]:
        vertex_obj = self._normalize_vertex(vertex)
        return GraphIncidentEdgeIterator(vertex_obj, reverse=reverse, const=const)

    def adjacent_vertex_iterator(
        self,
        vertex: GraphVertex[T] | T,
        *,
        reverse: bool = False,
        const: bool = False,
    ) -> GraphAdjacentVertexIterator[T]:
        vertex_obj = self._normalize_vertex(vertex)
        neighbors = [self._vertices[value] for value in vertex_obj.adjacent_values()]
        return GraphAdjacentVertexIterator(neighbors, reverse=reverse, const=const)

    def __len__(self) -> int:
        return self.vertex_count()

    def __iter__(self) -> Iterator[GraphVertex[T] | T]:
        return self.vertex_iterator()

    def __contains__(self, value: object) -> bool:
        return value in self._vertices

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return NotImplemented
        if self.vertex_count() != other.vertex_count() or self.edge_count() != other.edge_count():
            return False
        if set(self._vertices.keys()) != set(other._vertices.keys()):
            return False
        for value, vertex in self._vertices.items():
            if set(vertex.adjacent_values()) != set(other._vertices[value].adjacent_values()):
                return False
        return True

    def _comparison_key(self) -> tuple[int, int, tuple[tuple[str, tuple[str, ...]], ...]]:
        adjacency = []
        for value, vertex in self._vertices.items():
            neighbors = tuple(sorted(map(repr, vertex.adjacent_values())))
            adjacency.append((repr(value), neighbors))
        adjacency.sort(key=lambda item: item[0])
        return (self.vertex_count(), self.edge_count(), tuple(adjacency))

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return NotImplemented
        return self._comparison_key() < other._comparison_key()

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return NotImplemented
        return self._comparison_key() <= other._comparison_key()

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return NotImplemented
        return self._comparison_key() > other._comparison_key()

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return NotImplemented
        return self._comparison_key() >= other._comparison_key()

    def __str__(self) -> str:
        lines: list[str] = []

        def append_line(vertex: GraphVertex[T]) -> None:
            neighbors = ", ".join(repr(value) for value in vertex.adjacent_values())
            lines.append(f"{vertex.value!r}: [{neighbors}]")

        ForEachAlgorithm.apply(self.vertex_iterator(), append_line)
        return "\n".join(lines)

    def copy(self) -> "Graph[T]":
        return Graph(self)

    def __copy__(self) -> "Graph[T]":
        return self.copy()

    def __deepcopy__(self, memo: dict[int, object] | None = None) -> "Graph[T]":
        return self.copy()

    def _require_vertex(self, value: T) -> GraphVertex[T]:
        if value not in self._vertices:
            raise ValueError(f"Vertex {value!r} is not present in the graph")
        return self._vertices[value]

    def _edge_key(self, value_a: T, value_b: T) -> frozenset[T]:
        return frozenset((value_a, value_b))

    def _normalize_vertex(self, vertex: GraphVertex[T] | T) -> GraphVertex[T]:
        if isinstance(vertex, GraphVertex):
            if vertex.value not in self._vertices or self._vertices[vertex.value] is not vertex:
                raise ValueError("Vertex does not belong to this graph")
            return vertex
        return self._require_vertex(vertex)

    def _normalize_edge(self, edge: GraphEdge[T] | Tuple[T, T]) -> GraphEdge[T]:
        if isinstance(edge, GraphEdge):
            value_a, value_b = edge.as_value_pair()
            key = self._edge_key(value_a, value_b)
            graph_edge = self._edges.get(key)
            if graph_edge is not edge:
                raise ValueError("Edge does not belong to this graph")
            return edge

        value_a, value_b = edge
        key = self._edge_key(value_a, value_b)
        graph_edge = self._edges.get(key)
        if graph_edge is None:
            raise ValueError("Edge does not belong to this graph")
        return graph_edge

    def _copy_from(self, other: "Graph[T]") -> None:
        for value, vertex in other._vertices.items():
            copied_vertex = GraphVertex(vertex.value)
            self._vertices[value] = copied_vertex

        for key, edge in other._edges.items():
            value_a, value_b = edge.as_value_pair()
            vertex_a = self._vertices[value_a]
            vertex_b = self._vertices[value_b]
            copied_edge = GraphEdge(edge.edge_id, vertex_a, vertex_b)
            self._edges[key] = copied_edge
            vertex_a.attach_edge(value_b, copied_edge)
            vertex_b.attach_edge(value_a, copied_edge)

        self._next_edge_id = other._next_edge_id
