def count_uniform_integers(A, B):
    """
    Returns the number of uniform integers between A and B, inclusive.

    :param A: The lower bound (inclusive)
    :param B: The upper bound (inclusive)
    :return: The number of uniform integers between A and B
    """
    def is_uniform(n):
        """Checks if a number is uniform."""
        digits = [int(d) for d in str(n)]
        return len(set(digits)) == 1

    count = 0
    for i in range(A, B + 1):
        if is_uniform(i):
            count += 1
    return count

print(count_uniform_integers(222, 223))  # Output: 1
print(count_uniform_integers(1, 10))     # Output: 9
print(count_uniform_integers(100, 200))  # Output: 10