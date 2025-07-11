def count_uniform_numbers(A, B):
    """
    Counts the number of uniform integers between A and B, inclusive.

    Args:
        A (int): The lower bound of the range (inclusive).
        B (int): The upper bound of the range (inclusive).

    Returns:
        int: The number of uniform integers between A and B.
    """
    count = 0
    min_digits = len(str(A))
    max_digits = len(str(B))

    for digits in range(min_digits, max_digits + 1):
        for digit in range(1, 10):
            uniform_number = int(str(digit) * digits)
            if A <= uniform_number <= B:
                count += 1

    return count

# Example usage:
A = 222
B = 333
print(count_uniform_numbers(A, B))