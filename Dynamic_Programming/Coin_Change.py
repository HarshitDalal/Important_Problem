def minCoins(amount: int, coins: list, dp: list) -> int:
    if amount == 0:
        return 0

    for c in coins:
        for i in range(amount + 1):
            if i >= c:
                dp[i] = min(dp[i], dp[i - c] + 1)

    if dp[amount] > amount:
        return -1

    return dp[amount]


def main() -> None:
    amount = int(input())
    coins = list(map(int, input().split()))

    dp = [amount+1]*(amount+1)
    dp[0] = 0

    ans = minCoins(amount, coins, dp)
    print(ans)


if __name__ == '__main__':
    main()
