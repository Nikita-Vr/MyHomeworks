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
    
    