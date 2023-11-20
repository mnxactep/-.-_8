from itertools import permutations

while True:
    try:
        N = int(input("Введите количество сотрудников: "))
        if N <= 0:
            raise ValueError
        break
    except ValueError:
        print("Количество сотрудников должно быть целым положительным числом")

while True:
    try:
        distances = list(map(int, input(f"Введите расстояния до домов для каждого из {N} сотрудников: ").split()))
        if len(distances) != N or any(d < 0 for d in distances):
            raise ValueError
        break
    except ValueError:
        print(f"Введите {N} положительных чисел, разделенных пробелом")

while True:
    try:
        tariffs = list(map(int, input(f"Введите тарифы за проезд для каждого из {N} такси: ").split()))
        if len(tariffs) != N or any(t < 0 for t in tariffs):
            raise ValueError
        break
    except ValueError:
        print(f"Введите {N} положительных чисел, разделенных пробелом")

min_cost = float('inf')
min_permutation = []

for permutation in permutations(range(N)):
    cost = sum(distances[i] * tariffs[permutation[i]] for i in range(N))
    if cost < min_cost:
        min_cost = cost
        min_permutation = permutation

print("Оптимальное распределение такси для сотрудников:")
for i, p in enumerate(min_permutation):
    print(f"Сотрудник {i+1} должен ехать на такси {p+1}")

print(f"Общая стоимость: {min_cost} Рубля" if min_cost == 1 else f"Общая стоимость: {min_cost} Рублей")
