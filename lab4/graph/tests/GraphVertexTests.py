from __future__ import annotations

import unittest

from GraphEdge import GraphEdge
from GraphVertex import GraphVertex


class GraphVertexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.vertex_a = GraphVertex("A")
        self.vertex_b = GraphVertex("B")
        self.edge = GraphEdge(1, self.vertex_a, self.vertex_b)
        self.vertex_a.attach_edge("B", self.edge)
        self.vertex_b.attach_edge("A", self.edge)

    def test_degree_and_incident_edges(self) -> None:
        self.assertEqual(self.vertex_a.degree(), 1)
        self.assertTrue(self.vertex_a.has_neighbor("B"))
        self.assertEqual(self.vertex_a.adjacent_values(), ["B"])
        self.assertEqual(self.vertex_a.get_edge("B"), self.edge)
        self.assertEqual(self.vertex_a.incident_edges(), [self.edge])

    def test_detach_edge_removes_neighbor(self) -> None:
        self.vertex_a.detach_edge("B")
        self.assertEqual(self.vertex_a.degree(), 0)
        self.assertFalse(self.vertex_a.has_neighbor("B"))
        self.assertIsNone(self.vertex_a.get_edge("B"))
        self.assertEqual(self.vertex_a.incident_edges(), [])

    def test_clear_resets_adjacency(self) -> None:
        self.vertex_a.clear()
        self.assertEqual(self.vertex_a.degree(), 0)
        self.assertEqual(self.vertex_a.adjacent_values(), [])
        self.assertEqual(self.vertex_a.incident_edges(), [])


if __name__ == "__main__":
    unittest.main()
