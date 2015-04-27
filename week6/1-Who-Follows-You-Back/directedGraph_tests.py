from directedGraph import DirectedGraph
from directedGraph import EdgeAlreadyThere
import unittest


class TestDirecteGraph(unittest.TestCase):
    def setUp(self):
        self.graph1 = DirectedGraph()

    def test_init(self):
        self.assertTrue(isinstance(self.graph1, DirectedGraph))

    def test_add_edge(self):
        self.graph1.add_edge("first", "second")
        self.graph1.add_edge("first", "third")
        with self.assertRaises(EdgeAlreadyThere):
            self.graph1.add_edge("first", "third")
        self.assertIn("first", self.graph1.graph.keys())
        self.assertIn("second", self.graph1.graph["first"])

    def test_get_neighbors_for(self):
        self.graph1.add_edge("first", "second")
        self.graph1.add_edge("first", "third")
        self.assertEqual(self.graph1.get_neighbors_for("first"), ['second', 'third'])

    def test_path_between(self):
        self.graph1.add_edge("first", "second")
        self.graph1.add_edge("first", "third")
        self.assertTrue(self.graph1.path_between("first", "second"))
        self.assertTrue(self.graph1.path_between("first", "third"))
        self.assertFalse(self.graph1.path_between("third", "first"))


if __name__ == '__main__':
    unittest.main()
