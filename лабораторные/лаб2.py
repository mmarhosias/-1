def count_list_elements(input_list):
    count = 0
    for element in input_list:
        if isinstance(element, list):
            count += 1
    return count

# Пример использования
my_list = [1, [2, 3], "text", [4, 5], 6]
result = count_list_elements(my_list)
print(f"Количество элементов списочного типа: {result}")

# Объяснение:
# Функция count_list_elements проверяет каждый элемент списка с помощью isinstance(element, list).
# Возвращает количество элементов, которые являются списками.