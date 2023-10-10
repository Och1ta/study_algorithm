# Если список list_set_1 включает элементы списка list_set_2,
# то list_set_1 называют супермножеством по отношению к списку list_set_2.

list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]


def list_superset(list_set_1, list_set_2):
    k = 0

    for i in range(len(list_set_1)):
        for j in range(len(list_set_2)):
            if list_set_1[i] == list_set_2[j]:
                k += 1

    if len(list_set_1) == len(list_set_2) == k:
        return 'Наборы равны.'
    elif len(list_set_2) == k:
        return f"Набор {list_set_1} - супермножество."
    elif len(list_set_1) == k:
        return f"Набор {list_set_2} - супермножество."
    else:
        return 'Супермножество не обнаружено.'


list_superset(list_set_1, list_set_2)

list_superset(list_set_2, list_set_3)

list_superset(list_set_1, list_set_3)

list_superset(list_set_2, list_set_4)
