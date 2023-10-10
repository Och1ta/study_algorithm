def main():
    nums = list(map(int, input().split()))
    element = int(input())
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == element:
            return print(mid + 1)

        if nums[mid] < element:
            left = mid + 1

        else:
            right = mid - 1

    return print(mid)


if __name__ == '__main__':
    main()
