import unittest
from tsp import tsp

class TestTSP(unittest.TestCase):
    def test_tsp(self):
        points = [[0, 0], [10, 0], [5, 3], [0, 5], [3, 4], [4, 3], [3, 0]]
        self.assertAlmostEqual(tsp(points), 25.0)

if __name__ == '__main__':
    unittest.main()