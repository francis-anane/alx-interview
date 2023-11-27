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

    # Dictionary to store computed results for memoization
    memo = {}

    def minCoins(target):
        """
        Helper function for recursive computation of minimum coins needed.

        Args:
            target (int): Current target amount.

        Returns:
            int: Minimum number of coins needed to meet the target.
        """

        # Check if the result for the current target is already memoized
        if target in memo:
            return memo[target]

        # Base cases
        if target == 0:
            return 0

        if target < 0:
            return float('inf')

        # Initialize with a large value
        min_coins = float('inf')

        # Iterate over each coin value
        for coin in coins:
            # Recursive call to calculate the result for the current coin
            result = 1 + minCoins(target - coin)
            min_coins = min(min_coins, result)

        # Memoize the result for the current target
        memo[target] = min_coins

        return min_coins

    # Call the helper function to get the final result
    result = minCoins(total)

    # Return the result, or -1 if total cannot be met
    return result if result != float('inf') else -1
