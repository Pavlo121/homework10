import concurrent.futures
import math


# Функція для обчислення частини факторіала
def partial_factorial(start, end):
    result = 1
    for i in range(start, end):
        result *= i
    return result


# Функція для обчислення факторіала з використанням кількох потоків
def parallel_factorial(n, num_threads=4):
    # Розбиваємо обчислення на кілька частин
    step = n // num_threads
    ranges = [(i * step + 1, (i + 1) * step + 1) if i != num_threads - 1 else (i * step + 1, n + 1) for i in
              range(num_threads)]

    # Використовуємо потоки для обчислення частин факторіала
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda r: partial_factorial(r[0], r[1]), ranges))

    # Об'єднуємо результати
    total_result = 1
    for res in results:
        total_result *= res

    return total_result


if __name__ == "__main__":
    number = int(input("Введіть число для обчислення факторіала: "))
    threads = int(input("Введіть кількість потоків: "))

    result = parallel_factorial(number, threads)
    print(f"Факторіал числа {number} дорівнює {result}")
