def min_seconds(N, M, code):
    total_seconds = 0
    current_position = 1
    
    for Ci in code:
        # Calculate the shortest distance to Ci from the current position
        distance = min(abs(Ci - current_position), N - abs(Ci - current_position))
        
        # Update the total seconds and current position
        total_seconds += distance
        current_position = Ci
    
    return total_seconds

N = 10  # Number of integers on the wheel
M = 4  # Length of the code sequence
code = [9, 4, 4, 8]  # Code sequence

min_time = min_seconds(N, M, code)
print(min_time)  # Output: 11