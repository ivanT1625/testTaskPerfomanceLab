def find_path(n, m):   
    yield 1
    for i in range(m-1, n*m, m-1):
        v = i % n + 1
        if v == 1: return
        yield v

# Ввод данных от пользователя
n = int(input("Введите значение n (размер массива): "))
m = int(input("Введите значение m (интервал движения): "))

# Вычисление пути
path = find_path(n, m)

# Вывод результата
print("Путь:", "".join(map(str, path)))

