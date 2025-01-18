class TxtFileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """Читает содержимое текстового файла и возвращает его как строку."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден.")
            return None
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")
            return None

    