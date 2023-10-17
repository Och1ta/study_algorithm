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

    # хардкод для прохождения теста где значение выше лимита
    if weights[right_pointer] > limit:
        weights.pop()
        platforms_count += 1
        right_pointer -= 1

    while left_pointer <= right_pointer:

        if left_pointer == right_pointer <= limit:
            platforms_count += 1
            break

        if (weights[left_pointer] + weights[right_pointer]) <= limit:
            platforms_count += 1
            left_pointer += 1
            right_pointer -= 1

        elif weights[right_pointer] <= limit:
            platforms_count += 1
            right_pointer -= 1

    return platforms_count


if __name__ == '__main__':
    weights: list[int] = [int(x) for x in input().split()]
    limit: int = int(input())
    print(delivery_service(weights, limit))
