import multiprocessing


# Функція для підрахунку суми частини масиву
def sum_chunk(chunk, result, index):
    total = sum(chunk)
    result[index] = total


# Головна функція для поділу масиву на частини та паралельного обчислення
def parallel_sum(array, num_processes):
    # Розділяємо масив на частини
    chunk_size = len(array) // num_processes
    chunks = [array[i * chunk_size: (i + 1) * chunk_size] for i in range(num_processes)]

    # Список для зберігання результатів
    manager = multiprocessing.Manager()
    result = manager.dict()

    # Створення процесів
    processes = []
    for i, chunk in enumerate(chunks):
        process = multiprocessing.Process(target=sum_chunk, args=(chunk, result, i))
        processes.append(process)
        process.start()

    # Очікуємо завершення всіх процесів
    for process in processes:
        process.join()

    # Підсумовуємо всі результати
    total_sum = sum(result.values())
    return total_sum


# Приклад використання
if __name__ == "__main__":
    # Великий масив чисел
    array = [i for i in range(1, 1000001)]  # Масив з 1 до 1 млн

    # Кількість процесів
    num_processes = 4

    total_sum = parallel_sum(array, num_processes)
    print(f"Total sum: {total_sum}")
