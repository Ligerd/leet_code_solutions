import pytest

from solutions.best_time_to_buy_and_sell_stock.solution import Solution


@pytest.mark.parametrize(
    "input_data,expected", [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)]
)
def test_solution(input_data, expected):
    s = Solution()
    result = s.maxProfit(prices=input_data)
    assert result == expected
