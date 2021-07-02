def single_number(nums):
    a = 0
    for num in nums:
        a ^= num
    return a


def two_sum(list, k):
    complements = set()
    for num in list:
        if num in complements:
            return True
        else:
            complement = k - num
            complements.add(complement)
    return False


def binary_search(list, x):
    start = 0
    end = len(list) - 1
    while start < end:
        # Get mid point
        mid = start + (end - start) // 2
        # Is this the value?
        if list[mid] == x:
            return mid
        # Is the value greater than or less than the value
        elif list[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return -1


if __name__ == "__main__":
    print(single_number([4, 3, 2, 4, 1, 3, 2]))
    print(two_sum([4, 7, 1, -3, 2], 5))
