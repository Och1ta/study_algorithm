def delivery_service(weights: list[int], limit: int) -> int:
    # input
    # В первой строке записан массив целых чисел, через пробел — это вес отдельных роботов.
    # Во второй строке записан лимит — предельная грузоподъёмность платформы.
    # output
    # Целое число, указывающее на необходимое количество платформ для транспортировки.

    weights: list[int] = sorted(weights)  # Сортируем веса роботов по возрастанию
    platforms_count: int = 0
    left_pointer: int = 0
    right_pointer: int = len(weights) - 1

    while left_pointer <= right_pointer:
        # Пока левый указатель меньше правого
        if weights[right_pointer] + weights[left_pointer] <= limit:
            # Если суммарный вес крайнего левого и правого робота не превышает лимит,
            # то помещаем обоих на платформу
            platforms_count += 1  # Увеличиваем счетчик платформ
            left_pointer += 1
            right_pointer -= 1

        elif weights[right_pointer] or weights[left_pointer] == limit:
            # Выбираем самого тяжелого робота
            # на крайнем левом или правом положении
            platforms_count += 1
            right_pointer -= 1

    return platforms_count


if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    limit = int(input())
    print(delivery_service(weights, limit))
