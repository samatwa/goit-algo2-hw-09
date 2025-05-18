import random
import math


# Визначення функції Сфери
def sphere_function(x):
    return sum(xi**2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current_point = [random.uniform(bound[0], bound[1]) for bound in bounds]
    current_value = func(current_point)

    for _ in range(iterations):
        # Генеруємо сусідню точку
        neighbor = [
            max(min(current_point[i] + random.uniform(-0.1, 0.1), bounds[i][1]), bounds[i][0])
            for i in range(len(bounds))
        ]
        neighbor_value = func(neighbor)

        # Якщо сусідня точка краща, оновлюємо поточну
        if neighbor_value < current_value:
            if abs(current_value - neighbor_value) < epsilon:
                break
            current_point, current_value = neighbor, neighbor_value

    return current_point, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    current_point = [random.uniform(bound[0], bound[1]) for bound in bounds]
    current_value = func(current_point)

    for _ in range(iterations):
        # Генеруємо випадкову точку в межах
        new_point = [random.uniform(bound[0], bound[1]) for bound in bounds]
        new_value = func(new_point)

        # Якщо кандидат кращий, оновлюємо поточну
        if new_value < current_value:
            if abs(current_value - new_value) < epsilon:
                break
            current_point, current_value = new_point, new_value

    return current_point, current_value


# Simulated Annealing
def simulated_annealing(
    func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6
):
    current_point = [random.uniform(bound[0], bound[1]) for bound in bounds]
    current_value = func(current_point)
    best = current_point[:]
    best_value = current_value

    for _ in range(iterations):
        # Зменшуємо температуру
        if temp < epsilon:
            break

        # Генеруємо сусідню точку
        neighbor = [
            max(min(current_point[i] + random.uniform(-0.5, 0.5), bounds[i][1]), bounds[i][0])
            for i in range(len(bounds))
        ]
        neighbor_value = func(neighbor)
        delta = neighbor_value - current_value

        # Якщо сусідня точка краща, або приймаємо гіршу з ймовірністю
        if delta < 0 or math.exp(-delta / temp) > random.random():
            current_point, current_value = neighbor, neighbor_value
            if current_value < best_value:
                best, best_value = current_point[:], current_value

        temp *= cooling_rate

    return best, best_value


if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)