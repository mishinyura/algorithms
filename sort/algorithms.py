def sort_select(self, lst: list) -> None:
    """
    Функция сортировки выбором. Сортирует переданный список
    :return: None
    """
    amount = len(lst)  # число элементов в списке
    for i in range(amount - 1):
        min = lst[i]  # запоминаем минимальное значение
        i_min = i  # запоминаем индекс минимального значения
        for j in range(i + 1, amount):  # поиск миимального среди оставшихся элементов
            if min > lst[j]:
                min = lst[j]
                i_min = j

        if i_min != i:  # обмен значениями, если был найден минимальный не в i-й позиции
            lst[i], lst[i_min] = lst[i_min], lst[i]

def sort_inserts(lst: list) -> None:
    """
    Алгоритм сортировки вставками
    :return:
    """
    amount = len(lst)  # число элементов в списке

    for i in range(1, amount):
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else: #Если элемент стоящий слева от j меньше j, то мы сдвинули элемент достаточно
                break

def sort_bubble(lst: list) -> None:
    """
    Алгоритм сортировки пузырьком
    :param lst:
    :return:
    """
    amount = len(lst) # число элементов в списке

    for i in range(0, amount - 1):
        for j in range(0, amount - 1 - i): # проход по оставшимся не отсортированным парам массива
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def merge_list(f_lst: list, s_lst: list) -> list:
    """
    Слияние списка с сортировкой
    :param f_lst:
    :param s_lst:
    :return:
    """
    new_lst = []
    f_amount = len(f_lst)
    s_amount = len(s_lst)
    i = 0
    j = 0
    while i < f_amount and j < s_amount:
        if f_lst[i] <= s_lst[j]:
            new_lst.append(f_lst[i])
            i += 1
        else:
            new_lst.append(s_lst[j])
            j += 1

    new_lst += f_lst[i:] + s_lst[j:]
    return new_lst

def sort_merge(lst: list):
    """
    Сортировка слиянием
    :param lst:
    :return:
    """
    amount = len(lst) // 2 # деление массива на два примерно равной длины
    f_lst = lst[:amount]
    s_lst = lst[amount:]

    if len(f_lst) > 1:  # если длина 1-го списка больше 1, то делим дальше
        f_lst = sort_merge(f_lst)
    if len(s_lst) > 1:  # если длина 2-го списка больше 1, то делим дальше
        s_lst = sort_merge(s_lst)

    return merge_list(f_lst, s_lst)  # слияние двух отсортированных списков в один


def sort_quick(lst: list) -> list:
    """
    Быстрая сортировка Хоара через рекурсию
    :param lst:
    :return:
    """
    if len(lst) > 1:
        x = lst[len(lst) // 2]  # пороговое значение (для разделения на малые и большие)
        low = [u for u in lst if u < x]
        eq = [u for u in lst if u == x]
        hi = [u for u in lst if u > x]
        lst = sort_quick(low) + eq + sort_quick(hi)

    return lst