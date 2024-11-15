"""Implement find_interval."""


def find_interval(query_point, intervals):
    """Find the index of the largest endpoint that is <= query_point.

    If query_point is smaller than all the endpoints, return one less than the
    minimum index.

    Parameters
    ----------
    query_point : float
        number to test
    intervals : list
        ordered list of floats defining the intervals

    Returns
    -------
    int
        index of the endpoint
    """

    if len(intervals) == 0:
        raise ValueError("At least one interval endpoint must be provided")

    # Check if intervals are in ascending order
    if any(intervals[i] >= intervals[i+1] for i in range(len(intervals)-1)):
        raise ValueError("Intervals must be in ascending order")

    for idx, endpoint in enumerate(intervals):
        if query_point < endpoint:
            return idx - 1

    return len(intervals) - 1
