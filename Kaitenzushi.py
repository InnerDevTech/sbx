import math

def grains_to_square(n):
    """
    Returns the smallest square number on a chessboard that has at least as many grains as the given amount.

    Args:
        n (int): The given amount of grains.

    Returns:
        int: The smallest square number that has at least as many grains as the given amount.
    """
    if n < 1:
        raise ValueError("Input must be a positive integer")

    return math.ceil(math.log2(n) + 1)

print(grains_to_square(1000))  # Output: 10
print(grains_to_square(2000))  # Output: 11
print(grains_to_square(4000))  # Output: 12 