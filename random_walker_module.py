import numpy as np


class RandomWalker:
    """
    Represents a random walker in 2D space.
    The walker starts at (0, 0) and evolves in discrete time steps,
    with each step perturbing both coordinates by additive N(0, 1) noise.
    """

    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0

    def step(self):
        """Evolve the random walker one step ahead in time."""
        self.x_pos += np.random.normal(0, 1)
        self.y_pos += np.random.normal(0, 1)

    def get_x_pos(self):
        """Return the current x coordinate of the random walker."""
        return self.x_pos

    def get_y_pos(self):
        """Return the current y coordinate of the random walker."""
        return self.y_pos


class ModifiedRandomWalker(RandomWalker):
    """
    A modified random walker that jumps to the
    closest walker before taking a step.
    """

    def step(self, other_walkers):
        """
        Evolve the modified random walker one step ahead in time.
        First, find the closest walker among the other_walkers,
        jump to its location, then take a random step.
        """
        if other_walkers:
            closest_walker = min(other_walkers,
                                 key=lambda w: self._distance(w))
            self.x_pos = closest_walker.get_x_pos()
            self.y_pos = closest_walker.get_y_pos()

        # Now take a random step as in the parent class
        self.x_pos += np.random.normal(0, 1)
        self.y_pos += np.random.normal(0, 1)

    def _distance(self, other_walker):
        """Calculate the Euclidean distance to another walker."""
        dx = self.x_pos - other_walker.get_x_pos()
        dy = self.y_pos - other_walker.get_y_pos()
        return np.sqrt(dx**2 + dy**2)

# You can add any additional utility functions or constants here if needed


if __name__ == "__main__":
    # You can add some basic testing code here if you want
    rw = RandomWalker()
    print(f"Initial position: ({rw.get_x_pos()}, {rw.get_y_pos()})")
    rw.step()
    print(f"After one step: ({rw.get_x_pos()}, {rw.get_y_pos()})")

    mrw = ModifiedRandomWalker()
    other_walkers = [RandomWalker(), RandomWalker()]
    print(f"Initial position of MRW: ({mrw.get_x_pos()}, {mrw.get_y_pos()})")
    mrw.step(other_walkers)
    print(f"After one step of MRW: ({mrw.get_x_pos()}, {mrw.get_y_pos()})")
