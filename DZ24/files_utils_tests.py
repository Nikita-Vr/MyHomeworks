from files_utils import read_json, write_json, read_csv, write_csv, read_txt, write_txt, read_yaml, write_yaml
import json
import csv
import yaml
import os

# Минимальный датасет для тестирования
data_json = {
    "name": "Test",
    "value": 123
}

data_csv = [
    {"name": "Test", "value": 123},
    {"name": "Sample", "value": 456}
]

data_txt = "Это тестовый текст."

data_yaml = {
    "name": "Test",
    "description": "Тестирование YAML"
}

# Запись данных в файлы для тестирования
write_json(data_json, 'test.json')
write_csv(data_csv, 'test.csv')
write_txt(data_txt, 'test.txt')
write_yaml(data_yaml, 'test.yaml')
# Чтение и проверка данных из файлов
read_json_result = read_json('test.json')
read_csv_result = read_csv('test.csv')
read_txt_result = read_txt('test.txt')
read_yaml_result = read_yaml('test.yaml')

# Вывод результатов чтения
print("JSON Result:", read_json_result)
print("CSV Result:", read_csv_result)
print("TXT Result:", read_txt_result)
print("YAML Result:", read_yaml_result)

# Удаление тестовых файлов
os.remove('test.json')
os.remove('test.csv')
os.remove('test.txt')
os.remove('test.yaml')