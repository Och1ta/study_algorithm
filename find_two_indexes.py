def find_two_indexes(data, expected_result):
    left_pointer = 0
    right_pointer = len(data) - 1

    while left_pointer < right_pointer:
        summ = data[left_pointer] + data[right_pointer]

        if summ == expected_result:
            return data[left_pointer], data[right_pointer]

        if summ > expected_result:
            right_pointer -= 1

        if summ < expected_result:
            left_pointer += 1


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum))
