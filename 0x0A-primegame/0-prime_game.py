#!/usr/bin/python3
""" Prime game """


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the number of elements
        in each round.

    Returns:
        str or None: The winner (either "Maria" or "Ben") or
        None if it's a tie.
    """
    winner_counter = {"Maria": 0, "Ben": 0}

    for i in range(x):
        round_winner = is_round_winner(nums[i], x)
        if round_winner is not None:
            winner_counter[round_winner] += 1

    if winner_counter["Maria"] > winner_counter["Ben"]:
        return "Maria"
    elif winner_counter["Ben"] > winner_counter["Maria"]:
        return "Ben"
    else:
        return None


def isRoundWinner(n, x):
    """
    Determines the winner of a single round.

    Args:
        n (int): The number of elements in the round.
        x (int): Total number of rounds.

    Returns:
        str or None: The round winner (either "Maria" or "Ben")
        or None if the round is a tie.
    """
    number_list = [i for i in range(1, n + 1)]
    players = ["Maria", "Ben"]

    for i in range(n):
        # Get the current player
        current_player = players[i % 2]
        selected_indices = []
        prime = -1

        for idx, num in enumerate(number_list):
            # If already picked a prime num, then find if num is
            # a multiple of the prime num
            if prime != -1:
                if num % prime == 0:
                    selected_indices.append(idx)
            # Else check if num is prime, then pick it
            else:
                if is_prime(num):
                    selected_indices.append(idx)
                    prime = num

        # If failed to pick, then the current player lost
        if prime == -1:
            if current_player == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx, val in enumerate(selected_indices):
                del number_list[val - idx]

    return None


def isPrime(n):
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # 0, 1, and even numbers greater than 2 are NOT PRIME
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        # Not prime if divisible by another number less or equal to
        # the square root of itself.
        # n**(1/2) returns the square root of n
        for i in range(3, int(n**(1/2)) + 1, 2):
            if n % i == 0:
                return False
        return True
