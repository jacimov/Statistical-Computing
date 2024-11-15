import unittest
from random_walker_module import ModifiedRandomWalker, RandomWalker


class TestModifiedRandomWalker(unittest.TestCase):
    def test_walker_initialization(self):
        walker = ModifiedRandomWalker()
        self.assertIsInstance(walker, ModifiedRandomWalker)

    def test_walker_step(self):
        walker = ModifiedRandomWalker()
        other_walkers = [RandomWalker(), RandomWalker(), RandomWalker()]
        initial_x = walker.get_x_pos()
        initial_y = walker.get_y_pos()
        walker.step(other_walkers)
        self.assertTrue(
            walker.get_x_pos() != initial_x or walker.get_y_pos() != initial_y)


if __name__ == '__main__':
    unittest.main()
