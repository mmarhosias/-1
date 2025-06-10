# Задание:
# В файле data_v2.txt посчитать количество цифр, расположенных рядом с символом «Z».


with open('data_v2.txt', 'r') as file:
    data = file.read()
    count = 0
    prev_even_pos = -1
    for i, char in enumerate(data):
        if char.isdigit() and int(char) % 2 == 0:
            if prev_even_pos != -1 and i - prev_even_pos > 1:
                count += i - prev_even_pos - 1
            prev_even_pos = i
    print(f"Количество символов между четными цифрами: {count}")