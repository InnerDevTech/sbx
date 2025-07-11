def length_of_longest_substring(s: str) -> int:
    """
    Returns the longest substring without repeating characters
    
    Parameters:
    char_set:  set of characters in the string
    left:       left pointer of the sliding window
    max_length:  maximum length of substring without repeating characters

    Returns:
    int: length of the longest substring without repeating characters

    """
    
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

#Test the Function
s = "abcdgfabcdrtabc"
result = length_of_longest_substring(s)
print(f"The length of the longest substring without repeating characters in '{s}' is: {result}")