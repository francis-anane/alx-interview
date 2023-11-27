#!/usr/bin/python3
"""Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
"""
import sys


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins
    # needed for each value from 0 to total
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make change for 0
    dp[0] = 0

    # Update the dp array for each coin value
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Check if the total can be made with the available coins
    return dp[total] if dp[total] != float('inf') else -1
