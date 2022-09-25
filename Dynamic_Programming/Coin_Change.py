def minCoins(n: int, arr: list, dp: list) -> int:
    if n == 0:
        return 0

    ans = float('inf')

    for i in range(0, len(arr)):

        if (n-arr[i] >= 0):

            subAns = 0
            if (dp[n-arr[i]] != -1):
                subAns = dp[n-arr[i]]
            else:
                subAns = minCoins(n-arr[i], arr, dp)

            if (subAns != float('inf') and subAns+1 < ans):
                ans = subAns + 1

    dp[n] = ans
    return ans


def main() -> None:
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [-1]*(n+1)
    dp[0] = 0

    ans = minCoins(n, arr, dp)
    print(ans)


if __name__ == '__main__':
    main()
