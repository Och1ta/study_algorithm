def main():
    data = list(map(int, input().split()))
    flag = True
    last_item = len(data) - 1

    while flag:
        flag = False

        for item_index in range(last_item):

            if data[item_index] > data[item_index + 1]:
                data[item_index], data[item_index + 1] = (
                    data[item_index + 1], data[item_index]
                )
                flag = True

        item_index -= 1

    return print(data)


if __name__ == '__main__':
    main()
