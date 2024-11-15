# rosenbrock.py
import numpy as np
from typing import Tuple
import time


class Optimizer:
    """Class for optimizing the Rosenbrock function using grid search."""

    def __init__(self, a: float = np.pi/2, b: float = 100):
        """Set up optimizer with Rosenbrock parameters a and b."""
        self.a = a
        self.b = b

    def calc(self, x: float, y: float) -> float:
        """Calculate Rosenbrock function value at point (x,y)."""
        return (self.a - x)**2 + self.b * (y - x**2)**2

    def grid(self, n: int) -> Tuple[np.ndarray, np.ndarray]:
        """Make grid with n intervals."""
        if not isinstance(n, int) or n < 1:
            raise ValueError("n must be a positive integer")

        x = np.linspace(-3, 3, n + 1)
        y = np.linspace(-1, 5, n + 1)
        return np.meshgrid(x, y)

    def run_fast(self, n: int) -> Tuple[float, float, float, float]:
        """Run vectorized optimization on n x n grid."""
        start = time.time()
        X, Y = self.grid(n)
        Z = (self.a - X)**2 + self.b * (Y - X**2)**2

        min_idx = np.unravel_index(np.argmin(Z), Z.shape)
        min_val = Z[min_idx]
        min_x = X[min_idx]
        min_y = Y[min_idx]

        end = time.time()
        return end - start, float(min_val), float(min_x), float(min_y)

    def run_slow(self, n: int) -> Tuple[float, float, float, float]:
        """Run non-vectorized optimization on n x n grid."""
        start = time.time()
        X, Y = self.grid(n)
        Z = np.zeros_like(X)

        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                Z[i, j] = self.calc(X[i, j], Y[i, j])

        min_idx = np.unravel_index(np.argmin(Z), Z.shape)
        min_val = Z[min_idx]
        min_x = X[min_idx]
        min_y = Y[min_idx]

        end = time.time()
        return end - start, float(min_val), float(min_x), float(min_y)

    def min_point(self) -> Tuple[float, float]:
        """Get true minimum point (x,y)."""
        return (self.a, self.a**2)
