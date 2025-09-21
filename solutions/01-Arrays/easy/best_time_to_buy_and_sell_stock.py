"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


def bruteforce(prices: list[int]) -> int:
    """Study question. No bruteforce."""
    return 0


def solution_two_pointers(prices: list[int]) -> int:
    if len(prices) <= 1:
        return 0

    buy = 0
    sell = 1
    max_profit = 0

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            max_profit = max(max_profit, prices[sell] - prices[buy])
        else:
            buy = sell
        sell += 1

    return max_profit


def solution_min_value(prices: list[int]) -> int:
    min_stock = float("inf")
    max_profit = 0

    for price in prices:
        min_stock = min(min_stock, price)
        max_profit = max(max_profit, price - min_stock)

    return int(max_profit)


def solution_pure_kadane(prices: list[int]) -> int:
    """
    Think of cur as “what would happen if I held the stock through that day"
    """
    best = 0
    cur = 0
    for i in range(1, len(prices)):
        cur = max(0, cur + prices[i] - prices[i - 1])
        best = max(best, cur)
    return best


if __name__ == "__main__":
    assert solution_two_pointers([7, 1, 5, 3, 6, 4]) == 5
    assert solution_two_pointers([7, 6, 4, 3, 1]) == 0
    assert solution_min_value([7, 1, 5, 3, 6, 4]) == 5
    assert solution_min_value([7, 6, 4, 3, 1]) == 0
    assert solution_pure_kadane([7, 1, 5, 3, 6, 4]) == 5
    assert solution_pure_kadane([7, 6, 4, 3, 1]) == 0
