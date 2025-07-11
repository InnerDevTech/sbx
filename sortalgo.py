'''
 `A` ——> the input list of integers to be sorted
 `k` ——> a number such that all integers are in range `0…k-1`
'''
def countsort(A, k):
 
    # create an integer list of size `n` to store the sorted list
    output = [0] * len(A)
 
    # create an integer list of size `k + 1`, initialized by all zero
    freq = [0] * (k + 1)
 
    # using the value of each item in the input list as an index,
    # store each integer's count in `freq[]`
    for i in A:
        freq[i] = freq[i] + 1
 
    # calculate the starting index for each integer
    total = 0
    for i in range(k + 1):
        oldCount = freq[i]
        freq[i] = total
        total += oldCount
 
    # copy to the output list, preserving the order of inputs with equal keys
    for i in A:
        output[freq[i]] = i
        freq[i] = freq[i] + 1
 
    # copy the output list back to the input list
    for i in range(len(A)):
        A[i] = output[i]
 
 
if __name__ == '__main__':
 
    A = [4, 7, 3, 9, 4, 8, 2, 10, 10, 1, 4, 2, 1, 10]
 
    # range of list elements
    k = 10
 
    countsort(A, k)
    print(A)

def print_pairs(array, target):
        for a in array:
            for b in array:
                if a + b == target:
                    print(a, b)

a = 50
def print_even(array):
        for a in array:
            if a % 2 == 0:
                print("Sequence for {0}".format(a))
                for k in range(0, a):
                    print(k)