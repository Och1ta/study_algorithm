def encrypted_instructions(encoded_command: str) -> str:
    """
    input
    Сокращенная форма команды. Например, 3[a]2[bc]. Гарантированно приходит валидная строка.
    В строке могут быть только буквы, числа и квадратные скобки.
    Длина строки может находиться в диапазоне от 0 (пустая строка) до 30 символов включительно.
    Числа в строке могут быть от 1 до 300 включительно.
    output
    Полная форма команды. Например, aaabcbc.
    """
    LEFT_POINTER: str = "["
    RIGHT_POINTER: str = "]"
    data_calculations: tuple[list, list] = ([], [])
    temp_variable: str = ""
    temp_result: str = ""

    for symbol in encoded_command:

        if symbol.isdigit():
            temp_variable += symbol

        elif symbol == LEFT_POINTER:
            data_calculations[1].append(int(temp_variable))
            data_calculations[0].append(temp_result)
            temp_variable: str = ""
            temp_result: str = ""

        elif symbol == RIGHT_POINTER:
            temp_result: str = data_calculations[0].pop() + data_calculations[1].pop() * temp_result

        else:
            temp_result += symbol

    return temp_result


if __name__ == '__main__':
    print(encrypted_instructions(input()))
