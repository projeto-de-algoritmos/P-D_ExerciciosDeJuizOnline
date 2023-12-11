class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(n)]

        jobs.sort(key=lambda x: x[1])

        dp = [0] * n
        dp[0] = jobs[0][2]

        for i in range(1, n):
            include_current = jobs[i][2]
            last_non_overlapping = -1

            low, high = 0, i - 1
            while low <= high:
                mid = (low + high) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    last_non_overlapping = mid
                    low = mid + 1
                else:
                    high = mid - 1

            if last_non_overlapping != -1:
                include_current += dp[last_non_overlapping]

            exclude_current = dp[i - 1]

            dp[i] = max(include_current, exclude_current)

        return dp[n - 1]