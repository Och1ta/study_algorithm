# input
# В первой строке записан массив целых чисел, через пробел — это вес отдельных роботов.
# Во второй строке записан лимит — предельная грузоподъёмность платформы.
# output
# Целое число, указывающее на необходимое количество платформ для транспортировки.


def delivery_service():
    weights = list(map(int, input().split()))
    limit = int(input())
    weights.sort()  # Сортируем веса роботов по возрастанию
    platforms_count: int = 0

    while weights:
        heaviest_robot = weights.pop()  # Выбираем самого тяжелого робота

        if weights and heaviest_robot + weights[0] <= limit:
            # Если есть другие роботы и суммарный вес текущего и следующего робота не превышает лимит,
            # то помещаем обоих на платформу
            weights.pop(0)

        platforms_count += 1  # Увеличиваем счетчик платформ

    print(platforms_count)


if __name__ == '__main__':
    delivery_service()
