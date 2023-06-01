import json
import datetime


def get_data(path):
    """Загружает список студентов из файла и сортирует по дате операции"""
    with open(path, 'r', encoding="utf-8") as file:
        data = json.load(file)
        data_sort = sorted(data, key=lambda data: str(data.get('date')), reverse=True)
        return data_sort


def selection_of_completed_operations(list_data, quantity=1):
    '''Создает список выполненных(EXECUTED) операций по заданноиму количкству '''
    operation = []
    total = 0
    for item in list_data:
        if len(item) != 0 and item['state'] == 'EXECUTED':
            total += 1
            operation.append(item)
        if total == quantity:
            break
    return operation
