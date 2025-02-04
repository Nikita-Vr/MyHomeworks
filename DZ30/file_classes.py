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

