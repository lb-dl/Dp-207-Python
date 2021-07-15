from bisect import bisect_left


def longest_sequence(list_) -> int:
    if len(list_) == 0:
        return 0
    temp = [0 for i in range(len(list_) + 1)]
    length = 1
    temp[0] = list_[0]
    for i in range(len(list_)):

        if list_[i] > temp[length - 1]:
            temp[length] = list_[i]
            length += 1
        else:
            temp[bisect_left(temp, list_[i], 0, length-1)] = list_[i]

    return length


example = [1, 4, 2, 3, 9, 5, 6, 7, 8, 3, 6, 7] # 7
print(longest_sequence(example))
example = [1, 2, 3] # 3
print(longest_sequence(example))
example = [5, 4, 3, 2, 1] # 1
print(longest_sequence(example))
example = [4, 4, 4, 4] # 1
print(longest_sequence(example))
example = [1000, 2000, 3000, 4000,  10, 20, 30, 40, 50, 1, 2, 3] # 5
print(longest_sequence(example))
example = [1] # 1
print(longest_sequence(example))
example = [1000000000, 1, 10, 1000, 2000, 3000, 100, 200, 300, 400,  20, 30, 40, 50, 60, 2, 3] # 7
print(longest_sequence(example))
