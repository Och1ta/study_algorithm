def valid_mountain_array(mountain: list[int]) -> bool:
    start, end, length = 0, -1, len(mountain)

    while start < length - 1 and mountain[start] < mountain[start + 1]:
        start += 1

    while end > -length and mountain[end] < mountain[end - 1]:
        end -= 1

    return start == end + length and 0 < start and end < -1


if __name__ == '__main__':
    mountain: list[int] = [int(x) for x in input().split()]
    print(valid_mountain_array(mountain))
