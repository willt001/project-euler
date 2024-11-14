def solution(total, coins):
    dp = [0] * (total + 1)
    dp[0] = 1  
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] += dp[amount - coin]
    return dp[total]
    
if __name__ == "__main__":
    total, coins = 200, [1, 2, 5, 10, 20, 50, 100, 200]
    print(solution(total, coins))