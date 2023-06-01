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


def creating_an_output_format(info):
    '''Создает вывод данных в заданном формате'''
    format_data = []
    for itm in info:
        date = itm['date'][:10]
        # print(date)
        format_date = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%d.%m.%Y')
        if itm.get('from') == None:
            itm["from"] = '->'
            z = ''
            from_info = ''
        else:
            sender = itm["from"].split()
            from_bill = sender.pop(-1)
            from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
            from_info = " ".join(sender)
            itm["from"] = from_bill
            z = '->'
        to_format = f"{itm['to'].split()[0]} **{itm['to'][-4:]}"
        format_data.append(f'''\
{format_date} {itm["description"]} 
{from_info} {itm["from"]} {z} {to_format}
{itm["operationAmount"]["amount"]} {itm["operationAmount"]["currency"]["name"]}
''')
    return format_data
