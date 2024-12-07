import json
import sys

# Функция для рекурсивного заполнения структуры из tests.json на основе значений из values.json
def fill_report(test_structure, values):
    # Преобразуем values в словарь для быстрого поиска
    values_dict = {item['id']: item['value'] for item in values}
    
    if isinstance(test_structure, dict):
        # Если текущий элемент - это словарь, проверяем его ключи
        for key, value in test_structure.items():
            # Если находим вложенные списки или словари, рекурсивно обрабатываем их
            if isinstance(value, dict) or isinstance(value, list):
                fill_report(value, values)
            # Если нашли id и оно есть в values_dict, заполняем value
            elif key == "id" and value in values_dict:
                test_structure["value"] = values_dict[value]
    
    elif isinstance(test_structure, list):
        # Если текущий элемент - это список, обрабатываем каждый элемент
        for item in test_structure:
            fill_report(item, values)

def main():
    # Получаем пути к файлам из аргументов командной строки
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    # Чтение данных из файла values.json
    with open(values_file, 'r') as f:
        values_data = json.load(f)

    # Чтение данных из файла tests.json
    with open(tests_file, 'r') as f:
        tests_data = json.load(f)

    # Заполнение report.json
    fill_report(tests_data['tests'], values_data['values'])

    # Запись результата в файл report.json
    with open(report_file, 'w') as f:
        json.dump(tests_data, f, indent=4)

# Запуск программы
if __name__ == '__main__':
    main()
