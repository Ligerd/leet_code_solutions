import pytest

from solutions.jump_game.solution import Solution


@pytest.mark.parametrize(
    "input_data,expected",
    [([2, 3, 1, 1, 4], True), ([3, 2, 1, 0, 4], False)],
)
def test_solution(input_data, expected):
    s = Solution()
    result = s.canJump(input_data)
    assert result == expected
