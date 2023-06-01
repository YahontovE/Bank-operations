from src.utils_get import get_data, selection_of_completed_operations, creating_an_output_format
import pytest

test_path='test_operation.json'
def test_get_data():
    data_1=get_data(test_path)
    assert isinstance(data_1,list)


def test_selection_of_completed_operations(test_data):
    assert selection_of_completed_operations(test_data,1)== [{
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "to": "Счет 35383033474447895560"
    }]

def test_creating_an_output_format(test_data):
    assert creating_an_output_format(test_data)==['26.08.2019 Перевод организации \nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n','03.07.2019 Перевод организации \n ->  Счет **5560\n8221.37 USD\n','30.06.2018 Перевод организации \nСчет 7510 68** **** 6952 -> Счет **6702\n''9824.07 USD\n','23.03.2018 Открытие вклада \n ->  Счет **2431\n48223.05 руб.\n']