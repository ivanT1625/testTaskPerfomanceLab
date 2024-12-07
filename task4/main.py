import sys

def read_numbers_from_file(file_path):
    """Читает числа из файла и возвращает их в виде списка."""
    with open(file_path, 'r') as f:
        return [int(line.strip()) for line in f.readlines()]

def min_moves_to_median(nums):
    """Вычисляет минимальное количество ходов для приведения всех элементов массива к медиане."""
    nums.sort()  # Сортируем массив
    n = len(nums)
    
    # Находим медиану
    median = nums[n // 2]  # Медиана для отсортированного массива
    
    # Считаем минимальные ходы
    moves = sum(abs(num - median) for num in nums)
    
    return moves

def main():
    # Получаем путь к файлу из аргумента командной строки
    file_path = sys.argv[1]

    # Чтение массива чисел из файла
    nums = read_numbers_from_file(file_path)

    # Вычисление минимального количества ходов
    result = min_moves_to_median(nums)

    # Вывод результата
    print(result)

# Запуск программы
if __name__ == '__main__':
    main()
