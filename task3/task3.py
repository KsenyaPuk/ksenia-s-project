import sys
import json

def update_values(node, values_dict):
    """
    Рекурсивно обходит структуру тестов и обновляет поле 'value'
    на основе словаря values_dict.
    """
    if isinstance(node, dict):
        # Если у текущего узла есть id, обновляем значение
        if 'id' in node:
            node_id = node['id']
            if node_id in values_dict:
                node['value'] = values_dict[node_id]

        # Рекурсивно обрабатываем вложенные элементы
        if 'values' in node and isinstance(node['values'], list):
            for item in node['values']:
                update_values(item, values_dict)

    elif isinstance(node, list):
        # Обрабатываем каждый элемент списка
        for item in node:
            update_values(item, values_dict)

def main():
    # Получаем пути к файлам из аргументов
    tests_path = sys.argv[1]
    values_path = sys.argv[2]
    report_path = sys.argv[3]

    # Читаем данные тестов
    with open(tests_path, 'r') as f:
        tests_data = json.load(f)['tests']  # Получаем список тестов

    # Читаем значения
    with open(values_path, 'r') as f:
        values_list = json.load(f)['values']  # Получаем список значений


    # Создаем словарь для быстрого поиска: id -> value
    values_dict = {item['id']: item['value'] for item in values_list}

    # Обновляем значения в структуре тестов
    for test in tests_data:
        update_values(test, values_dict)

    # Сохраняем результат
    with open(report_path, 'w') as f:
        json.dump({"tests": tests_data}, f, indent=2, ensure_ascii=False)
        print("report.json successfully updated!")

if __name__ == "__main__":
    main()