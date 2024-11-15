import pytest
from find_interval import find_interval
import random


def test_basic_functionality():
    assert find_interval(1.2, [1.0, 2.0, 3.0, 4.0]) == 0
    assert find_interval(0.2, [1.0, 2.0, 3.0, 4.0]) == -1
    assert find_interval(3.5, [1.0, 2.0, 3.0, 4.0]) == 2
    assert find_interval(5.0, [1.0, 2.0, 3.0, 4.0]) == 3


def test_edge_cases():
    assert find_interval(1.0, [1.0, 2.0, 3.0]) == 0
    assert find_interval(3.0, [1.0, 2.0, 3.0]) == 2
    assert find_interval(0.9, [1.0]) == -1
    assert find_interval(1.1, [1.0]) == 0


def test_error_cases():
    with pytest.raises(ValueError):
        find_interval(1.0, [])  # empty intervals list

    with pytest.raises(ValueError):
        find_interval(1.0, [3.0, 2.0, 1.0])  # unsorted intervals


def test_type_errors():
    with pytest.raises(Exception):
        find_interval("not a number", [1.0, 2.0, 3.0])
    with pytest.raises(Exception):
        find_interval(1.0, "not a list")


def test_property_monotonic_increasing():
    intervals = [1.0, 2.0, 3.0, 4.0, 5.0]
    for i in range(len(intervals) - 1):
        assert find_interval(intervals[i] + 0.1, intervals) == i
        assert find_interval(intervals[i + 1] - 0.1, intervals) == i


def test_randomized():
    for _ in range(100):  # Run 100 random tests
        intervals = sorted([random.uniform(0, 100) for _ in range(
            random.randint(1, 10))])
        query_point = random.uniform(0, 100)
        result = find_interval(query_point, intervals)
        if query_point < intervals[0]:
            assert result == -1
        elif query_point >= intervals[-1]:
            assert result == len(intervals) - 1
        else:
            assert intervals[result] <= query_point < intervals[result + 1]


@pytest.mark.xfail
def test_future_improvement():
    # This test demonstrates a potential future improvement
    assert find_interval(2.0, [1.0, 2.0, 2.0, 3.0]) == 1  # Currently returns 2
