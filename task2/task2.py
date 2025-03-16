import sys

def main():

    circle_file = sys.argv[1]  # Первый аргумент - файл с окружностью
    points_file = sys.argv[2]  # Второй аргумент - файл с точками

    # Читаем параметры окружности из файла
    with open(circle_file, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        x_center = float(lines[0])  # Координата X центра
        y_center = float(lines[1])  # Координата Y центра
        radius = float(lines[2])  # Радиус окружности
    radius_sq = radius ** 2  # Квадрат радиуса для сравнения

    # Читаем координаты точек из файла
    with open(points_file, 'r') as f:
        points = []
        for line in f:
            # Разделяем строку на X и Y и преобразуем в числа
            x_str, y_str = line.strip().split()
            x = float(x_str)
            y = float(y_str)
            points.append((x, y))

    # Определяем положение каждой точки
    for point in points:
        x, y = point
        # Вычисляем квадрат расстояния от точки до центра
        dx = x - x_center
        dy = y - y_center
        distance_sq = dx ** 2 + dy ** 2

        # Сравниваем с квадратом радиуса и определяем код
        if distance_sq < radius_sq:
            print(1)
        elif distance_sq == radius_sq:
            print(0)
        else:
            print(2)

if __name__ == "__main__":
    main()