from django.db import models
from PIL import Image
import os

def optimize_image(image_path, max_size=1024, quality=55):
    """
    Оптимизирует изображение:
    - Сжимает, если изображение больше max_size
    - Сохраняет пропорции
    - Конвертирует в WebP

    :param image_path: Путь к изображению
    :param max_size: Максимальный размер (ширина или высота)
    :param quality: Качество сохранения WebP (0-100)
    """
    img = Image.open(image_path)

    # Определяем текущий размер
    width, height = img.size

    # Проверяем, нужно ли уменьшение
    if width > max_size or height > max_size:
        if width > height:
            new_width = max_size
            new_height = int((max_size / width) * height)
        else:
            new_height = max_size
            new_width = int((max_size / height) * width)

        img = img.resize((new_width, new_height), Image.LANCZOS)  # Масштабируем

    # Меняем формат на WebP
    webp_path = os.path.splitext(image_path)[0] + ".webp"
    img.save(webp_path, "WEBP", quality=quality)  # Сжимаем
    print('получилось')
    return webp_path  # Возвращаем путь к WebP-файлу