def solution(l):
    # Initialise list of acceptable lucky triples
    lucky_count = 0
    # Initialise list of factor counts. Number of previous integers that are factors of this integer.
    factor_count = [0 for _ in range(len(l))]

    # Iterate over each integer in list (ignore first integer)
    for j in range(1, len(l)):
        # Iterate over each integer in the list (up to the jth integer)
        for i in range(j):
            # Is ith integer a factor of jth integer?
            if l[j] % l[i] == 0:
                # Increment the factor count by 1
                factor_count[j] += 1
    
    # Iterate over each integer in list (ignore first 2 integers)
    for k in range(2, len(l)):
        # Iterate over each integer in list (up to kth integer)
        for j in range(k):
            # Is the jth integer a factor of the kth integer?
            if l[k] % l[j] == 0:
                # Increment lucky count by the number of factors of the jth integer
                lucky_count += factor_count[j]

    # Return the total number of lucky triples
    return lucky_count

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ,20]
    print(solution(l))