from __future__ import annotations

import unittest

from Graph import Graph
from GraphAdjacentVertexIterator import GraphAdjacentVertexIterator
from GraphEdgeIterator import GraphEdgeIterator
from GraphIncidentEdgeIterator import GraphIncidentEdgeIterator
from GraphVertexIterator import GraphVertexIterator


class GraphIteratorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph: Graph[str] = Graph()
        for value in ("A", "B", "C"):
            self.graph.add_vertex(value)
        self.graph.add_edge("A", "B")
        self.graph.add_edge("B", "C")

    def test_vertex_iterator_forward_and_reverse(self) -> None:
        forward_values = [vertex.value for vertex in self.graph.vertex_iterator()]
        reverse_values = [
            vertex.value for vertex in self.graph.vertex_reverse_iterator()
        ]
        self.assertEqual(forward_values, ["A", "B", "C"])
        self.assertEqual(reverse_values, ["C", "B", "A"])

    def test_vertex_iterator_prev_and_clone(self) -> None:
        iterator = self.graph.vertex_iterator()
        first = next(iterator)
        self.assertEqual(first.value, "A")
        clone = iterator.clone()
        self.assertEqual(clone.current().value, "B")
        second = next(iterator)
        self.assertEqual(second.value, "B")
        self.assertEqual(iterator.prev().value, "B")
        self.assertEqual(iterator.prev().value, "A")

    def test_edge_iterator_const_and_reverse(self) -> None:
        edges = list(self.graph.edge_iterator(const=True))
        self.assertIn(("A", "B"), edges)
        self.assertIn(("B", "C"), edges)
        reverse_edges = list(self.graph.edge_reverse_iterator(const=True))
        self.assertEqual(reverse_edges, list(reversed(edges)))

    def test_incident_edge_iterator(self) -> None:
        iterator = self.graph.incident_edge_iterator("B")
        pairs = [edge.as_value_pair() for edge in iterator]
        self.assertCountEqual(pairs, [("A", "B"), ("B", "C")])
        const_pairs = list(self.graph.incident_edge_iterator("B", const=True))
        self.assertCountEqual(const_pairs, [("A", "B"), ("B", "C")])

    def test_adjacent_vertex_iterator(self) -> None:
        iterator = self.graph.adjacent_vertex_iterator("B")
        values = [vertex.value for vertex in iterator]
        self.assertCountEqual(values, ["A", "C"])
        const_values = list(self.graph.adjacent_vertex_iterator("B", const=True))
        self.assertCountEqual(const_values, ["A", "C"])

    def test_remove_vertex_by_iterator_uses_last(self) -> None:
        iterator = self.graph.vertex_iterator()
        next(iterator)  # advance to record last element
        self.graph.remove_vertex_by_iterator(iterator)
        self.assertNotIn("A", self.graph)

    def test_remove_vertex_by_iterator_uses_current_when_no_last(self) -> None:
        iterator = self.graph.vertex_iterator()
        self.graph.remove_vertex_by_iterator(iterator)
        self.assertNotIn("A", self.graph)

    def test_remove_edge_by_iterator_and_error_on_const(self) -> None:
        iterator = self.graph.edge_iterator()
        next(iterator)
        self.graph.remove_edge_by_iterator(iterator)
        self.assertEqual(self.graph.edge_count(), 1)
        const_iterator = self.graph.edge_iterator(const=True)
        with self.assertRaises(TypeError):
            self.graph.remove_edge_by_iterator(const_iterator)

    def test_remove_edge_by_iterator_uses_current_when_no_last(self) -> None:
        iterator = self.graph.edge_iterator()
        self.graph.remove_edge_by_iterator(iterator)
        self.assertEqual(self.graph.edge_count(), 1)

    def test_remove_vertex_by_iterator_const_raises(self) -> None:
        const_iterator = self.graph.vertex_iterator(const=True)
        with self.assertRaises(TypeError):
            self.graph.remove_vertex_by_iterator(const_iterator)

    def test_iterators_prev_stop_iteration(self) -> None:
        iterator = self.graph.vertex_iterator()
        with self.assertRaises(StopIteration):
            iterator.prev()
        last_iterator = self.graph.vertex_reverse_iterator()
        sequence = [next(last_iterator).value for _ in range(3)]
        self.assertEqual(sequence, ["C", "B", "A"])
        with self.assertRaises(StopIteration):
            next(last_iterator)

    def test_reverse_variants_on_custom_iterators(self) -> None:
        adjacent = list(self.graph.adjacent_vertex_iterator("B", reverse=True, const=True))
        self.assertEqual(adjacent, ["C", "A"])
        incident = list(self.graph.incident_edge_iterator("B", reverse=True, const=True))
        self.assertIn(("A", "B"), incident)
        self.assertIn(("B", "C"), incident)

    def test_to_list_helpers(self) -> None:
        const_vertices = self.graph.vertex_iterator(const=True).to_list()
        self.assertEqual(const_vertices, ["A", "B", "C"])
        raw_vertices = self.graph.vertex_iterator().to_list()
        self.assertEqual([vertex.value for vertex in raw_vertices], ["A", "B", "C"])
        edge_objects = self.graph.edge_iterator().to_list()
        self.assertEqual(
            {edge.as_value_pair() for edge in edge_objects},
            {("A", "B"), ("B", "C")},
        )
        incident_pairs = self.graph.incident_edge_iterator("B", const=True).to_list()
        self.assertCountEqual(incident_pairs, [("A", "B"), ("B", "C")])
        adjacent_vertices = self.graph.adjacent_vertex_iterator("B", const=True).to_list()
        self.assertCountEqual(adjacent_vertices, ["A", "C"])

    def test_vertex_iterator_additional_api(self) -> None:
        iterator = self.graph.vertex_iterator()
        self.assertTrue(iterator.is_valid())
        self.assertFalse(iterator.is_const())
        self.assertEqual(iterator.current().value, "A")
        next(iterator)
        self.assertEqual(iterator.last_vertex().value, "A")
        clone = iterator.clone()
        self.assertEqual(clone.current_vertex().value, "B")
        clone.reset()
        self.assertEqual(clone.current_vertex().value, "A")
        reversed_clone = iterator.reverse()
        self.assertEqual([vertex.value for vertex in reversed_clone], ["C", "B", "A"])

    def test_edge_iterator_additional_api(self) -> None:
        iterator = self.graph.edge_iterator()
        self.assertTrue(iterator.is_valid())
        self.assertFalse(iterator.is_const())
        self.assertEqual(iterator.current_edge().as_value_pair(), ("A", "B"))
        first = next(iterator)
        self.assertEqual(first.as_value_pair(), ("A", "B"))
        self.assertEqual(iterator.last_edge().as_value_pair(), ("A", "B"))
        clone = iterator.clone()
        self.assertEqual(clone.current_edge().as_value_pair(), ("B", "C"))
        clone.reset()
        self.assertEqual(clone.current_edge().as_value_pair(), ("A", "B"))
        reverse = iterator.reverse()
        self.assertEqual(
            [edge.as_value_pair() for edge in reverse],
            [("B", "C"), ("A", "B")],
        )

    def test_incident_edge_iterator_additional_api(self) -> None:
        iterator = self.graph.incident_edge_iterator("B")
        self.assertTrue(iterator.is_valid())
        self.assertFalse(iterator.is_const())
        self.assertEqual(iterator.current_edge().as_value_pair(), ("A", "B"))
        first = next(iterator)
        self.assertEqual(first.as_value_pair(), ("A", "B"))
        self.assertEqual(iterator.last_edge().as_value_pair(), ("A", "B"))
        clone = iterator.clone()
        self.assertEqual(clone.current_edge().as_value_pair(), ("B", "C"))
        clone.reset()
        self.assertEqual(clone.current_edge().as_value_pair(), ("A", "B"))
        self.assertEqual(iterator.prev().as_value_pair(), ("A", "B"))
        reverse = iterator.reverse()
        self.assertEqual(
            [edge.as_value_pair() for edge in reverse],
            [("B", "C"), ("A", "B")],
        )

    def test_adjacent_vertex_iterator_additional_api(self) -> None:
        iterator = self.graph.adjacent_vertex_iterator("B")
        self.assertTrue(iterator.is_valid())
        self.assertFalse(iterator.is_const())
        self.assertEqual(iterator.current_vertex().value, "A")
        first = next(iterator)
        self.assertEqual(first.value, "A")
        self.assertEqual(iterator.last_vertex().value, "A")
        clone = iterator.clone()
        self.assertEqual(clone.current_vertex().value, "C")
        clone.reset()
        self.assertEqual(clone.current_vertex().value, "A")
        reverse = iterator.reverse()
        self.assertEqual(
            [vertex.value for vertex in reverse],
            ["C", "A"],
        )


if __name__ == "__main__":
    unittest.main()
