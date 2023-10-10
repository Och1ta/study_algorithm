def main():
    nums_list = [-4, -3, -2, 0, 0, 2, 3, 5]
    # nums_list = list(map(int, input().split()))
    # -4 -3 -2 0 0 2 3 5 -> input
    # 0 0 4 4 9 9 16 25 -> output

    for i in range(len(nums_list) - 1):
        nums_list[i] = nums_list[i] * nums_list[i]
    print(sorted(nums_list))


if __name__ == '__main__':
    main()
