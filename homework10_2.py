from concurrent.futures import ProcessPoolExecutor, as_completed
from PIL import Image
import os

input_images = "input_images"
output_images = "output_images"
new_size = (800, 600)

# Функція для обробки одного зображення
def process_image(filename):
    if filename.endswith(".jpg"):
        with Image.open(os.path.join(input_images, filename)) as img:
            img = img.resize(new_size)
            img.save(os.path.join(output_images, filename))
            print(f"Обработано: {filename}")

# Паралельна обробка зображень за допомогою ProcessPoolExecutor
with ProcessPoolExecutor() as executor:
    # Запускаємо обробку зображень у потоках
    futures = [executor.submit(process_image, file) for file in os.listdir(input_images)]

    # Очікуємо завершення кожного потоку
    for future in as_completed(futures):
        future.result()

print("Все изображения обработаны.")
