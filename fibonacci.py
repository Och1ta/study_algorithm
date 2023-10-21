def barometer_fibonacci(version: int) -> int:
    if version in [0, 1]:
        return 1
    return (barometer_fibonacci(version - 1) +
            barometer_fibonacci(version - 2))


if __name__ == '__main__':
    print(barometer_fibonacci(int(input())))
