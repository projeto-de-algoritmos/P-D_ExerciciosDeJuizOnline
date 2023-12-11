class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        num_crimes = len(group)

        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, num_crimes + 1):
            curr_members, curr_profit = group[i - 1], profit[i - 1]
            new_dp = [row[:] for row in dp]

            for j in range(n + 1):
                for k in range(minProfit + 1):
                    new_dp[j][k] = dp[j][k]

                    if j >= curr_members:
                        prev_members, prev_profit = j - curr_members, max(0, k - curr_profit)
                        new_dp[j][k] += dp[prev_members][prev_profit]

                    new_dp[j][k] %= MOD

            dp = new_dp

        total_schemes = sum(dp[j][minProfit] for j in range(n + 1))
        return total_schemes % MOD 