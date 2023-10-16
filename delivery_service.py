def delivery_service(weights: list[int], limit: int) -> int:
    """
    input
    В первой строке записан массив целых чисел, через пробел — это вес отдельных роботов.
    Во второй строке записан лимит — предельная грузоподъёмность платформы.
    output
    Целое число, указывающее на необходимое количество платформ для транспортировки.
    """

    weights: list[int] = sorted(weights)
    platforms_count: int = 0
    left_pointer: int = 0
    right_pointer: int = len(weights) - 1
    print(weights)

    while left_pointer <= right_pointer:

        if weights[right_pointer] >= limit:
            platforms_count += 1
            right_pointer -= 1
            print('1 IF//', 'LEFT - ', weights[left_pointer], ', RIGHT - ', weights[right_pointer])
            print('POINT = ', platforms_count)
            print('_________________________')

        if (weights[left_pointer] + weights[right_pointer]) <= limit:
            platforms_count += 1
            print('2 IF//', 'LEFT - ', weights[left_pointer], ', RIGHT - ', weights[right_pointer])
            print('POINT = ', platforms_count)
            print('_________________________')

        else:
            platforms_count += 1
            print('ELSE//', 'LEFT - ', weights[left_pointer], ', RIGHT - ', weights[right_pointer])
            print('POINT = ', platforms_count)
            print('_________________________')

        left_pointer += 1
        right_pointer -= 1

    return platforms_count


if __name__ == '__main__':
    weights: list[int] = [int(x) for x in input().split()]
    limit: int = int(input())
    print(delivery_service(weights, limit))
