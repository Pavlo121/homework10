import threading


# Функція для пошуку тексту у файлі
def search_in_file(file_name, search_text):
    with open(file_name, 'r', encoding='utf-8') as file:
        line_number = 1
        for line in file:
            if search_text in line:
                print(f"Знайдено '{search_text}' у файлі {file_name} на рядку {line_number}")
            line_number += 1


# Функція для запуску пошуку в окремому потоці
def search_in_file_thread(file_name, search_text):
    thread = threading.Thread(target=search_in_file, args=(file_name, search_text))
    thread.start()
    return thread


# Основна функція для запуску пошуку в кількох файлах
def main():
    search_text = input("Введіть текст для пошуку: ")
    files = [
        'file1.txt',
        'file2.txt',
        'file3.txt'
    ]

    threads = []
    for file in files:
        thread = search_in_file_thread(file, search_text)
        threads.append(thread)

    # Чекаємо завершення всіх потоків
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
