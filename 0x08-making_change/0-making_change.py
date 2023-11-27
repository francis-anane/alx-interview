#!/usr/bin/python3
""" 0-making_change.py """


def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): List of coin values.
        total (int): Target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total.
             If total is 0 or less, returns 0.
             If total cannot be met by any number of coins, returns -1.
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of
    # coins needed for each value from 0 to total
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make change for 0
    dp[0] = 0

    # Update the dp array for each coin value
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Check if the total can be made with the available coins
    return dp[total] if dp[total] != float('inf') else -1
