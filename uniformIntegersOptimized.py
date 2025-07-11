def count_uniform_integers(A, B):
    """
    Returns the number of uniform integers between A and B, inclusive.

    :param A: The lower bound (inclusive)
    :param B: The upper bound (inclusive)
    :return: The number of uniform integers between A and B
    """
    def count_uniform_integers_with_digit(digit, num_digits):
        """Counts the number of uniform integers with the given digit and number of digits."""
        start = int(str(digit) * num_digits)
        if start > B:
            return 0
        end = int(str(digit) * (num_digits + 1)) - 1
        if end < A:
            return 0
        if start <= A and end >= B:
            return 1
        if start >= A and end <= B:
            return 1
        return 0

    count = 0
    for num_digits in range(len(str(A)), len(str(B)) + 1):
        for digit in range(1, 10):
            count += count_uniform_integers_with_digit(digit, num_digits)
    return count

print(count_uniform_integers(75, 100))  # Output: 1
print(count_uniform_integers(1, 9))     # Output: 9
print(count_uniform_integers(100, 200))  # Output: 10