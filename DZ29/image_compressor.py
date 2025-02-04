import os
from typing import Tuple
from PIL import Image
from pillow_heif import register_heif_opener


class ImageCompressor:
    """Класс для сжатия изображений и обработки директорий."""
    
    supported_formats: Tuple[str, ...] = ('.jpg', '.jpeg', '.png')
    
    def __init__(self, quality: int) -> None:
        """
        Инициализирует экземпляр компрессора с заданным качеством сжатия.
        
        Args:
            quality: Качество сжатия (1-100)
        """
        self.__quality = quality
        register_heif_opener()
    
    @property
    def quality(self) -> int:
        """Возвращает текущее качество сжатия."""
        return self.__quality
    
    @quality.setter
    def quality(self, value: int) -> None:
        """
        Устанавливает новое качество сжатия.
        
        Args:
            value: Новое значение качества (1-100)
            
        Raises:
            ValueError: Если значение вне допустимого диапазона
        """
        if 1 <= value <= 100:
            self.__quality = value
        else:
            raise ValueError("Качество должно быть в диапазоне от 1 до 100")
    
    def compress_image(self, input_path: str, output_path: str) -> None:
        """
        Сжимает изображение и сохраняет в формате HEIF.
        
        Args:
            input_path: Путь к исходному изображению
            output_path: Путь для сохранения результата
        """
        with Image.open(input_path) as img:
            img.save(output_path, "HEIF", quality=self.__quality)
        print(f"Сжато: {input_path} -> {output_path}")
    
    def process_directory(self, directory: str) -> None:
        """
        Обрабатывает все изображения в директории и поддиректориях.
        
        Args:
            directory: Путь к целевой директории
        """
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(self.supported_formats):
                    input_path = os.path.join(root, file)
                    output_path = os.path.splitext(input_path)[0] + '.heic'
                    self.compress_image(input_path, output_path)


def main(input_path: str) -> None:
    """
    Основная функция обработки ввода пользователя.
    
    Args:
        input_path: Путь к файлу или директории
    """
    compressor = ImageCompressor(quality=50)
    input_path = input_path.strip('"')
    
    if os.path.exists(input_path):
        if os.path.isfile(input_path):
            print(f"Обрабатываем файл: {input_path}")
            output_path = os.path.splitext(input_path)[0] + '.heic'
            compressor.compress_image(input_path, output_path)
        elif os.path.isdir(input_path):
            print(f"Обрабатываем директорию: {input_path}")
            compressor.process_directory(input_path)
    else:
        print("Указанный путь не существует")


if __name__ == "__main__":
    user_input: str = input("Введите путь к файлу или директории: ")
    main(user_input)