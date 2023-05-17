import pytest

from solutions.three_sum.solution import Solution


@pytest.mark.parametrize(
    "input_data,expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ],
)
def test_solution(input_data, expected):
    s = Solution()
    result = s.threeSum(input_data)
    assert result == expected
