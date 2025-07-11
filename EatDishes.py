from collections import deque

def dishes_eaten(N, K, D):
    """
    Calculate the number of dishes eaten.

    Args:
    N (int): The number of dishes on the kaiten belt.
    K (int): The number of previous dishes to consider.
    D (list): A list of dish types.

    Returns:
    int: The number of dishes eaten.
    """
    # Initialize a set to store the last K dishes eaten
    last_eaten = set()
    
    # Initialize a deque to store the order of the last K dishes eaten
    last_eaten_order = deque(maxlen=K)
    
    # Initialize the count of eaten dishes
    eaten_count = 0
    
    # Iterate over each dish
    for dish in D:
        # If the dish is not in the last K eaten dishes, eat it
        if dish not in last_eaten:
            # If the set is full, remove the oldest dish
            if len(last_eaten) == K:
                oldest_dish = last_eaten_order.popleft()
                last_eaten.remove(oldest_dish)
            
            last_eaten.add(dish)
            last_eaten_order.append(dish)
            eaten_count += 1
    
    return eaten_count

def print_results(N, K, D):
    print("Number of dishes (N):", N)
    print("Number of previous dishes to consider (K):", K)
    print("Dish types (D):", D)
    
    dishes_eaten_count = dishes_eaten(N, K, D)
    print("Number of dishes eaten:", dishes_eaten_count)

# Example usage:
N = 10  # Number of dishes
K = 3   # Number of previous dishes to consider
D = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2]  # Dish types

print_results(N, K, D)