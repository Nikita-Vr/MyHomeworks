import json
import csv
from abc import ABC, abstractmethod

class AbstractFile(ABC):
    @abstractmethod
    def read(self):
        """Читает данные из файла."""
        pass

    @abstractmethod
    def write(self, data):
        """Записывает данные в файл."""
        pass

    @abstractmethod
    def append(self, data):
        """Добавляет данные в файл."""
        pass

class JsonFile(AbstractFile):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def write(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file)

    def append(self, data):
        current_data = self.read()
        current_data.update(data)  # Пример: объединяем данные
        self.write(current_data)

