import unittest
from tsp_solver import tsp_solver
import numpy as np

class TestTSPSolver(unittest.TestCase):
    def test_tsp_solver(self):
        graph = np.array([[0, 0], [10, 0], [5, 3], [0, 5]])
        path = tsp_solver(graph)
        self.assertEqual(len(path), len(graph) + 1)
        self.assertEqual(path[0], 0)
        self.assertEqual(path[-1], 0)
        
    def test_tsp_solver_empty_graph(self):
        graph = np.array([])
        with self.assertRaises(IndexError):
            tsp_solver(graph)
        
if __name__ == '__main__':
    unittest.main()