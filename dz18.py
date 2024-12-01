def caesar_encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            if char in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
                base = ord("А")  # База для русских букв
                encrypted_char = chr((ord(char) - base + shift) % 32 + base)
            elif char in "abcdefghijklmnopqrstuvwxyz":
                base = ord("a")  # База для английских букв
                encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                encrypted_char = char  # Для других символов добавляем без изменений
        elif char == " ":  # Проверяем, является ли символ пробелом
            encrypted_char = char  # Оставляем пробел без изменений
        else:  # Для остальных символов
            # Используем ord() и chr() для их обработки
            encrypted_char = chr(ord(char) + shift)

        encrypted_text += encrypted_char  # Добавляем зашифрованный символ

    return encrypted_text


# Запрашиваем ввод у пользователя
text = input("Введите текст на русском или английском языке: ")
shift = int(input("Введите значение сдвига (число): "))

# Вызываем функцию шифрования
encrypted = caesar_encrypt(text, shift)
print("Зашифрованный текст:", encrypted)
