# Определение максимального элемента списка.


def get_max_list(k):
    if len(k) > 1:
        max_ = get_max_list(k[1:])
        if k[0] < max_:
            return max_
        else:
            return k[0]
    if len(k) == 1:
        return k[0]


my_list = [100, 435, 6500, 2300, 800, -114, 36]
print(f'Исходный список: {my_list}')
print(f"максимальный элемент: {get_max_list(my_list)}")