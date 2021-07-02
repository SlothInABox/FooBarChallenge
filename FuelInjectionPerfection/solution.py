def solution(n):
    # Convert string input to int
    current = int(n)
    # Add to list of steps (useful for debugging)
    steps = [current]
    # Loop until 1
    while current > 1:
        # Is even?
        if current % 2 == 0:
            current = current / 2
        # Is the number less than two divides away or is the LSB 01?
        elif current < 4 or current % 4 == 1:
            current -= 1
        # Case where LSB: 11, taking away would be bad
        else:
            current += 1
        steps.append(current)
    return len(steps) - 1

if __name__ == "__main__":
    print(solution('15'))