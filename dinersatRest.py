from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  S.sort()
  num_new_diners = (S[0] - 1) // (K + 1)
  for i in range(1, len(S)):
    num_new_diners += (S[i] - S[i-1] - K-1) // (K + 1)
  num_new_diners += (N - S[-1]) // (K + 1)
  return num_new_diners

N = 10  # Total seats
K = 1   # Social distancing rule
M = 2   # Number of diners already seated
S = [2, 8]  # Seats occupied by diners

print(getMaxAdditionalDinersCount(N, K, M, S))