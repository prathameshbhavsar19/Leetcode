class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2:
            return 0

        j = 0      # index of lowest price seen so far (buy day)
        bp = 0     # best profit so far

        for i in range(1, n):
            if prices[i] < prices[j]:
                j = i
                continue

            cand = prices[i] - prices[j]
            if cand > bp:
                bp = cand

        return bp


# ---- Tests ----
def run_tests():
    s = Solution()

    # Provided examples
    assert s.maxProfit([7,1,5,3,6,4]) == 5, "Example 1 failed"
    assert s.maxProfit([7,6,4,3,1]) == 0, "Example 2 failed"

    # Edge cases
    assert s.maxProfit([]) == 0, "Empty array"
    assert s.maxProfit([5]) == 0, "Single element"
    assert s.maxProfit([1,1]) == 0, "Two equal elements"
    assert s.maxProfit([1,2]) == 1, "Simple increasing"
    assert s.maxProfit([2,1]) == 0, "Simple decreasing"

    # More cases
    assert s.maxProfit([3,10,2,3]) == 7, "Peak before new min"
    assert s.maxProfit([2,4,1,7]) == 6, "Buy after a dip"
    assert s.maxProfit([2,1,2,1,0,1,2]) == 2, "Multiple small waves"
    assert s.maxProfit([1,2,3,4,5,6,7]) == 6, "Strictly increasing"
    assert s.maxProfit([9,8,7,6,5,4,3]) == 0, "Strictly decreasing"

    print("All tests passed ✅")


if __name__ == "__main__":
    run_tests()