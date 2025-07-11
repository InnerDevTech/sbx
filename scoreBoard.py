from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  has_odd = False
  largest_even = 0
  for n in S:
    if n % 2 == 1:
      has_odd = True
      largest_even = max(largest_even, n - 1)
    largest_even = max(largest_even, n)
    
  return largest_even // 2 + has_odd


N = 4  # number of problems
S = [4, 3, 3, 4]  # scores
result = getMinProblemCount(N, S)
print("Minimum number of problems:", result)