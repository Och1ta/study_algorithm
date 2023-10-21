LEFT_POINTER: str = "["
RIGHT_POINTER: str = "]"


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
    data_calculations: list[tuple[str, int]] = []
    temp_variable: str = ''
    temp_result: int = 0

    for symbol in encoded_command:
        if symbol == LEFT_POINTER:
            # Ищем открывающую скобку '['
            # Сохраняем число и символ в хранилище
            data_calculations.append((temp_variable, temp_result))

            # чистим temp_variable для нового символа в [ ]
            temp_variable = ''

            # чистим temp_result для нового числа в [ ]
            temp_result = 0

        elif symbol == RIGHT_POINTER:
            # Ищем закрывающую скобку ']'
            # Записываем крайнее число и символ из хранилища
            early_variable, earle_result = data_calculations.pop()
            temp_variable = early_variable + temp_variable * earle_result

        elif symbol.isdigit():
            # Обновляем текущее число
            temp_result = temp_result * 10 + int(symbol)

        else:
            # Обновляем текущий символ
            temp_variable += symbol

    return temp_variable


if __name__ == '__main__':
    print(encrypted_instructions(input()))
