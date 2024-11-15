import unittest
from crowded_cows import find_crowded


class TestCrowdedCows(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(find_crowded([7, 3, 4, 2, 3, 4], 3), 4)
        self.assertEqual(find_crowded([7, 3, 4, 2, 3, 10, 4], 3), 3)
        self.assertEqual(find_crowded([7, 3, 1, 0, 4, 2, 16, 28, 3, 4], 3), -1)

    def test_edge_cases(self):
        self.assertEqual(find_crowded([], 3), -1)
        self.assertEqual(find_crowded([5], 3), -1)
        self.assertEqual(find_crowded([1, 2, 3, 4, 5], 1), -1)

    def test_same_breed(self):
        self.assertEqual(find_crowded([5, 5, 5, 5, 5], 2), 5)
        self.assertEqual(find_crowded([1, 1, 2, 3, 4], 1), 1)

    def test_multiple_crowded(self):
        self.assertEqual(find_crowded([1, 3, 1, 3, 2, 3], 2), 3)
        self.assertEqual(find_crowded([1, 2, 3, 2, 1, 2], 2), 2)
        self.assertEqual(find_crowded([3, 1, 3, 2, 3, 1], 2), 3)
        self.assertEqual(find_crowded([5, 2, 5, 3, 2, 4], 3), 5)
        self.assertEqual(find_crowded([1, 2, 3, 3, 2], 2), 3)

    def test_k_values(self):
        self.assertEqual(find_crowded([1, 2, 2, 3, 4], 1), 2)
        self.assertEqual(find_crowded([3, 3, 2, 2, 1], 1), 3)
        self.assertEqual(find_crowded([1, 2, 3, 2, 1], 10), 2)


if __name__ == '__main__':
    unittest.main()
