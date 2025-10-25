from __future__ import annotations

import unittest

from Graph import Graph


class GraphTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph: Graph[str] = Graph()

    def test_add_and_contains_vertex(self) -> None:
        self.assertTrue(self.graph.empty())
        self.graph.add_vertex("A")
        self.assertTrue(self.graph.has_vertex("A"))
        self.assertIn("A", self.graph)
        self.assertEqual(len(self.graph), 1)
        self.assertFalse(self.graph.empty())

    def test_clear_resets_state(self) -> None:
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_edge("A", "B")
        self.graph.clear()
        self.assertTrue(self.graph.empty())
        self.assertEqual(self.graph.vertex_count(), 0)
        self.assertEqual(self.graph.edge_count(), 0)

    def test_add_edge_and_remove(self) -> None:
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        edge = self.graph.add_edge("A", "B")
        self.assertTrue(self.graph.has_edge("A", "B"))
        self.assertEqual(self.graph.edge_count(), 1)
        self.graph.remove_edge(edge.as_value_pair())
        self.assertFalse(self.graph.has_edge("A", "B"))
        self.assertEqual(self.graph.edge_count(), 0)

    def test_add_duplicate_vertex_raises(self) -> None:
        self.graph.add_vertex("A")
        with self.assertRaises(ValueError):
            self.graph.add_vertex("A")

    def test_add_edge_with_unknown_vertex_raises(self) -> None:
        self.graph.add_vertex("A")
        with self.assertRaises(ValueError):
            self.graph.add_edge("A", "B")

    def test_add_duplicate_edge_raises(self) -> None:
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_edge("A", "B")
        with self.assertRaises(ValueError):
            self.graph.add_edge("B", "A")

    def test_add_loop_edge_raises(self) -> None:
        self.graph.add_vertex("A")
        with self.assertRaises(ValueError):
            self.graph.add_edge("A", "A")

    def test_remove_unknown_vertex_raises(self) -> None:
        with self.assertRaises(ValueError):
            self.graph.remove_vertex("missing")

    def test_remove_unknown_edge_raises(self) -> None:
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_edge("A", "B")
        with self.assertRaises(ValueError):
            self.graph.remove_edge(("A", "C"))

    def test_remove_foreign_edge_raises(self) -> None:
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        other = Graph[str]()
        other.add_vertex("A")
        other.add_vertex("B")
        foreign_edge = other.add_edge("A", "B")
        with self.assertRaises(ValueError):
            self.graph.remove_edge(foreign_edge)

    def test_vertex_and_edge_degrees(self) -> None:
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")
        self.graph.add_edge("A", "B")
        self.graph.add_edge("B", "C")
        self.assertEqual(self.graph.vertex_degree("B"), 2)
        self.assertEqual(self.graph.vertex_degree("C"), 1)
        self.assertEqual(self.graph.edge_degree(("A", "B")), 1)
        self.assertEqual(self.graph.edge_degree(("B", "C")), 1)
        with self.assertRaises(ValueError):
            self.graph.vertex_degree("missing")
        with self.assertRaises(ValueError):
            self.graph.edge_degree(("C", "missing"))

    def test_copy_creates_independent_graph(self) -> None:
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_edge("A", "B")
        clone = self.graph.copy()
        self.assertEqual(clone, self.graph)
        clone.add_vertex("C")
        self.assertNotEqual(clone.vertex_count(), self.graph.vertex_count())

    def test_comparison_operators(self) -> None:
        g1 = Graph[str]()
        g2 = Graph[str]()
        for graph in (g1, g2):
            graph.add_vertex("A")
            graph.add_vertex("B")
        g1.add_edge("A", "B")
        self.assertNotEqual(g1, g2)
        self.assertTrue(g2 < g1)
        self.assertTrue(g1 > g2)
        g2.add_edge("A", "B")
        self.assertEqual(g1, g2)
        self.assertTrue(g1 <= g2)
        self.assertTrue(g1 >= g2)

    def test_iter_and_str_output(self) -> None:
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_edge("A", "B")
        vertices = list(self.graph)
        self.assertEqual(len(vertices), 2)
        self.assertEqual({v.value for v in vertices}, {"A", "B"})
        text = str(self.graph)
        self.assertIn("'A': ['B']", text)
        self.assertIn("'B': ['A']", text)


if __name__ == "__main__":
    unittest.main()
