import os
import cairosvg
from django.db import models
from PIL import Image

def optimize_image(image_field, max_size=1024, quality=95):
    """
    Оптимизирует изображения:
    - SVG → Конвертирует в PNG, а затем в WebP (или JPEG/PNG)
    - PNG/JPEG → Оптимизирует и конвертирует в WebP (или JPEG/PNG)
    - Уменьшает размер, если больше max_size
    - Сохраняет пропорции

    :param image_field: Поле модели Django (например, instance.image)
    :param max_size: Максимальная длина любой стороны (по умолчанию 1024px)
    :param quality: Качество WebP (0-100)
    """
    image_path = image_field.path
    file_extension = os.path.splitext(image_path)[1].lower()  # Расширение файла

    # Если это SVG, конвертируем его в PNG
    if file_extension == ".svg":
        png_path = image_path.rsplit(".", 1)[0] + ".png"
        cairosvg.svg2png(url=image_path, write_to=png_path)  # Конвертируем SVG → PNG
        image_path = png_path  # Теперь работаем с PNG

    # Открываем изображение с Pillow
    img = Image.open(image_path)
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

    # Меняем формат на WebP (или можно оставить PNG/JPEG)
    webp_path = image_path.rsplit(".", 1)[0] + ".webp"
    img.save(webp_path, "WEBP", quality=quality)  # Сжимаем и сохраняем

    # Обновляем путь в Django ImageField
    relative_path = os.path.relpath(webp_path, os.path.dirname(image_path))
    image_field.name = os.path.join(os.path.dirname(image_field.name), relative_path)

