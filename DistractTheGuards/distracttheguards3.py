def is_perfect(pair):
    n = pair[0] + pair[1]

    while n % 2 == 0:
        n = n / 2
    return (pair[0] % n) != 0

def solution(banana_list):
    banana_matrix = [[0 for i in range(len(banana_list))] for j in range(len(banana_list))]

    for i in range(len(banana_list)):
        for j in range(i + 1, len(banana_list)):
            pair = [banana_list[i], banana_list[j]]
            if is_perfect(pair):
                banana_matrix[i][j] = 1
                banana_matrix[j][i] = 1

    to_check = len(banana_list)
    marked = [0 for _ in range(len(banana_list))]
    n_pairs = 0

    while to_check > 0:
        current_idx = 0
        for i in range(1, len(banana_matrix)):
            if marked[i] == 0:
                if (sum(banana_matrix[i]) < sum(banana_matrix[current_idx])) or marked[current_idx] == 1:
                    current_idx = i

        if sum(banana_matrix[current_idx]) == 0 and marked[current_idx] == 0:
            marked[current_idx] = 1
            to_check -= 1
        else:
            sub_idx = banana_matrix[current_idx][0]
            for i in range(len(banana_matrix)):
                if i != current_idx and sum(banana_matrix[i]) < sum(banana_matrix[sub_idx]):
                    sub_idx = i
            if marked[sub_idx] == 0:
                marked[current_idx] = 1
                marked[sub_idx] = 1
                to_check -= 2
                n_pairs += 1

    return len(banana_list) - n_pairs

if __name__ == "__main__":
    print(solution([1, 7, 3, 21, 13, 19]))