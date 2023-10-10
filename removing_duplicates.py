# Формат ввода
# В первой строке записано целое число n — это длина массива, переданного во второй строке.
# Во второй строке записано n натуральных чисел, разделённых пробелами.

# Формат вывода
# Уникальные числа из исходного массива по возрастанию и символы подчёркивания.
# Элементы должны быть разделены пробелами. Общее количество элементов должно быть равно n.

def main():
    n = int(input())
    n_list = input().split()
    temp_list = []

    while n > len(temp_list):
        for i in n_list:
            if i not in temp_list:
                temp_list.append(i)
        if n > len(temp_list):
            temp_list.append('_')

    print(' '.join(temp_list))


if __name__ == '__main__':
    main()