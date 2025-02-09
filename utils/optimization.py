from django.db import models
from PIL import Image
import os

def optimize_image(image_field, max_size=1024, quality=85):
    """
    Оптимизирует изображение:
    - Уменьшает размер, если больше max_size
    - Сохраняет пропорции
    - Конвертирует в WebP
    - Обновляет путь в Django ImageField

    :param image_field: Поле модели Django (например, instance.image)
    :param max_size: Максимальная длина любой стороны (по умолчанию 1024px)
    :param quality: Качество WebP (0-100)
    """
    image_path = image_field.path
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

        img = img.resize((new_width, new_height), Image.LANCZOS)

    # Меняем формат на WebP, но сохраняем структуру папок
    webp_path = image_path.rsplit(".", 1)[0] + ".webp"  # Просто заменяем расширение
    img.save(webp_path, "WEBP", quality=quality)  # Сжимаем и сохраняем

    # Обновляем путь в Django ImageField
    relative_path = os.path.relpath(webp_path, os.path.dirname(image_path))
    image_field.name = os.path.join(os.path.dirname(image_field.name), relative_path)
