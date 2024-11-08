import random
import threading
import time


# Клас для представлення організму
class Organism:
    def __init__(self, id, energy):
        self.id = id  # Унікальний ідентифікатор організму
        self.energy = energy  # Енергія організму

# Метод для годування організму
    def feed(self, food_amount):
        self.energy += food_amount

# Метод для розмноження організму
    def reproduce(self):
        if self.energy > 20:
            new_organism = Organism(id=f"{self.id}_child", energy=10)
            self.energy -= 10
            return new_organism
        return None

#Метод для старіння організму
    def age(self):
        self.energy -= 1  # Втрата енергії через старіння

#Перевірка чи живий організм
    def is_alive(self):
        return self.energy > 0


# Функція для симуляції обробки одного організму
def simulate_organism(organism, food_supply):
    # Організм їсть
    organism.feed(food_supply)

    # Організм розмножується
    new_organism = organism.reproduce()
    if new_organism:
        population.append(new_organism)
        print(f"Організм {organism.id} розмножився і створив нового організму {new_organism.id}")

    # Організм старіє
    organism.age()

    # Перевірка чи організм все ще живий
    if organism.is_alive():
        print(f"Організм {organism.id} вижив з енергією {organism.energy}")
    else:
        print(f"Організм {organism.id} помер")


# Функція для запуску симуляції популяції
def simulate_population():
    global population

    # Параметри симуляції
    food_supply = 5  # Кількість їжі, яку кожен організм отримує
    generations = 10  # Кількість поколінь для симуляції

    for generation in range(generations):
        print(f"\n--- Покоління {generation + 1} ---")

        # Створення потоків для кожного організму
        threads = []
        for organism in population:
            thread = threading.Thread(target=simulate_organism, args=(organism, food_supply))
            threads.append(thread)
            thread.start()

        # Очікуємо завершення всіх потоків
        for thread in threads:
            thread.join()

        # Фільтруємо мертвих організмів
        population = [organism for organism in population if organism.is_alive()]

        # Якщо популяція порожня, завершуємо симуляцію
        if not population:
            print("Популяція вимерла.")
            break


# Ініціалізація початкової популяції
population = [Organism(id=f"organism_{i}", energy=random.randint(5, 15)) for i in range(10)]

# Запуск симуляції
simulate_population()
