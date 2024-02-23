from math import isinf


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        current_prices: list[int] = [float("inf") for _ in range(n)]
        current_prices[src] = 0

        for stops_num in range(0, k + 1, 1):
            prices_for_next: list[float] = current_prices.copy()

            for source, destination, price in flights:
                cost: int = current_prices[source] + price
                prices_for_next[destination] = min(prices_for_next[destination], cost)

            current_prices = prices_for_next

        return current_prices[dst] if not isinf(current_prices[dst]) else -1
