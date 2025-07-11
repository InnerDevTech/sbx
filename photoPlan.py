def countArtisticPhotographs(N, X, Y, C):
    count = 0
    P = []
    A = []
    B = []
    
    # Store the indices of 'P', 'A', and 'B' cells
    for i in range(N):
        if C[i] == 'P':
            P.append(i)
        elif C[i] == 'A':
            A.append(i)
        elif C[i] == 'B':
            B.append(i)
    
    # Iterate over the 'P', 'A', and 'B' cells
    for p in P:
        for a in A:
            for b in B:
                # Check if the actor is between the photographer and the backdrop
                if (p < a and a < b) or (b < a and a < p):
                    # Check if the distances satisfy the conditions
                    if X <= abs(p - a) <= Y and X <= abs(a - b) <= Y:
                        count += 1
    
    return count

#N = 10  # Length of the string
#X = 2   # Minimum distance
#Y = 3   # Maximum distance
#C = "P.A.B.P.A.B"  # String representing the photography set

#N = 5
#C = "APABA"
#X = 2
#Y = 3

N = 8
C = ".PBAAP.B"
X = 1
Y = 3

print(countArtisticPhotographs(N, X, Y, C))