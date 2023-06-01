from src.utils_get import get_data, selection_of_completed_operations, creating_an_output_format

PATH_TO_DATA='operations.json'
list_data = get_data(PATH_TO_DATA)
client_operation = selection_of_completed_operations(list_data, quantity=5)
output_of_information_about_operation = creating_an_output_format(client_operation)

for i in output_of_information_about_operation:
    print(i)