class TxtFileHandler:
    """
    Класс для работы с текстовыми файлами: чтение, запись и добавление данных.
    """

    def __init__(self, filename: str):
        """
        Конструктор класса, который принимает имя файла.

        :param filename: Имя файла для работы.
        """
        self.filename = filename

    def read_file(self) -> str:
        """
        Метод для чтения данных из TXT файла.

        :return: Содержимое файла в виде строки. Если файл не найден, возвращает пустую строку.
        """
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
        """
        Метод для записи данных в TXT файл, перезаписывая его содержимое.

        :param data: Произвольное количество строк для записи.
        """
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                for line in data:
                    file.write(line)
        except Exception as e:
            print(f"Произошла ошибка при записи в файл: {e}")

    def append_file(self, *data: str) -> None:
        """
        Метод для добавления данных в конец TXT файла.

        :param data: Произвольное количество строк для добавления.
        """
        try:
            with open(self.filename, 'a', encoding='utf-8') as file:
                for line in data:
                    file.write(line)
        except Exception as e:
            print(f"Произошла ошибка при добавлении в файл: {e}")


# Пример использования и тестирование класса
if __name__ == "__main__":
    filename = "my_file.txt"
    handler = TxtFileHandler(filename)

    # Запись в файл
    handler.write_file("Это тестовая строка.\n")

    # Добавление в файл
    handler.append_file("Это добавленная строка.\n")

    # Чтение из файла
    content = handler.read_file()
    print("Содержимое файла:")
    print(content)

    # Тестирование отсутствия файла
    handler_not_found = TxtFileHandler("non_existent_file.txt")
    print("Чтение из несуществующего файла:")
    print(handler_not_found.read_file())