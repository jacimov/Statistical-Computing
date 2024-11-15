# test_rosenbrock.py
import pytest
import numpy as np
from rosenbrock import Optimizer


def test_init():
    """Test initialization."""
    opt = Optimizer(a=1.5, b=200)
    assert opt.a == 1.5
    assert opt.b == 200


def test_calc():
    """Test function calculation."""
    opt = Optimizer(a=1, b=100)

    # At minimum point
    assert np.isclose(opt.calc(1, 1), 0)

    # At origin
    assert np.isclose(opt.calc(0, 0), 1)

    # At some other point, e.g., (0,1)
    # (1-0)² + 100(1-0²)² = 1 + 100 = 101
    assert np.isclose(opt.calc(0, 1), 101)


def test_grid():
    """Test grid creation."""
    opt = Optimizer()

    # Check size
    X, Y = opt.grid(10)
    assert X.shape == (11, 11)
    assert Y.shape == (11, 11)

    # Check bounds
    assert np.isclose(X.min(), -3)
    assert np.isclose(X.max(), 3)
    assert np.isclose(Y.min(), -1)
    assert np.isclose(Y.max(), 5)

    # Check errors
    with pytest.raises(ValueError):
        opt.grid(-1)
    with pytest.raises(ValueError):
        opt.grid(1.5)


def test_compare():
    """Test fast vs slow methods match."""
    opt = Optimizer()
    n = 10  # Small grid

    _, v_min, v_x, v_y = opt.run_fast(n)
    _, nv_min, nv_x, nv_y = opt.run_slow(n)

    assert np.isclose(v_min, nv_min)
    assert np.isclose(v_x, nv_x)
    assert np.isclose(v_y, nv_y)


def test_min():
    """Test minimum point."""
    opt = Optimizer()
    x, y = opt.min_point()
    assert np.isclose(x, np.pi/2)
    assert np.isclose(y, (np.pi/2)**2)
    assert np.isclose(opt.calc(x, y), 0)
