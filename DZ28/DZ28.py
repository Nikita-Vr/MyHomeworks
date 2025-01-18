class TxtFileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self) -> str:
        """Метод для чтения данных из TXT файла."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден.")
            return ""
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")
            return ""

    def write_file(self, *data: str) -> None:
        """Метод для записи данных в TXT файл."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                for line in data:
                    file.write(line + '\n')
        except Exception as e:
            print(f"Произошла ошибка при записи в файл: {e}")

    def append_file(self, *data: str) -> None:
        """Метод для добавления данных в конец TXT файла."""
        try:
            with open(self.filename, 'a', encoding='utf-8') as file:
                for line in data:
                    file.write(line + '\n')
        except Exception as e:
            print(f"Произошла ошибка при добавлении в файл: {e}")

# Пример использования
if __name__ == "__main__":
    handler = TxtFileHandler('example.txt')

    # Запись данных в файл
    handler.write_file("Это пример текста.", "Вторая строка.")

    # Добавление данных в файл
    handler.append_file("Добавленный текст.", "Еще одна строка.")

    # Чтение данных из файла
    content = handler.read_file()
    if content:
        print("Содержимое файла:")
        print(content)