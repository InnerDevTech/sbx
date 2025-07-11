def count_artistic_photographs(C, X, Y):
    """
    Counts the number of different artistic photographs that could potentially be taken at the set.

    Args:
        C (str): A string representing the photography set, where "P" indicates a cell that can contain a photographer,
                 "A" indicates a cell that can contain an actor, "B" indicates a cell that can contain a backdrop,
                 and "." indicates an empty cell.
        X (int): The minimum distance between the photographer and the actor, and between the actor and the backdrop.
        Y (int): The maximum distance between the photographer and the actor, and between the actor and the backdrop.

    Returns:
        int: The number of different artistic photographs that could potentially be taken at the set.
    """
    N = len(C)
    P, A, B = [], [], []
    empty_cells = 0
    cell_indices = {"P": P, "A": A, "B": B}
    
    for i, c in enumerate(C):
        if c != ".":
            cell_indices[c].append(i)
        else:
            empty_cells += 1

    # Create a set of indices of non-empty cells for efficient lookups
    non_empty_cells = set(i for i, c in enumerate(C) if c != ".")

    count = 0
    for p in P:
        for a in A:
            if X <= abs(p - a) <= Y:
                # Only consider backdrops that are within the valid distance range
                valid_backdrops = [b for b in B if X <= abs(a - b) <= Y and min(p, b) < a < max(p, b)]
                count += sum(all(i in non_empty_cells for i in range(min(p, b), max(p, b) + 1)) for b in valid_backdrops)

    return count, empty_cells

# Example usage:
C = "P.A.B."
X = 1
Y = 2
N = len(C)
artistic_photographs, empty_cells = count_artistic_photographs(C, X, Y)
print("Number of cells:", N)
print("Number of artistic photographs:", artistic_photographs)
print("Number of empty cells:", empty_cells)