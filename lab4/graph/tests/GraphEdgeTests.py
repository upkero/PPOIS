from __future__ import annotations

import unittest

from GraphEdge import GraphEdge
from GraphVertex import GraphVertex


class GraphEdgeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.vertex_a = GraphVertex("A")
        self.vertex_b = GraphVertex("B")
        self.edge = GraphEdge(7, self.vertex_a, self.vertex_b)

    def test_contains_vertex_and_endpoints(self) -> None:
        self.assertTrue(self.edge.contains_vertex(self.vertex_a))
        self.assertTrue(self.edge.contains_vertex(self.vertex_b))
        endpoints = self.edge.endpoints()
        self.assertEqual(endpoints, (self.vertex_a, self.vertex_b))
        self.assertEqual(self.edge.as_value_pair(), ("A", "B"))
        self.assertEqual(self.edge.edge_id, 7)

    def test_other_returns_opposite_vertex(self) -> None:
        self.assertIs(self.edge.other(self.vertex_a), self.vertex_b)
        self.assertIs(self.edge.other(self.vertex_b), self.vertex_a)

    def test_other_raises_for_non_incident_vertex(self) -> None:
        vertex_c = GraphVertex("C")
        with self.assertRaises(ValueError):
            self.edge.other(vertex_c)

    def test_constructor_rejects_loop(self) -> None:
        with self.assertRaises(ValueError):
            GraphEdge(8, self.vertex_a, self.vertex_a)


if __name__ == "__main__":
    unittest.main()
