
import collections

def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    coins = sorted(coins)
    dp = [-1]*(amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        minval = float("inf")
        for c in coins:
            if c > i:   break
            if dp[i-c] == -1:   continue
            minval = min(minval, dp[i-c]+1)
        dp[i] = -1 if minval == float("inf") else minval
    return dp[-1]