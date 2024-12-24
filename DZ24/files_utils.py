import json
import csv
import yaml

# Функции для работы с JSON

def read_json(file_path: str, encoding: str = "utf-8"):
    """Читает данные из JSON-файла."""
    with open(file_path, 'r', encoding=encoding) as f:
        return json.load(f)

def write_json(data, file_path: str, encoding: str = "utf-8"):
    """Записывает данные в JSON-файл."""
    with open(file_path, 'w', encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def append_json(data: list[dict], file_path: str, encoding: str = "utf-8"):
    """Добавляет данные в существующий JSON-файл."""
    try:
        existing_data = read_json(file_path, encoding)
        existing_data.extend(data)
    except FileNotFoundError:
        existing_data = data
    write_json(existing_data, file_path, encoding)

# Функции для работы с CSV

def read_csv(file_path, delimiter=';', encoding: str ='windows-1251'):
    """Читает данные из CSV-файла."""
    with open(file_path, 'r', encoding=encoding) as f:
        return list(csv.DictReader(f, delimiter=delimiter))

def write_csv(data, file_path, delimiter=';', encoding: str ='windows-1251'):
    """Записывает данные в CSV-файл."""
    with open(file_path, 'w', newline='', encoding=encoding) as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)

def append_csv(data, file_path, delimiter=';', encoding: str ='windows-1251'):
    """Добавляет данные в существующий CSV-файл."""
    existing_data = read_csv(file_path, delimiter, encoding)
    existing_data.extend(data)
    write_csv(existing_data, file_path, delimiter, encoding)

# Функции для работы с TXT

def read_txt(file_path, encoding: str = "utf-8"):
    """Читает данные из текстового файла."""
    with open(file_path, 'r', encoding=encoding) as f:
        return f.read()

def write_txt(data, file_path, encoding: str = "utf-8"):
    """Записывает данные в текстовый файл."""
    with open(file_path, 'w', encoding=encoding) as f:
        f.write(data)

def append_txt(data, file_path, encoding: str = "utf-8"):
    """Добавляет данные в конец текстового файла."""
    with open(file_path, 'a', encoding=encoding) as f:
        f.write(data)

# Функция для работы с YAML

def read_yaml(file_path):
    """Читает данные из YAML-файла."""
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)