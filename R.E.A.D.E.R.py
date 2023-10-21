def reader(peoples: int, tact: int):
    """
    intput
    Первая строка — целое число от 1 до 500, количество претендентов.
    Вторая строка — целое число от 1 до 500, количество тактов в считалке.
    output
    Целое число — номер победившего претендента.
    """
    members: list[int] = []

    for i in range(peoples):
        members.append(i + 1)

    point: int = 1
    index: int = 0

    while len(members) > 1:
        if point == tact:
            del members[index]
            point: int = 1

        else:
            point += 1
            index += 1

        if index == len(members):
            index: int = 0

    return members[0]


if __name__ == '__main__':
    print(reader(int(input()), int(input())))
