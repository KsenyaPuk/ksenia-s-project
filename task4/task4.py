import sys


def main():

    file_name = sys.argv[1]  # Получаем имя файла из аргументов

    # Читаем числа из файла и добавляем в список
    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    # Сортируем массив для нахождения медианы
    numbers.sort()
    count = len(numbers)

    # Вычисляем медиану
    median_index = count // 2
    if count % 2 == 1:
        median = numbers[median_index]
    else:
        # Для четного количества берем левый из двух средних элементов
        median = numbers[median_index - 1]

    # Считаем общее количество ходов
    total = 0
    for num in numbers:
        total += abs(num - median)

    print(total)


if __name__ == "__main__":
    main()