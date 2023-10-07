class Solution:
  def numOfArrays(self, n: int, m: int, k: int) -> int:
    kMod = 1_000_000_007
    dp = [[[0] * (k + 1) for j in range(m + 1)] for _ in range(n + 1)]

    for j in range(1, m + 1):
      dp[1][j][1] = 1

    for i in range(2, n + 1):
      for j in range(1, m + 1):
        for cost in range(1, k + 1):
          dp[i][j][cost] = j * dp[i - 1][j][cost] % kMod

          for prevMax in range(1, j):
            dp[i][j][cost] += dp[i - 1][prevMax][cost - 1]
            dp[i][j][cost] %= kMod

    return sum(dp[n][j][k] for j in range(1, m + 1)) % kMod
