import sys

def main():
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    # Создаем круговой массив
    circular_array = list(range(1, n + 1))

    # Инициализируем путь и текущую позицию
    path = []
    current = 0  # Начинаем с первого элемента
    path.append(circular_array[current])

    # Вычисляем следующие элементы пути
    while True:
        # Перемещаемся на m-1 позиций вперед (по модулю n)
        current = (current + m - 1) % n

        # Если вернулись к началу, завершаем цикл
        if current == 0:
            break

        # Добавляем текущий элемент в путь
        path.append(circular_array[current])

    # Преобразуем путь в строку и выводим
    print(''.join(map(str, path)))

if __name__ == "__main__":
    main()