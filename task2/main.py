import math
import sys

# Функция для вычисления положения точки относительно окружности
def calculate_position(center_x, center_y, radius, x, y):
    # Рассчитываем расстояние от точки (x, y) до центра окружности (center_x, center_y)
    distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
    
    # Сравниваем расстояние с радиусом
    if distance == radius:
        return 0  # Точка лежит на окружности
    elif distance < radius:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка снаружи окружности

# Главная программа
def main():
    # Получаем пути к файлам из аргументов командной строки
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    
    # Чтение данных из файла с окружностью
    with open(circle_file, 'r') as f:
        center_x, center_y = map(float, f.readline().split())
        radius = float(f.readline().strip())
    
    # Чтение данных из файла с точками
    with open(points_file, 'r') as f:
        for line in f:
            x, y = map(float, line.split())
            # Вычисление положения точки относительно окружности
            position = calculate_position(center_x, center_y, radius, x, y)
            print(position)

# Запуск программы
if __name__ == '__main__':
    main()
